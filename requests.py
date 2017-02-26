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

    def todos_create(self):
        errors = []
        if not request.form.get('title'):
            errors.append('Titled is required')
        if not request.form.get('text'):
            errors.append('Text description is required')
        if not request.form.get('done'):
            errors.append("Done field is required")

        if errors:
            return Response(
                json_util.dumps(errors),
                status=422,
                mimetype='application/json'
            )

        else:
            done = True
            if str(request.form.get('done').lower()) == 'false':
                done = False
            if str(request.form.get('done')) == '0':
                done = False
            now = datetime.datetime.utcnow()
            todo_id = self.db.todos.insert_one({
                "title": request.form.get('title'),
                "text": request.form.get('text'),
                "done": done,
                "createdAt": now,
                "updatedAt": now
            }).inserted_id
            return Response(
                json_util.dumps({
                    "title": request.form.get('title'),
                    "text": request.form.get('text'),
                    "done": done,
                    "_id": str(todo_id),
                    "createdAt": str(now),
                    "updatedAt": str(now)
                }),
                status=200,
                mimetype='application/json'
            )