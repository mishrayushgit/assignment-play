from fastapi import FastAPI
from starlette_exporter import PrometheusMiddleware, handle_metrics
from app.db.database import Base, engine
from app.routes.play import router as play_router

# Create all tables in database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Soundverse Play API",
    description="A lightweight audio library API",
    version="1.0.0"
)

# Prometheus monitoring middleware
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

# Routes
app.include_router(play_router, prefix="/play", tags=["Play"])

@app.get("/")
def root():
    return {"message": "API is running "}