from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    from random import randint

    intentos = 0
    estimado = 0
    numero_secreto = 25  # Set the winning number to 25
    nombre = "Usuario"
    message = ""  # Initialize message
    alert_type = ""  # Initialize alert_type

    if request.method == 'POST':
        estimado = int(request.form['guess'])
        intentos += 1

        if estimado < numero_secreto:
            message = "My number is higher."
        elif estimado > numero_secreto:
            message = "My number is lower."
        else:
            message = f"Congratulations, {nombre}! You guessed the number in {intentos} attempts."
            alert_type = "success"

    return render_template('index.html', nombre=nombre, intentos=intentos, estimado=estimado,
                           numero_secreto=numero_secreto, message=message, alert_type=alert_type)

if __name__ == '__main__':
    app.run(debug=False)




