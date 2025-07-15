
import random
import re
from datetime import datetime
import html

class ChatbotCamiloTorres:
    def __init__(self):
        self.responses = {
            'saludo': [
                "¡Hola! Soy el asistente virtual de la IE Camilo Torres. ¿En qué puedo ayudarte?",
                "¡Bienvenido/a! Estoy aquí para ayudarte con información sobre nuestra institución.",
                "¡Hola! ¿Cómo puedo asistirte hoy con información de la IE Camilo Torres?"
            ],
            'horarios': [
                "Nuestros horarios de atención son de lunes a viernes de 7:00 AM a 4:00 PM.",
                "La institución funciona en jornada única de 7:00 AM a 4:00 PM, de lunes a viernes.",
                "Puedes visitarnos de lunes a viernes entre las 7:00 AM y las 4:00 PM."
            ],
            'icfes': [
                "Ofrecemos preparación especializada para las pruebas ICFES. Puedes acceder a nuestros recursos en la sección 'Preparación ICFES'.",
                "Tenemos simulacros, guías de estudio y material especializado para el ICFES. Consulta nuestra página de preparación.",
                "La preparación para el ICFES es una de nuestras fortalezas. Revisa todos nuestros recursos disponibles en línea."
            ],
            'mision': [
                "Nuestra misión es formar integralmente a los estudiantes con valores éticos y académicos sólidos.",
                "Nos dedicamos a la formación integral de personas competentes y comprometidas con su comunidad.",
                "Trabajamos por la excelencia académica y la formación en valores de nuestros estudiantes."
            ],
            'contacto': [
                "Puedes contactarnos a través de nuestras redes sociales: Facebook, Instagram y TikTok.",
                "Síguenos en nuestras redes sociales para estar al día con nuestras actividades y noticias.",
                "Para contacto directo, puedes visitarnos en la institución o seguirnos en redes sociales."
            ],
            'matriculas': [
                "Para información sobre matrículas, por favor acércate a la institución en horario de atención.",
                "El proceso de matrícula se realiza presencialmente. Te esperamos de lunes a viernes de 7:00 AM a 4:00 PM.",
                "Para matricular a tu hijo/a, debes venir con la documentación requerida en horario de atención."
            ],
            'despedida': [
                "¡Gracias por contactarnos! Que tengas un excelente día.",
                "¡Hasta pronto! Recuerda que estamos aquí para ayudarte.",
                "¡Nos vemos! No dudes en contactarnos si necesitas más información."
            ],
            'default': [
                "Interesante pregunta. Te recomiendo visitar nuestra página web para más información específica.",
                "No tengo información específica sobre eso, pero puedes contactar directamente a la institución.",
                "Para información más detallada, te sugiero acercarte a la institución o revisar nuestras redes sociales."
            ]
        }
        
        self.patterns = {
            'saludo': r'\b(hola|buenos días|buenas tardes|buenas noches|saludos|hey|hi)\b',
            'horarios': r'\b(horarios?|horario|atención|funciona|abierto|cerrado|cuando)\b',
            'icfes': r'\b(icfes|examen|prueba|simulacro|puntaje|saber 11|preparación)\b',
            'mision': r'\b(misión|vision|valores|objetivo|propósito|filosofía)\b',
            'contacto': r'\b(contacto|teléfono|correo|email|redes|facebook|instagram|tiktok)\b',
            'matriculas': r'\b(matrícula|matricular|inscribir|inscripción|admisión|ingreso)\b',
            'despedida': r'\b(adiós|chao|bye|hasta luego|gracias|nos vemos)\b'
        }
    
    def analyze_message(self, message):
        message = message.lower()
        
        for category, pattern in self.patterns.items():
            if re.search(pattern, message, re.IGNORECASE):
                return category
        
        return 'default'
    
    def get_response(self, user_message):
        # Sanitizar entrada del usuario
        user_message = html.escape(user_message.strip())
        
        # Validar longitud
        if len(user_message) > 500:
            return {
                'message': 'El mensaje es demasiado largo. Por favor, escribe algo más corto.',
                'timestamp': datetime.now().strftime("%H:%M"),
                'category': 'error'
            }
        
        category = self.analyze_message(user_message)
        response = random.choice(self.responses[category])
        
        # Agregar timestamp
        timestamp = datetime.now().strftime("%H:%M")
        
        return {
            'message': response,
            'timestamp': timestamp,
            'category': category
        }

# Función para usar el chatbot
def chat_with_bot():
    bot = ChatbotCamiloTorres()
    
    print("🤖 Chatbot IE Camilo Torres")
    print("=" * 40)
    print("Escribe 'salir' para terminar la conversación")
    print()
    
    while True:
        user_input = input("Tú: ")
        
        if user_input.lower() in ['salir', 'exit', 'quit']:
            print("🤖 Bot: ¡Hasta pronto! Gracias por contactar a la IE Camilo Torres.")
            break
        
        if user_input.strip() == '':
            continue
            
        response = bot.get_response(user_input)
        print(f"🤖 Bot [{response['timestamp']}]: {response['message']}")
        print()

# Para usar el chatbot desde la línea de comandos
if __name__ == "__main__":
    chat_with_bot()
