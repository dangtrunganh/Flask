# -*- coding: UTF-8 -*-

from flask_api import FlaskAPI

app = FlaskAPI(__name__)


@app.route('/')
def run_demo_api():
    return {
        "message": "Hi, I am VTA."
    }


if __name__ == '__main__':
    app.run()
