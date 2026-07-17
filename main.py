import os
import subprocess
import sys

def resource_path(relative_path):
    """ تابع برای تعیین مسیر صحیح فایل‌های داخلی در حالت EXE """
    try:
        base_path = sys._MEIPASS  # مسیر موقت PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    # تنظیم مسیر فایل‌های ضروری
    os.environ["STREAMLIT_SERVER_PORT"] = "8501"
    streamlit_path = resource_path("app.py")
    subprocess.run(["streamlit", "run", "app.py", "--server.port=8502"])

if __name__ == "__main__":
    main()