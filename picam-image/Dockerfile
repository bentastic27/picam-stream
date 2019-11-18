FROM balenalib/rpi-python:3.7-latest
RUN pip install picamera
COPY cam.py /cam.py
EXPOSE 8000
CMD ["python3", "/cam.py"]
