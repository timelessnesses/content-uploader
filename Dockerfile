FROM python:3
WORKDIR /app
COPY **
COPY *.*
COPY *.*
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python","main.py"]
