#!/usr/bin/python3
#!/usr/bin/python3
"""Package handler"""
from models.engine.file_storage import FileStorage

try:
    storage = FileStorage()
    storage.reload()
except Exception as e:
    print(f"An error occurred during initialization or reloading: {e}")
