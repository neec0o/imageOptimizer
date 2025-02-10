from fastapi import FastAPI, File, UploadFile
import shutil
import os
from pathlib import Path
from image_processing import optimize_image

# FastAPI App starten
app = FastAPI()

# Verzeichnisse für Uploads & optimierte Bilder
UPLOAD_DIR = Path("temp")
OPTIMIZED_DIR = Path("static")
UPLOAD_DIR.mkdir(exist_ok=True)
OPTIMIZED_DIR.mkdir(exist_ok=True)

@app.post("/upload")
async def upload_and_optimize(file: UploadFile = File(...)):
    """Speichert ein Bild, optimiert es und gibt den neuen Dateipfad zurück"""
    file_location = UPLOAD_DIR / file.filename
    optimized_location = OPTIMIZED_DIR / file.filename

    # Datei speichern
    with file_location.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Bild optimieren
    optimize_image(file_location, optimized_location)

    # Originalbild löschen
    file_location.unlink()

    return {"filename": file.filename, "optimized_path": str(optimized_location)}

# Starte den Server mit: uvicorn main:app --reload
