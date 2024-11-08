import uvicorn
from core.config import config

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=config.HOST,
        reload=config.DEBUG_MODE,
        port=8080,
    )