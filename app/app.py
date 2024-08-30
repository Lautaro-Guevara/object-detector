from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para manejar la carga de imágenes
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        # Aquí puedes guardar el archivo y procesarlo
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        # Procesar la imagen con el modelo de detección
        # ...
        return redirect(url_for('result', filename=file.filename))

# Ruta para mostrar los resultados
@app.route('/result/<filename>')
def result(filename):
    # Aquí puedes cargar la imagen procesada y mostrarla
    return render_template('result.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
