from flask import Flask, jsonify, request
from app import app
from ..models.items import Items
from ..models.images import Images


@app.route('/api/v1/items/add')
def index():
    # As a list to test debug toolbar
    Items.objects().delete()  # Removes
    Items(title="Simple todo A ПЫЩЬ!", url='http://www.google.com', price=150, status=1, isBackdoor=False).save()
    items = Items.objects.all()
    return jsonify({'items': items})


@app.route('/api/v1/items/<int:id>', methods=['GET'])
def get_item(id):
    task = [task for task in tasks if task['id'] == id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/api/v1/items', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
