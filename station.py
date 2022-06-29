from app import app
from time import sleep



if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)