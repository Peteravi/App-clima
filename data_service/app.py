from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

OPENWEATHERMAP_API_KEY = '984962d60092807e17bb446f5c6dc080'

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'Se requiere el parámetro "city".'}), 400
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'No se pudieron obtener los datos del clima.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
