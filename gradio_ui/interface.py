import gradio as gr
from fastAPI.core import logic

gr_interface = gr.Interface(fn=logic.greet, inputs="text", outputs="text")
gradio_app = gr_interface.app  # <- FastAPI에서 mount할 대상
