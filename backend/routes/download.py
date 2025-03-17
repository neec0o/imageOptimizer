from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from pathlib import Path
from auth import get_current_user
from image_processing import create_zip

router = APIRouter(prefix="/download", tags=["Download"])

TEMP_DIR = Path("temp")

@router.get("/")
async def download_zip(user: dict = Depends(get_current_user)):
    session_id = user["username"]
    user_folder = TEMP_DIR / session_id
    zip_path = create_zip(user_folder, session_id)

    return FileResponse(zip_path, filename=f"{session_id}.zip", media_type="application/zip")
