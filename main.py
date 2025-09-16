from flask import Flask, render_template, request, jsonify
import os
from chatbot import ChatbotCamiloTorres

app = Flask(__name__)

# Configuración simple
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'camilo-torres-secret-key-2025')

bot = ChatbotCamiloTorres()

# Rutas principales
@app.route('/')
def index():
    return render_template('index.html', titulo="Inicio - IE Camilo Torres")

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html', titulo="Quiénes Somos - IE Camilo Torres")

@app.route('/simbolos_institucionales')
def simbolos_institucionales():
    return render_template('simbolos_institucionales.html', titulo="Símbolos Institucionales - IE Camilo Torres")

@app.route('/imagenes')
def imagenes():
    return render_template('imagenes.html', titulo="Galería de Imágenes - IE Camilo Torres")

@app.route('/icfes')
def icfes():
    return render_template('icfes.html', titulo="Preparación ICFES - IE Camilo Torres")

@app.route('/anexos')
def anexos():
    return render_template('anexos.html', titulo="Anexos - IE Camilo Torres")

@app.route("/tec")
def tec():
    return render_template("tec.html")

@app.route('/feria')
def feria():
    return render_template('feria.html', titulo="Feria Educativa")


@app.route('/smartedu')
def smartedu():
    return render_template("smartedu.html", titulo="SMART-EDU - IE Camilo Torres")
    
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html', titulo="Chatbot - IE Camilo Torres")

@app.route('/chat', methods=['POST'])
def chat():
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400

    user_message = data.get('message', '').strip()
    if not user_message or len(user_message) > 500:
        return jsonify({'error': 'Invalid message length'}), 400

    response = bot.get_response(user_message)
    return jsonify(response)

@app.route("/ping")
def ping():
    return "pong", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
