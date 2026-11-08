from flask import Flask, render_template
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

app = Flask(__name__)

# Використовуємо імена файлів, які лежать у папці static/images/
MINIONS_DATA = [
    {
        "name": "Кевін (Kevin)",
        "eyes": 2,
        "trait": "Високий, лідер компанії, носить пасма волосся у вигляді паростка.",
        "image": "images/kevin.jpg"
    },
    {
        "name": "Боб (Bob)",
        "eyes": 2,
        "trait": "Короткий, пухкий, з різнокольоровими очима (гетерохромія) та іграшковим ведмедиком.",
        "image": "images/bob.jpg"
    },
    {
        "name": "Стюарт (Stuart)",
        "eyes": 1,
        "trait": "Одноокий, грайливий, любить грати на гітарі.",
        "image": "images/stuart.jpg"
    }
]

@app.route('/')
def home():
    return render_template('index.html', minions=MINIONS_DATA)

if __name__ == '__main__':
    app.run(debug=True)