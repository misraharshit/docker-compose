FROM python:3.9
RUN pip install psutil
COPY scrape.py /app/scrape.py
WORKDIR /app
CMD ["python3", "scrape.py"]
