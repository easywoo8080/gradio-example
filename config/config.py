import os

# 환경 변수에서 값 가져오기
FASTAPI_HOST = os.getenv("DEV_FASTAPI_HOST", "0.0.0.0")
FASTAPI_PORT = int(os.getenv("DEV_FASTAPI_PORT", 8000))
FASTAPI_URL = f"http://localhost:{FASTAPI_PORT}/api"  # f-string으로 수정

GRADIO_HOST = os.getenv("DEV_GRADIO_HOST", "0.0.0.0")
GRADIO_PORT = int(os.getenv("DEV_GRADIO_PORT", 7860))
