#!/bin/bash

# Start ollama in the background
ollama serve &

# Wait for ollama to be ready
until ollama list >/dev/null 2>&1; do
    echo "Waiting for Ollama to start..."
    sleep 1
done

# Check if qwen2.5:1.5b model exists, if not pull it with retries
if ! ollama list | grep -q "qwen2.5:1.5b"; then
    echo "Pulling qwen2.5:1.5b model..."
    MAX_RETRIES=200
    RETRY_COUNT=0

    while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
        echo "Attempt $((RETRY_COUNT + 1)) of $MAX_RETRIES..."

        if ollama pull qwen2.5:1.5b; then
            echo "Model pulled successfully!"
            break
        else
            RETRY_COUNT=$((RETRY_COUNT + 1))
            if [ $RETRY_COUNT -lt $MAX_RETRIES ]; then
                echo "Pull failed, retrying in 10 seconds..."
                sleep 10
            else
                echo "Failed to pull model after $MAX_RETRIES attempts"
                echo "You can manually pull it later with: docker exec ollama ollama pull qwen2.5:1.5b"
            fi
        fi
    done
else
    echo "qwen2.5:1.5b model already exists"
fi

wait
