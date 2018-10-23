FROM python:3

WORKDIR /app
ADD requirements.lock .
ADD server.py .
RUN pip install -r requirements.lock

EXPOSE 80
CMD ["/app/server.py"]

