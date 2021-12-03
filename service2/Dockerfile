FROM python:3.6
WORKDIR /service2
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5001
ENTRYPOINT ["python3", "genre.py"]