FROM python

COPY requirements.txt /pipeline/
COPY src /pipeline/

WORKDIR /pipeline
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
