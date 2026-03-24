from pydantic import BaseModel, ConfigDict
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
    model_config = ConfigDict(from_attributes=True)

    id: int
    play_count: int
