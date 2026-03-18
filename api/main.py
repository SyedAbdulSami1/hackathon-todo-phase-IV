import os
import sys

# Add project root to path
# __file__ is /var/task/api/main.py on Vercel
api_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(api_dir)

if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Add backend to path
backend_dir = os.path.join(root_dir, 'backend')
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Now import the app
try:
    from backend.index import app
except ImportError as e:
    print(f"IMPORT ERROR: {e}")
    # Fallback to try relative import if needed
    try:
        from ..backend.index import app
    except:
        raise e

# Vercel's Python builder looks for 'app' by default
# but we can explicitly expose it here
app = app
