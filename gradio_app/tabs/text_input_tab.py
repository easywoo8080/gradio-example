# tab/input/text_input_tab.py
import gradio as gr
import requests
from config.config import FASTAPI_URL  # 공통 API_URL import

url = f"{FASTAPI_URL}/list"


def greet(name):
    try:
        res = requests.get(url, params={"name": name}, timeout=(1, 2))
        return res.json().get("message", "오류 발생")
    except Exception as e:
        return f"에러: {e}"

def create_tab():
    name_input = gr.Textbox(label="Name")
    greet_output = gr.Textbox(label="Greeting")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name_input, outputs=greet_output)
