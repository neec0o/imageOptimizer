from PIL import Image
import zipfile
from pathlib import Path

def optimize_image(image_path: Path, max_width: int, max_height: int, quality: int):
    #Bild mit User Werten anpassen
    with Image.open(image_path) as img:
        original_width, original_height = img.size

        # Berechne neue Größe, behalte Aspect Ratio
        if original_width > max_width or original_height > max_height:
            img.thumbnail((max_width, max_height)) # Image skalieren
		# Entferne Meta-Daten (EXIF)
        img_without_exif = Image.new("RGB", img.size)
        img_without_exif.paste(img)
        # Speichere das optimierte Image
        img_without_exif.save(image_path, img.format, quality=quality)

def create_zip(folder_path: Path, session_id: str) -> Path:
    zip_path = folder_path / f"{session_id}.zip"

    with zipfile.ZipFile(zip_path, "w") as zipf:
        for file in folder_path.iterdir():
            if file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                zipf.write(file, arcname=file.name)

    return zip_path
