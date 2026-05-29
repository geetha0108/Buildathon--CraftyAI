import logging
from typing import Optional
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from config import HOST, PORT
from services import CrochetService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("main")

app = FastAPI(
    title="CraftyAI - Crochet Assistant Backend",
    description="FastAPI backend to connect CraftyAI frontend with local LM Studio & Gemma 4 E4B",
    version="1.0.0"
)

# Enable CORS for frontend connection (crucial for local/cross-origin development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify backend status.
    """
    return {
        "status": "healthy",
        "service": "CraftyAI Backend",
        "description": "FastAPI is running and ready to handle requests."
    }

@app.post("/generate")
async def generate(
    prompt: str = Form(...),
    image: Optional[UploadFile] = File(None)
):
    """
    Generate crochet patterns using prompt text and an optional uploaded image.
    Sends multimodal input to local LM Studio running Gemma 4 E4B.
    """
    logger.info(f"Received generation request. Prompt: {prompt[:100]}...")
    if image:
        logger.info(f"Image received: {image.filename} (content_type: {image.content_type})")
    else:
        logger.info("No image provided.")

    try:
        pattern = await CrochetService.generate_pattern(prompt=prompt, image=image)
        logger.info("Successfully generated and validated crochet pattern.")
        return pattern
    except Exception as e:
        logger.error(f"Error during pattern generation: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Pattern generation failed: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    logger.info(f"Starting server on {HOST}:{PORT}")
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
