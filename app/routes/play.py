from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.clip import Clip
from app.schemas.clip import ClipResponse, ClipCreate
from typing import List
import httpx
from fastapi.responses import StreamingResponse
router = APIRouter()

# GET /play - return all clips
@router.get("/", response_model=List[ClipResponse])
def get_clips(db: Session = Depends(get_db)):
    clips = db.query(Clip).all()
    return clips

# GET /play/{id}/stream - stream a clip
@router.get("/{clip_id}/stream")
async def stream_clip(clip_id: int, db: Session = Depends(get_db)):
    clip = db.query(Clip).filter(Clip.id == clip_id).first()
    
    if not clip:
        raise HTTPException(status_code=404, detail="Clip not found")
    
   
    clip.play_count += 1
    db.commit()

    
    async def audio_stream():
        async with httpx.AsyncClient() as client:
            async with client.stream("GET", clip.audio_url) as response:
                async for chunk in response.aiter_bytes():
                    yield chunk

    return StreamingResponse(
        audio_stream(),
        media_type="audio/mpeg",
        headers={"Content-Disposition": f"inline; filename={clip.title}.mp3"}
    )
# GET /play/{id}/stats - get stats for a clip
@router.get("/{clip_id}/stats")
def get_stats(clip_id: int, db: Session = Depends(get_db)):
    clip = db.query(Clip).filter(Clip.id == clip_id).first()
    
    if not clip:
        raise HTTPException(status_code=404, detail="Clip not found")
    
    return {
        "id": clip.id,
        "title": clip.title,
        "genre": clip.genre,
        "duration": clip.duration,
        "play_count": clip.play_count
    }

# POST /play - add a new clip 
@router.post("/", response_model=ClipResponse)
def create_clip(clip: ClipCreate, db: Session = Depends(get_db)):
    new_clip = Clip(**clip.model_dump())
    db.add(new_clip)
    db.commit()
    db.refresh(new_clip)
    return new_clip