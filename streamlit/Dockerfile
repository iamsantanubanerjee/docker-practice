# Streamlit Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.10-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 to the world outside this container
EXPOSE 8501

# Run streamlit app when the container launches
CMD ["streamlit", "run", "app.py", "--server.port=8501"]
