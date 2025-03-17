const API_URL = "http://backend:8000";  // Backend-URL im Docker-Netzwerk

async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const response = await fetch(`${API_URL}/token`, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `username=${username}&password=${password}`
    });

    const data = await response.json();
    if (response.ok) {
        localStorage.setItem("token", data.access_token);
        document.getElementById("login-container").style.display = "none";
        document.getElementById("upload-container").style.display = "block";
    } else {
        document.getElementById("login-message").innerText = "Login fehlgeschlagen!";
    }
}

async function uploadImages() {
    const fileInput = document.getElementById("fileInput");
    const maxWidth = document.getElementById("maxWidth").value;
    const maxHeight = document.getElementById("maxHeight").value;
    const quality = document.getElementById("quality").value;
    const token = localStorage.getItem("token");

    if (!fileInput.files.length) {
        alert("Bitte wähle eine Datei aus!");
        return;
    }

    const formData = new FormData();
    for (let file of fileInput.files) {
        formData.append("file", file);
    }
    formData.append("max_width", maxWidth);
    formData.append("max_height", maxHeight);
    formData.append("quality", quality);

    const response = await fetch(`${API_URL}/upload`, {
        method: "POST",
        headers: { "Authorization": `Bearer ${token}` },
        body: formData
    });

    const data = await response.json();
    document.getElementById("upload-message").innerText = "Upload erfolgreich!";
}

async function downloadZip() {
    const token = localStorage.getItem("token");
    const response = await fetch(`${API_URL}/download`, {
        method: "GET",
        headers: { "Authorization": `Bearer ${token}` }
    });

    if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "bilder.zip";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    } else {
        alert("Fehler beim Herunterladen der Bilder!");
    }
}
