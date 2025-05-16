import gradio as gr
import importlib
from config.config import GRADIO_HOST, GRADIO_PORT
from gradio_app.tabs.text_input_tab import create_tab as text_input_tab
from gradio_app.tabs.slider_input_tab import create_tab as slider_input_tab
from gradio_app.tabs.test_input_tab import create_tab as test_input_tab

# (모듈명, 한글 라벨) 순서로 명시
TAB_INFOS = [
    ("text_input_tab", "텍스트 입력"),
    ("slider_input_tab", "슬라이더 입력"),
    ("test_input_tab", "테스트 입력"),
]


def start_gradio():
    server_name = GRADIO_HOST
    server_port = GRADIO_PORT


    with gr.Blocks() as demo:
        with gr.Tabs():
            for module_name, label in TAB_INFOS:
                module = importlib.import_module(f"gradio_app.tabs.{module_name}")
                with gr.TabItem(label):
                    module.create_tab()
    demo.launch(server_name=server_name, server_port=server_port)

if __name__ == "__main__":
    start_gradio()