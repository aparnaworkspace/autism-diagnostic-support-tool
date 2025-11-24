#!/bin/bash

# Navigate to project root
cd "$(dirname "$0")"

# Activate virtual environment
source venv/bin/activate

# Start Jupyter Lab in background
echo "Starting Jupyter Lab..."
jupyter lab > jupyter.log 2>&1 &

# Give Jupyter a moment to boot
sleep 2

# Start Streamlit app in background
echo "Starting Streamlit App..."
streamlit run app/streamlit_app.py > streamlit.log 2>&1 &

echo "----------------------------------------"
echo "✔ Jupyter Lab running at  http://localhost:8888"
echo "✔ Streamlit App running at http://localhost:8501"
echo ""
echo "You can now open both tabs in your browser."
echo "----------------------------------------"
