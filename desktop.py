import threading
import webview
import streamlit.web.cli as stcli
import sys

def run_streamlit():
    sys.argv = [
        "streamlit",
        "run",
        "智能工厂数字孪生平台.py",
        "--server.headless=true",
        "--global.developmentMode=false"
    ]
    stcli.main()

if __name__ == "__main__":
    threading.Thread(target=run_streamlit, daemon=True).start()
    webview.create_window(
        "智能工厂数字孪生平台",
        "http://localhost:8501",
        width=1400,
        height=900
    )
    webview.start()

