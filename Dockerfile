# Aden Hive - Multi-Container Docker Setup

# --- STAGE 1: Frontend Build ---
FROM node:20-slim AS frontend-builder
WORKDIR /app/core/frontend
COPY core/frontend/package*.json ./
RUN npm install
COPY core/frontend/ ./
RUN npm run build

# --- STAGE 2: Backend & Tools Setup ---
FROM python:3.11-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    ripgrep \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome (stable) for browser-use tools
RUN mkdir -p /etc/apt/keyrings \
    && wget -q -O /etc/apt/keyrings/google-chrome.asc https://dl.google.com/linux/linux_signing_key.pub \
    && echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.asc] http://dl.google.com/linux/chrome/deb/ stable main" \
       > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install UV for faster Python package management
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

# Copy the entire workspace (honoring .dockerignore)
COPY . .

# Build the Python environment using UV
RUN uv sync --frozen

# Copy the built frontend from Stage 1
COPY --from=frontend-builder /app/core/frontend/dist ./core/frontend/dist

# Expose ports: 8000 (Backend), 4001 (Tools), 3000 (Frontend serve)
EXPOSE 8000 4001 3000

# Default environment variables
ENV HIVE_HOME=/root/.hive
ENV PYTHONPATH=/app/core:/app/tools/src

# Entrypoint will be handled by Docker Compose
