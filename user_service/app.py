from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de usuario (simulados para este ejemplo)
usuarios = {
    'usuario1': {'nombre': 'Usuario 1', 'correo': 'usuario1@example.com', 'contraseña': 'contraseña1'},
    'usuario2': {'nombre': 'Usuario 2', 'correo': 'usuario2@example.com', 'contraseña': 'contraseña2'}
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    if not usuario or not contraseña:
        return jsonify({'error': 'Usuario y contraseña son necesarios para iniciar sesión'}), 400

    if usuario not in usuarios or usuarios[usuario]['contraseña'] != contraseña:
        return jsonify({'error': 'Credenciales inválidas'}), 401

    return jsonify({'mensaje': 'Inicio de sesión exitoso', 'usuario': usuarios[usuario]}), 200

if __name__ == '__main__':
    app.run(debug=True)
