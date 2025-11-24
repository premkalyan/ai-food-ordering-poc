"""
Vercel serverless function entry point
This file is required for Vercel deployment
"""

import sys
from pathlib import Path

# Add parent directory to path so we can import main
sys.path.append(str(Path(__file__).parent.parent))

from main import app

# Vercel will use this as the entry point
handler = app

