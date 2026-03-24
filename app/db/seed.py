from app.db.database import SessionLocal, engine, Base
from app.models.clip import Clip

# Create tables if doesnt exists
Base.metadata.create_all(bind=engine)

clips = [
    {
        "title": "Chill Lofi Beat",
        "description": "A relaxing lofi beat perfect for studying",
        "genre": "lofi",
        "duration": "30s",
        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    },
    {
        "title": "Ambient Space",
        "description": "Deep ambient sounds from outer space",
        "genre": "ambient",
        "duration": "30s",
        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
    },
    {
        "title": "Electronic Pulse",
        "description": "High energy electronic track",
        "genre": "electronic",
        "duration": "30s",
        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
    },
    {
        "title": "Acoustic Morning",
        "description": "Soft acoustic guitar for a calm morning",
        "genre": "acoustic",
        "duration": "30s",
        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
    },
    {
        "title": "Pop Vibes",
        "description": "Upbeat pop track to get you moving",
        "genre": "pop",
        "duration": "30s",
        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"
    },
    {
        "title": "Jazz Night",
        "description": "Smooth jazz for a late night session",
        "genre": "jazz",
        "duration": "30s",
        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3"
    }
]

def seed():
    db = SessionLocal()
    
    # check
    existing = db.query(Clip).first()
    if existing:
        print("Database already seeded!")
        db.close()
        return
    
    for clip in clips:
        db_clip = Clip(**clip)
        db.add(db_clip)
    
    db.commit()
    db.close()
    print("Database seeded with 6 clips")

if __name__ == "__main__":
    seed()