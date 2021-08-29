FROM python:3
WORKDIR /app
COPY *.* .
RUN pip install flask
RUN mkdir stuff
EXPOSE 80
CMD ["python","main.py"]
