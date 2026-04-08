FROM python:3.10

WORKDIR /app

# Copy only requirements first (faster builds)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of files
COPY . .

# Run your baseline agent
CMD ["python", "baseline.py"]