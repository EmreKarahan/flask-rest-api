from flask import Flask, jsonify, render_template
from app import app
from ..models.items import Items
from ..models.images import Images



@app.route('/')
def index():
    # As a list to test debug toolbar
    Items.objects().delete()  # Removes
    Items(title="Simple todo A ПЫЩЬ!", url= 'http://www.google.com', price=150, status=1, is_backdoor=False).save()  # Insert
    items = Items.objects.all()
    return jsonify({'items': items})


@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
