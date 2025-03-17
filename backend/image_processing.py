from PIL import Image
import zipfile
from pathlib import Path

def optimize_image(image_path: Path, max_width: int, max_height: int, quality: int):
    """ Optimiert das Bild, entfernt Metadaten und speichert es mit neuer Größe & Qualität. """
    with Image.open(image_path) as img:
        original_width, original_height = img.size

        # Berechne neue Größe, behalte Aspect Ratio
        if original_width > max_width or original_height > max_height:
            img.thumbnail((max_width, max_height))  # Skaliert das Bild direkt

        # Entferne Metadaten (EXIF)
        exif_data = img.info.get("exif")  # Falls vorhanden, wird es entfernt
        img = img.convert("RGB") if img.mode in ("RGBA", "P") else img

        # Speichern ohne EXIF für JPGs
        save_params = {"quality": quality}
        if img.format == "JPEG" and exif_data:
            save_params["exif"] = b""  # Entfernt EXIF-Daten bei JPEGs

        img.save(image_path, img.format, **save_params)

def create_zip(folder_path: Path, session_id: str) -> Path:
    """ Erstellt ein ZIP-Archiv mit allen optimierten Bildern. """
    zip_path = folder_path / f"{session_id}.zip"

    with zipfile.ZipFile(zip_path, "w") as zipf:
        for file in folder_path.iterdir():
            if file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                zipf.write(file, arcname=file.name)

    return zip_path
