FROM python:3.9-slim

WORKDIR /app

COPY . .
# Install dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# Copy the rest of the application

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]