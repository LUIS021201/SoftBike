from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for, abort

app = Flask(__name__)
app.secret_key = 'lwiu74dhn2SuF3j'
app.debug = True




@app.route('/')
def index():

    return render_template('index.html')


@app.route('/iniciar-sesion')
def iniciar_sesion():

    return render_template('iniciar-sesion.html')


@app.route('/confirmar-renta')
def confirmar_renta():

    return render_template('checkout-renta.html')

@app.route('/escoger-bicicleta')
def escoger_bici():

    return render_template('escoger-bici.html')

if __name__ == '__main__':
    app.run(debug=True)
