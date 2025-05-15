from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastAPI.core import logic
from gradio_ui.interface import gradio_app  # 여기서 gradio_app은 .app 객체여야 함

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/gradio", gradio_app)  # 문제 없음

@app.get("/api/greet")
def api_greet(name: str):
    return {"message": logic.greet(name)}
