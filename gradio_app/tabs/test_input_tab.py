# tab/input/text_input_tab.py
import gradio as gr
import requests
from config.config import FASTAPI_URL  # 공통 API_URL import

url = f"{FASTAPI_URL}/list"

def get_api(name):
    try:
        res = requests.get(url, params={"name": name}, timeout=(1, 2))
        data = res.json()  # 이 줄에서 문제가 발생할 수 있음
        return data.get("message", "오류 발생")
    except requests.exceptions.RequestException as e:
        return f"요청 오류: {e}"
    except ValueError as e:
        return f"응답 JSON 파싱 오류: {e}"
    except Exception as e:
        return f"기타 오류: {e}"


def create_tab():
    test_input = gr.Textbox(label="test")
    test_output = gr.Textbox(label="Greeting")
    test_btn = gr.Button("Greet")
    test_btn.click(fn=get_api, inputs=test_input, outputs=test_output)
    return [test_input, test_output, test_btn]
