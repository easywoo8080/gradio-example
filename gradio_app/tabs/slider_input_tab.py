import gradio as gr
import requests
from config.config import FASTAPI_URL

url = f"{FASTAPI_URL}/list"

def get_api(value):
    try:
        res = requests.get(url, params={"name": str(value)}, timeout=(1, 2))
        return res.json().get("message", "오류 발생")
    except Exception as e:
        return f"에러: {e}"

def create_tab():
    with gr.Row():
        slider_input = gr.Slider(minimum=0, maximum=1010, step=2, label="Influx Text")
        slider_output = gr.Textbox(label="Greeting")
    slider_btn = gr.Button("Greet")
    slider_btn.click(fn=get_api, inputs=slider_input, outputs=slider_output)
    return [slider_input, slider_output, slider_btn]
