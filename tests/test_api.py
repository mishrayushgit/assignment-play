from fastapi.testclient import TestClient
from app.main import app
from dotenv import load_dotenv
import os
load_dotenv()
client = TestClient(app, headers={"X-API-Key": os.getenv("API_KEY")})

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}


def test_get_clips():
    response = client.get("/play")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_stats():
    response = client.get("/play/1/stats")
    assert response.status_code == 200
    data = response.json()
    assert "play_count" in data
    assert "title" in data


def test_clip_not_found():
    response = client.get("/play/999/stats")
    assert response.status_code == 404


def test_create_clip():
    response = client.post("/play", json={
        "title": "Test Beat",
        "description": "A test hip hop beat",
        "genre": "hip-hop",
        "duration": "30s",
        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Test Beat"