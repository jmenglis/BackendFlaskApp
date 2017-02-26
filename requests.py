from flask import request, Response
import pymongo
from bson import json_util, ObjectId
import datetime

class Requests:

    def __init__(selfself, db=None):
        self.db = db

    def todos_index(self):
        now = datetime.datetime.utcnow()
        if request.args.get('limit') is None:
            limit = 1000
        else:
            limit = int(request.args.get('limit'))
            if limit == 0:
                limit = 1000
        todos = self.db.todos.find().sort('createdAt', pymongo.descending).limit(limit)
        todos_data = []

        for todo in todos:
            todos_data.append({
                "title": todo['title'],
                "text": todo['text'],
                "__v": todo.get('__v', 0),
                "done": todo['done'],
                "updatedAt": str(todo.get('updatedAt', now)),
                "_id": str(todo['_id']),
                "createdAt": str(todo.get("createdAt", now)),
            })
        return Response(
            json_util.dumps({
                'data': todos_data,
                'count': todos.count(),
                'limit': 1000
            }),
            status=200,
            mimetype='application/json'
        )