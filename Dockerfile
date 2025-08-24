# # Use the official Python base image
# FROM python:3.12

# # Set working directory inside the container
# WORKDIR /app

# # Copy requirements first to leverage Docker cache
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application
# COPY . .

# # Set Streamlit port and run the app
# EXPOSE 8501
# CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.baseUrlPath=/space-truss"]







FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Streamlit behind reverse proxy
ENV STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_ENABLECORS=false \
    STREAMLIT_SERVER_ENABLEXSRSFPROTECTION=false \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

EXPOSE 8501
CMD ["streamlit","run","app.py","--server.port=8501","--server.address=0.0.0.0"]
