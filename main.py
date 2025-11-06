from flask import Flask, render_template, request, jsonify
import os
from chatbot import ChatbotCamiloTorres

app = Flask(__name__)

# Configuración general
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'camilo-torres-secret-key-2025')

bot = ChatbotCamiloTorres()

# ==========================
# 🔷 RUTAS PRINCIPALES
# ==========================
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

@app.route('/tec')
def tec():
    return render_template('tec.html', titulo="Tecnología - IE Camilo Torres")

@app.route('/feria')
def feria():
    return render_template('feria.html', titulo="Feria Educativa - IE Camilo Torres")

# ==========================
# 🧠 SMART-EDU
# ==========================
@app.route('/smartedu')
def smartedu():
    return render_template('smartedu.html', titulo="SMART-EDU - IE Camilo Torres")

# Materias SmartEdu
@app.route('/smartedu/matematicas')
def smartedu_matematicas():
    return render_template('matematicas.html', titulo="Matemáticas - SmartEdu")

@app.route('/smartedu/espanol')
def smartedu_espanol():
    return render_template('espanol.html', titulo="Español - SmartEdu")

@app.route('/smartedu/ingles')
def smartedu_ingles():
    return render_template('ingles.html', titulo="Inglés - SmartEdu")

@app.route('/smartedu/sociales')
def smartedu_sociales():
    return render_template('sociales.html', titulo="Ciencias Sociales - SmartEdu")

@app.route('/smartedu/naturales')
def smartedu_naturales():
    return render_template('naturales.html', titulo="Ciencias Naturales - SmartEdu")

@app.route('/smartedu/quimica')
def smartedu_quimica():
    return render_template('quimica.html', titulo="Química - SmartEdu")

@app.route('/smartedu/biologia')
def smartedu_biologia():
    return render_template('biologia.html', titulo="Biología - SmartEdu")

@app.route('/smartedu/fisica')
def smartedu_fisica():
    return render_template('fisica.html', titulo="Física - SmartEdu")

@app.route('/smartedu/filosofia')
def smartedu_filosofia():
    return render_template('filosofia.html', titulo="Filosofía - SmartEdu")

@app.route('/smartedu/etica')
def smartedu_etica():
    return render_template('etica.html', titulo="Ética - SmartEdu")

@app.route('/smartedu/religion')
def smartedu_religion():
    return render_template('religion.html', titulo="Religión - SmartEdu")

@app.route('/smartedu/tecnologia')
def smartedu_tecnologia():
    return render_template('tecnologia.html', titulo="Tecnología - SmartEdu")

@app.route('/smartedu/educacion_fisica')
def smartedu_educacion_fisica():
    return render_template('educacion_fisica.html', titulo="Educación Física - SmartEdu")

@app.route('/smartedu/artistica')
def smartedu_artistica():
    return render_template('artistica.html', titulo="Educación Artística - SmartEdu")

@app.route('/smartedu/herramientas')
def smartedu_herramientas():
    return render_template('herramientas.html', titulo="Herramientas de IA - SmartEdu")

# ==========================
# 🤖 CHATBOT
# ==========================
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

# ==========================
# ⚙️ OTROS
# ==========================
@app.route("/festival-gastronomico")
def festival():
    return render_template("festival.html", titulo="Festival Gastronómico - IE Camilo Torres")

@app.route("/ping")
def ping():
    return "pong", 200

# ==========================
# 🚀 EJECUCIÓN
# ==========================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
   
   
