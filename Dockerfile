FROM python:3.8.3-slim

WORKDIR /src/app
COPY /webapp .

RUN pip install -r requirements.txt

# ENV FLASK_APP=main.py
ENV FLASK_ENV=development


EXPOSE 5000
CMD ["python", "main.py"]