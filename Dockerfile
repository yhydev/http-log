FROM python:3.9-slim
RUN mkdir /app 
COPY main.py /app
COPY requirement.txt /app
WORKDIR /app
RUN pip install -r requirement.txt
EXPOSE 8000
CMD ["gunicorn","main:app", "-b", "0.0.0.0:8000"]
