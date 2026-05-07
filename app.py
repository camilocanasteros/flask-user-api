from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

# Obtener usuarios
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Crear usuario
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data.get('name') or not data.get('email'):
        return jsonify({'error': 'Name and email are required'}), 400

    user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email']
    }

    users.append(user)

    return jsonify(user), 201

# Actualizar usuario
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    for user in users:
        if user['id'] == user_id:
            data = request.get_json()

            user['name'] = data.get('name', user['name'])
            user['email'] = data.get('email', user['email'])

            return jsonify(user)

    return jsonify({'error': 'User not found'}), 404

# Eliminar usuario
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({'message': 'User deleted'})

    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)