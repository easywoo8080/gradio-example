import multiprocessing
import uvicorn
import time
import os
from gradio_app.run_gradio import start_gradio
from config.config import FASTAPI_HOST, FASTAPI_PORT  # Config에서 가져오기



def run_fastapi():
    uvicorn.run("fastapi_app.run_fastapi:app", host=FASTAPI_HOST, port=FASTAPI_PORT, reload=True)

def run_gradio():
    start_gradio()

if __name__ == "__main__":
    fastapi_proc = multiprocessing.Process(target=run_fastapi)
    gradio_proc = multiprocessing.Process(target=run_gradio)

    fastapi_proc.start()
    gradio_proc.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("서버 종료 중...")
        fastapi_proc.terminate()
        gradio_proc.terminate()
        fastapi_proc.join()
        gradio_proc.join()
        print("서버가 종료되었습니다.")
