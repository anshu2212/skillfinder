import logging
from dotenv import load_dotenv
from os import environ
from apps import create_app
load_dotenv()

app = create_app()

if __name__ == "__main__":
    PORT=5000
    if "APP_PORT" in environ:
        PORT=environ.get('APP_PORT')
    app.run(host="0.0.0.0", port=PORT,debug=True)