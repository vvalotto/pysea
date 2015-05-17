from flask import Flask, render_template, flash, redirect, url_for
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = "Victor"
bootstrap = Bootstrap(app)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def inicio():
    return render_template('/general/inicio.html')


@app.route('/acerca/')
def acerca():
    return render_template('general/acerca.html')


@app.route('/versiones/')
def versiones():
    return


@app.route('/componentes/')
def componentes():
    return

@app.route("/adquisicion/", methods=['GET', 'POST'])
def adquisicion():
    pass

@app.route("/procesamiento/")
def procesamiento():
    return


@app.route("/visualizacion/")
def visualizacion():
    return