FROM python:3.12-slim

WORKDIR /app

# Copy requirements and packages first for better caching
COPY ./requirements.txt /app/requirements.txt
COPY ./packages.txt /app/packages.txt

# Install system packages including espeak-ng for TTS
RUN apt-get update && \
    apt-get -qq -y install espeak-ng > /dev/null 2>&1 && \
    xargs -r -a /app/packages.txt apt-get install -y && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r /app/requirements.txt

# Create user
RUN useradd -m -u 1000 user
USER user
ENV HOME /home/user
ENV PATH $HOME/.local/bin:$PATH

# Setup app directory
WORKDIR $HOME
RUN mkdir app
WORKDIR $HOME/app

# Copy application files
COPY --chown=user . $HOME/app

EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run Streamlit
CMD streamlit run app.py \
    --server.headless true \
    --server.address 0.0.0.0 \
    --server.port 8501 \
    --server.enableCORS false \
    --server.enableXsrfProtection false \
    --server.fileWatcherType none
