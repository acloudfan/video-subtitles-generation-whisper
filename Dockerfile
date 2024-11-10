FROM ubuntu

RUN apt update && apt install ffmpeg -y && apt install python3 -y && apt install python3-pip -y

RUN pip install -U openai-whisper  --break-system-packages


RUN pip install setuptools-rust --break-system-packages

COPY generate.py  /opt/generate.py

ENTRYPOINT  ["python3", "/opt/generate.py", "/home/videos"]






