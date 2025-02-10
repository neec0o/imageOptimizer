###Projektablaufplan: Bildoptimierung mit Python

📁 image-optimizer
 ┣ 📁 backend
 ┃ ┣ 📁 temp  # Temporäre Dateien
 ┃ ┣ 📁 static  # Optimierte Bilder
 ┃ ┣ 📜 main.py  # FastAPI App
 ┃ ┣ 📜 image_processing.py  # Bildverarbeitung
 ┃ ┣ 📜 config.py  # Konfigurationen
 ┃ ┗ 📜 cleanup.py  # Automatische Löschung
 ┣ 📜 Dockerfile
 ┣ 📜 docker-compose.yml
 ┣ 📜 requirements.txt
 ┗ 📜 README.md

 
1️⃣ Projektstruktur & Umgebung aufsetzen
🔹 Ziel: Eine saubere Projektstruktur mit Docker aufsetzen
✅ Schritte:
    📂 Projektordner erstellen
    🐍 Virtuelle Umgebung einrichten (venv)
    📜 requirements.txt mit benötigten Bibliotheken erstellen
    🐳 Dockerfile und docker-compose.yml schreiben
    🏗 Ordnerstruktur vorbereiten
	📌 Technologien & Bibliotheken:
		FastAPI für das Backend
		Uvicorn als ASGI-Server
		Pillow für die Bildbearbeitung
		Zipfile für die Archivierung
		Celery & Redis für die Hintergrund-Jobs
2️⃣ Backend mit FastAPI aufsetzen
🔹 Ziel: Die API-Grundstruktur aufbauen
✅ Schritte:
    FastAPI-Projekt in main.py starten
    Endpunkt für den File-Upload erstellen
    Temporäre Speicherung der Dateien im /temp Ordner
    API mit Uvicorn lokal testen

📌 Beispiel-Endpunkte:
POST /upload  ->  Bilder hochladen  
GET /download/{zip_id}  ->  Zip-Download  
DELETE /cleanup  ->  Manuelle Löschung  

3️⃣ Bilder verarbeiten & optimieren
🔹 Ziel: Hochgeladene Bilder skalieren & optimieren
✅ Schritte:
    Pillow nutzen, um Bildgröße anzupassen
    Qualität reduzieren (JPEG, PNG)
    Ratio beibehalten
    Wenn Bild kleiner als Zielgröße → Originalgröße beibehalten

📌 Regeln für Skalierung:
Falls (Breite > Zielbreite) oder (Höhe > Zielhöhe) → Verkleinern  
Falls (Breite < Zielbreite UND Höhe < Zielhöhe) → Original beibehalten  

4️⃣ ZIP-Datei für Download erstellen
🔹 Ziel: Alle optimierten Bilder als ZIP bereitstellen
✅ Schritte:
    ZIP-Archiv mit zipfile erstellen
    ZIP-ID generieren & speichern
    Download-Link für Nutzer bereitstellen

5️⃣ Automatische Datei-Löschung nach 10 Minuten
🔹 Ziel: Speicherplatz nicht unnötig belegen
✅ Schritte:
    Celery & Redis einbinden
    Hintergrund-Task starten:
        Originalbilder sofort löschen
        ZIP-Dateien nach 10 Minuten entfernen
    Logging für erfolgreiche Löschungen hinzufügen
6️⃣ Docker-Integration & Deployment
🔹 Ziel: Projekt als Docker-Container auf VPS deployen
✅ Schritte:
    Dockerfile schreiben
    docker-compose.yml erstellen
    Redis-Container für Celery hinzufügen
    Backend mit Uvicorn als Service starten
    Logging & Debugging in Docker-Logs einbinden
7️⃣ Testing & Fehlerbehandlung
🔹 Ziel: Fehler abfangen & Logs schreiben
✅ Schritte:
    API mit Postman testen
    Fehlerfälle abdecken (z. B. ungültige Datei, fehlende Parameter)
    Logging mit Python-Logging-Modul einbinden
8️⃣ Optional: Frontend hinzufügen (Falls gewünscht)
🔹 Ziel: Einfaches Web-Interface für Upload & Download
✅ Technologie:
    HTML, JS für UI
