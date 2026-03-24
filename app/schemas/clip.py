from pydantic import BaseModel
from typing import Optional

class ClipBase(BaseModel):
    title: str
    description: Optional[str] = None
    genre: Optional[str] = None
    duration: Optional[str] = None
    audio_url: str

class ClipCreate(ClipBase):
    pass

class ClipResponse(ClipBase):
    id: int
    play_count: int

    class Config:
        from_attributes = True