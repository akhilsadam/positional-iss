"""Application entry point."""
from app import init_app

app = init_app()
port = 5026

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False,port=port)