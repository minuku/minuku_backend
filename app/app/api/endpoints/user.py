from flask import jsonify

from ...main import app
from ...core.database import users


@app.route('/users/')
def route_users():
    users_data = []
    for user in users:
        user_data = {
            'name': user.name,
            'email': user.email,
        }
        users_data.append(user_data)
    return jsonify(users_data)
