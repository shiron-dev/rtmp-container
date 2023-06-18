FROM python:3

RUN apt-get update
RUN apt-get install ffmpeg -y
RUN pip install --upgrade pip
RUN pip install opencv-python ffmpeg-python
COPY main.py main.py

CMD ["python", "main.py"]
