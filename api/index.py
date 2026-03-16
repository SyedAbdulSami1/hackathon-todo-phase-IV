import os
import sys

# Add the project root to sys.path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Now we can import from backend
from backend.index import app

# This file is the entry point for Vercel
# It exposes the FastAPI app from the backend directory
