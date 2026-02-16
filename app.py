from flask import Flask

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return "Bienvenido al Sistema de Ventas GRIVOX – Catálogo de accesorios"

# Ruta dinámica adaptada al negocio
@app.route('/producto/<nombre>')
def producto(nombre):
    return f"Producto: {nombre} – disponible en el sistema GRIVOX."

if __name__ == '__main__':
    app.run(debug=True)
