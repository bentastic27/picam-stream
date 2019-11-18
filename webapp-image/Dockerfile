FROM python:3.8
WORKDIR /srv
RUN pip install --no-cache-dir flask kubernetes gunicorn 
COPY . /srv/
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]