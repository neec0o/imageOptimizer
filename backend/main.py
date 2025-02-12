from fastapi import FastAPI, File, UploadFile, Depends, Query, Cookie
import shutil
import uuid
from pathlib import Path
from fastapi.responses import FileResponse, JSONResponse
from image_processing import optimize_image, create_zip

app = FastAPI()

#Main Ordner für den ganzen Bumms
TEMP_DIR = Path("temp")
TEMP_DIR.mkdir(exist_ok=True)

def get_user_session(session_id: str = Cookie(default=None)):
    #Session ID abfrühstücken
    if session_id is None:
        new_session_id = str(uuid.uuid4())  # Zufällige UUID generieren
        return new_session_id
    return session_id

@app.post("/upload")
async def upload_image(
    file: UploadFile = File(...),
    max_width: int = Query(1920),
    max_height: int = Query(1080),
    quality: int = Query(80),
    session_id: str = Depends(get_user_session)
):
    # Datei speichern und umbennen mit Sessio ID
    user_folder = TEMP_DIR / session_id
    user_folder.mkdir(exist_ok=True)
    filename = file.filename.rsplit(".", 1) 
    new_filename = f"{filename[0]}_{session_id}.{filename[1]}" if len(filename) > 1 else f"{file.filename}_{session_id}"
    file_location = user_folder / new_filename
    
    with file_location.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Bild optimieren aus der image_processing datei
    optimize_image(file_location, max_width, max_height, quality)

    return JSONResponse(content={"filename": new_filename, "session_id": session_id},
                        headers={"Set-Cookie": f"session_id={session_id}; Path=/; HttpOnly"})

@app.get("/download")
async def download_zip(session_id: str = Depends(get_user_session)):
    #Zip erstellen und Pfad returnen
    user_folder = TEMP_DIR / session_id
    zip_path = create_zip(user_folder, session_id)

    return FileResponse(zip_path, filename=f"{session_id}.zip", media_type="application/zip")
