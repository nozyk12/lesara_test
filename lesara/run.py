import sys
import os

sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from lesara import app

app.run('0.0.0.0', 8000, debug=True)
