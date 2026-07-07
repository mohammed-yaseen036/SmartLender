FROM python:3.10-slim

WORKDIR /code

# Copy requirements and install dependencies
COPY "5.Project Development Phase/requirements.txt" /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . /code

# Grant all permissions so Hugging Face user can execute successfully
RUN chmod -R 777 /code

# Expose Hugging Face default port
EXPOSE 7860

# Run Flask application
CMD ["python", "5.Project Development Phase/app.py"]
