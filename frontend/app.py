from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Ruta de inicio
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
