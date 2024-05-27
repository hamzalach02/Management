from flask import Flask, render_template, request

app = Flask(__name__)

app.jinja_env.globals.update(enumerate=enumerate)  # Ajout de enumerate pour Jinja2

questions = [
    "Je suis conscient(e) de mes émotions quand elles surviennent.",
    "Je sais gérer mes émotions dans des situations stressantes.",
    "Je comprends pourquoi je ressens certaines émotions dans des situations spécifiques.",
    "Je peux facilement identifier les émotions des autres à partir de leurs expressions faciales.",
    "Je suis capable de réguler mes émotions pour rester calme dans des situations difficiles.",
    "Je suis empathique envers les autres et je comprends leurs sentiments.",
    "Je suis capable de motiver moi-même pour atteindre mes objectifs malgré les obstacles.",
    "Je m'efforce de développer et de maintenir des relations positives avec les autres.",
    "Je peux adapter mon comportement en fonction des émotions des autres.",
    "Je reconnais mes propres forces et faiblesses émotionnelles.",
    "Je suis conscient(e) de l'impact de mes émotions sur les autres.",
    "Je fais des efforts pour améliorer ma compréhension de moi-même.",
    "Je reste calme sous pression.",
    "Je peux gérer plusieurs priorités sans me sentir débordé(e).",
    "J'écoute attentivement les autres quand ils partagent leurs émotions.",
    "Je ressens de la satisfaction lorsque j'aide les autres à résoudre leurs problèmes émotionnels.",
    "Je suis persévérant(e) même face à des échecs.",
    "Je cherche à comprendre les perspectives émotionnelles des autres.",
    "Je résous les conflits de manière constructive.",
    "Je sais quand demander de l'aide pour mieux gérer mes émotions."
]

categories = {
    "Conscience de soi": [0, 2, 9, 10, 11],
    "Maîtrise de soi": [1, 4, 12, 13, 19],
    "Conscience sociale": [3, 5, 14, 15, 17],
    "Gestion des relations": [6, 7, 8, 16, 18]
}

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
    scores = [int(request.form[f'q{i}']) for i in range(len(questions))]
    results = {}
    for category, indices in categories.items():
        results[category] = sum(scores[i] for i in indices) / len(indices)
    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
