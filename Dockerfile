FROM python:3
ENV BUILDKIT_PROGRESS=plain
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set working directory
RUN mkdir /code
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project files
COPY . /code/

# Expose port 8000 (adjust if using a different port)
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "your_project_name.wsgi:application", "--bind", "0.0.0.0:8000"]
