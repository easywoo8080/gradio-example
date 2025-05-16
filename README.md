# gradio-example
gradio 연습용 사이트  


# 최초 pip
```bash
Package Version
------- -------
pip     25.0.1
```


# 설치 pip
```bash

# 2025-05-15 문지우 : 초기 fastAPI, gradio, uvicorn 설치
pip install fastapi gradio uvicorn
pip install gradio_client
pip install python-dotenv


# Gradio 자동실행을 위한 
pip install watchdog

```

# 실행방법
```bash
# fastAPI server on
uvicorn fastapi_app.run_fastapi:app --host 0.0.0.0 --port 8000 --reload
# gradio server on

python -m gradio_app.run_gradio
```
