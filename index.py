from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')

@app.route('/html')
def html():
    return render_template('html.html')

@app.route('/css')
def css():
    return render_template('css.html')

@app.route('/python')
def python():
    return render_template('python.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')



@app.route('/submit', methods=['POST'])
def submit():
    # Obtener los datos del formulario
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    mensaje = request.form.get('mensaje')
    
    # Renderizar una nueva página HTML con la información recibida
    return render_template('mensaje.html', nombre=nombre, email=email, mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)