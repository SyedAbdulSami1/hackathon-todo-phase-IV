import os
import sys

# Add the project root to sys.path so we can import 'backend'
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
    # Fallback for different Vercel structure
    try:
        from index import app
    except ImportError:
        raise e

# This exposes the FastAPI app to Vercel
