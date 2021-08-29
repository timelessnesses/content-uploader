FROM python:3
WORKDIR /app
COPY **
COPY *.*
COPY *.*
RUN pip install -r flask
RUN mkdir stuff
EXPOSE 80
CMD ["python","main.py"]
