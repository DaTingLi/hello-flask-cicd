ARG PYVER=3.11
FROM python:${PYVER}-slim

# Set working directory
WORKDIR /app

# Allow configuring pip index URL at build time
ARG PIP_INDEX_URL=https://pypi.org/simple

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --timeout 120 -i "${PIP_INDEX_URL}" -r requirements.txt

# Copy application code
COPY app.py .

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=3s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

# Run the application
CMD ["python", "app.py"]
