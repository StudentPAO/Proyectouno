from flask import Flask, render_template
#importamos la libreriaa de Flask
# This is a sample Python script.
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#creamos una ruta a raiz
app = Flask(__name__)
@app.route("/")
#creamos una funcion para mostrar index.html
def index():
    return render_template("index.html")
# Press the green button in the gutter to run the script.
#creamos una condicional para tener un archivo
if __name__ == '__main__':
    app.run(port=3000, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/