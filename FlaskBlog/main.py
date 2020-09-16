from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/showDatiSensore')
def showDatiSensore():
    return render_template('dati_sensore.html')


if __name__ == "__main__":
    app.run(debug=True)