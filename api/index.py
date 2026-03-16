import os
import sys

# Get the absolute path of the current directory (api/)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the project root directory
root_dir = os.path.dirname(current_dir)

# Add the project root to sys.path so we can import 'backend'
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Add the backend directory to sys.path so internal imports in backend work
backend_dir = os.path.join(root_dir, 'backend')
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Now we can import the FastAPI app
try:
    from backend.index import app
except ImportError as e:
    print(f"Import error: {e}")
    # Fallback if Vercel changes the structure
    sys.path.append(os.path.join(root_dir, 'backend'))
    from index import app

# This exposes the FastAPI app to Vercel
