import uvicorn
from fastAPI.app import app  # FastAPI 애플리케이션 가져오기

# FastAPI 실행
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)