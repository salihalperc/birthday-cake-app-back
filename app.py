from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS

app = Flask(__name__)
SECRET_PASSWORD = os.getenv("SECRET_PASSWORD")

CORS(app, origins=["https://salihalperc.github.io/birthday-cake-app"])
@app.route('/verify-password', methods=['POST'])
def verify_password():
    data = request.get_json()
    if data.get('password') == SECRET_PASSWORD:
        return jsonify({"success": True})
    return jsonify({"success": False})

@app.route('/get-message', methods=['GET'])
def get_message():
    return jsonify({
        "message": """Bir dilek tut ve muma üfle! 🕯️

Bugün senin özel günün ve sana en güzel dileklerimi sunuyorum. Hayatın hep mutluluk, sevgi ve güzel anılarla dolu olsun. 

Yeni yaşın sana sağlık, başarı ve hayallerini gerçekleştirme fırsatı getirsin. Sen çok özel birisin ve bu dünyayı daha güzel bir yer yapıyorsun.

İyi ki doğdun, iyi ki varsın! 🎂🎉

Sana sevgilerle... 💝"""
    })

# ⛔ app.run() KULLANMA! Gunicorn kullanacağız.
