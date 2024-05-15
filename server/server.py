"""
Example server for dependency injection demo. Contents in this file really don't matter.
"""

from flask import Flask
from time import time

app = Flask(__name__)

@app.get('/authenticated')
def data():
    return {
        "authenticated": True if int(time()) % 2 == 0 else False
    }

app.run(debug=True)