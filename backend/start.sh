#!/bin/sh

# Run Alembic upgrade to head
echo "Running Alembic upgrade..."
alembic upgrade head

# Start Uvicorn server
echo "Starting Uvicorn server..."
uvicorn src.main:app --host 0.0.0.0 --port 80
