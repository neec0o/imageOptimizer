import os
import time
from pathlib import Path

# temporären Dateien
TEMP_DIR = Path("temp")
DELETE_AFTER_MINUTES = 10  # mins bis loeschung

def cleanup_old_files():
    now = time.time()
    for folder in TEMP_DIR.iterdir():
        if folder.is_dir():  
            for file in folder.iterdir():
                if file.is_file():
                    file_age_minutes = (now - file.stat().st_mtime) / 60  
                    if file_age_minutes > DELETE_AFTER_MINUTES:
                        print(f"Lösche {file} (Alter: {file_age_minutes:.1f} Minuten)")
                        file.unlink()  # Datei löschen
            
            # Falls der Ordner nach dem Löschen leer ist → löschen
            if not any(folder.iterdir()):
                print(f"Lösche leeren Ordner {folder}")
                folder.rmdir()

if __name__ == "__main__":
    while True:
        cleanup_old_files()
        print("Cleanup abgeschlossen. Warte 5 Minuten...")
        time.sleep(300)  # 5 Minuten, bevor der nächste Cleanup läuft
