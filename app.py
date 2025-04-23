from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagina1')
def pagina1():
    productos = ['Memoria SD', 'Acesorios', 'Funda de Protecion']
    return render_template('pagina1.html', productos=productos)

@app.route('/pagina2')
def pagina2():
    tabla = [
        {'nombre': 'Ana', 'edad': 21, 'usuario':'Ana657'},
        {'nombre': 'Luis', 'edad': 25, 'usuario': 'Sanchez69'}
    ]
    return render_template('pagina2.html', tabla=tabla)

if __name__ == '__main__':
    app.run(debug=True)
