"""Application entry point."""

from app import init_app
from app.options import *

if __name__ == "__main__":
    app = init_app()
    app.run(host=host, debug=False,port=port)