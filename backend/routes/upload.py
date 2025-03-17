from fastapi import APIRouter, UploadFile, File, Query, Depends
from pathlib import Path
import shutil
from auth import get_current_user
from image_processing import optimize_image

router = APIRouter(prefix="/upload", tags=["Upload"])

TEMP_DIR = Path("temp")
TEMP_DIR.mkdir(exist_ok=True)

@router.post("/")
async def upload_image(
    file: UploadFile = File(...),
    max_width: int = Query(1920),
    max_height: int = Query(1080),
    quality: int = Query(80),
    user: dict = Depends(get_current_user)
):
    session_id = user["username"]
    user_folder = TEMP_DIR / session_id
    user_folder.mkdir(exist_ok=True)

    filename = file.filename.rsplit(".", 1)
    new_filename = f"{filename[0]}_{session_id}.{filename[1]}" if len(filename) > 1 else f"{file.filename}_{session_id}"
    file_location = user_folder / new_filename
    
    with file_location.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    optimize_image(file_location, max_width, max_height, quality)

    return {"filename": new_filename, "session_id": session_id}
