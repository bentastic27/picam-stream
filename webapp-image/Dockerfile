FROM python:3.8
RUN pip install --no-cache-dir flask kubernetes
COPY . /srv/
CMD ["python", "/srv/app.py"]