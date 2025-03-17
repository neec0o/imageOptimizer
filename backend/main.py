from fastapi import FastAPI
from routes import upload, download, user

app = FastAPI()

# Endpoints einbinden
app.include_router(user.router)
app.include_router(upload.router)
app.include_router(download.router)
