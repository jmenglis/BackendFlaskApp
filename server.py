from flask import Flask, render_template
from pymongo import MongoClient

from config import *

app = Flask(__name__, static_folder=ASSETS_FOLDER, template_folder=TEMPLATE_FOLDER)
app.config.from_object('config')


def mongo_connect():
    connection = MongoClient('mongodb://%s:%s' % (MONGO_HOST, MONGO_PORT))
    db = connection[MONGO_DBNAME]
    return db

db = mongo_connect()

if __name__ == '__main__':
    app.run(port=9000, debug=True)

