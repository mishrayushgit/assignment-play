# Soundverse Play API

A lightweight audio library backend service that lets users fetch and stream short hip-hop audio previews, built with FastAPI and PostgreSQL.

---

## Live Demo

**Base URL:** `https://soundverse-play-dvij.onrender.com/`

> All endpoints require an API key. Contact for access .

---

## 📁 Project Structure

```
soundverse-play/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── config.py            # Environment config with Pydantic
│   ├── routes/
│   │   └── play.py          # All /play endpoints
│   ├── models/
│   │   └── clip.py          # SQLAlchemy DB model
│   ├── schemas/
│   │   └── clip.py          # Pydantic request/response schemas
│   ├── middleware/
│   │   └── auth.py          # API key authentication
│   └── db/
│       ├── database.py      # DB connection and session
│       └── seed.py          # Seed script for initial clips
├── tests/
│   └── test_api.py          # Pytest test suite
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI pipeline
├── docker-compose.yml       # Prometheus + Grafana monitoring
├── prometheus.yml           # Prometheus scrape config
├── Procfile                 # Render start command
├── requirements.txt         # Python dependencies
└── .env                     # Environment variables (not committed)
```

---

## Tech Stack

- **FastAPI** — Python web framework
- **PostgreSQL** — Database (hosted on Neon.tech)
- **SQLAlchemy** — ORM for database interaction
- **Pydantic** — Data validation and settings management
- **Prometheus + Grafana** — Monitoring and metrics
- **Render** — Cloud deployment
- **GitHub Actions** — CI/CD pipeline

---

##  API Endpoints

All endpoints require the following header:
```
X-API-Key: <your-api-key>
```

### GET `/`
Health check — returns API status.

**Response:**
```json
{
  "message": "Soundverse Play API is running"
}
```

---

### GET `/play`
Returns a list of all audio clips.

**Response:**
```json
[
  {
    "id": 1,
    "title": "Street Dreams",
    "description": "Hard hitting hip hop beat from the streets",
    "genre": "hip-hop",
    "duration": "30s",
    "audio_url": "https://...",
    "play_count": 5
  }
]
```

---

### GET `/play/{id}/stream`
Streams the audio clip and increments its play count.

**Example:** `GET /play/1/stream`

**Response:** Audio stream (`audio/mpeg`)

---

### GET `/play/{id}/stats`
Returns metadata and play count for a specific clip.

**Example:** `GET /play/1/stats`

**Response:**
```json
{
  "id": 1,
  "title": "Street Dreams",
  "genre": "hip-hop",
  "duration": "30s",
  "play_count": 5
}
```

---

### POST `/play`
Add a new clip entry (metadata only, no file upload).

**Request Body:**
```json
{
  "title": "Trap Banger",
  "description": "Hard trap beat with 808s",
  "genre": "trap",
  "duration": "30s",
  "audio_url": "https://example.com/audio.mp3"
}
```

---

## Database Schema

```sql
CREATE TABLE clips (
    id          SERIAL PRIMARY KEY,
    title       VARCHAR NOT NULL,
    description VARCHAR,
    genre       VARCHAR,
    duration    VARCHAR,
    audio_url   VARCHAR NOT NULL,
    play_count  INTEGER DEFAULT 0
);
```

---

## Running Locally

### Prerequisites
- Python 3.12+
- uv package manager
- Docker Desktop (for monitoring)
- PostgreSQL database (Neon.tech recommended)

### Setup

**1. Clone the repo:**
```bash
git clone https://github.com/yourusername/soundverse-play.git
cd soundverse-play
```

**2. Create virtual environment and install dependencies:**
```bash
uv venv
.venv\Scripts\activate  # Windows
uv sync
```

**3. Create `.env` file:**
```env
DATABASE_URL=postgresql://username:password@host/dbname?sslmode=require
API_KEY=your_api_key_here
```

**4. Seed the database:**
```bash
python -m app.db.seed
```

**5. Run the server:**
```bash
uvicorn app.main:app --reload
```

API will be live at `http://localhost:8000`
Auto docs at `http://localhost:8000/docs`

---

## Monitoring

Prometheus and Grafana run locally via Docker.

**Start monitoring:**
```bash
docker-compose up
```

| Service | URL |
|---|---|
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |

**Grafana login:** `admin` / check your `.env`

**Metrics tracked:**
- Total API requests (`starlette_requests_total`)
- Requests by endpoint
- Response latency (`starlette_request_duration_seconds_sum`)

---

## Running Tests

```bash
pytest
```

Tests cover:
- Root health check
- Get all clips
- Get clip stats
- Clip not found (404)
- Create new clip

---

## CI/CD

GitHub Actions automatically runs on every push:
1. **Linting** — flake8 checks code quality
2. **Tests** — pytest runs full test suite

---

## Authentication

All API endpoints are protected with an API key.

Pass it in the request header:
```
X-API-Key: <contact for access>
```

---
