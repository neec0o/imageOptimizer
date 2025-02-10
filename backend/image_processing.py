from PIL import Image
from pathlib import Path

def optimize_image(image_path: Path, output_path: Path, max_width: int = 800, quality: int = 70):
    """Skaliert und optimiert ein Bild für das Web."""
    with Image.open(image_path) as img:
        # Originalmaße abrufen
        width, height = img.size

        # Verhältnis berechnen und neue Größe setzen
        if width > max_width:
            ratio = max_width / width
            new_size = (max_width, int(height * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)

        # Optimiertes Bild speichern
        img.save(output_path, quality=quality, optimize=True)
