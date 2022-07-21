from flask import render_template, session, redirect, url_for, flash
from app.forms import LoginForm

from . import auth

@auth.route("/login", methods= ['GET' ,'POST' ])
def login():
    login_form= LoginForm()
    context = {
        "login_form" : LoginForm()
    }
    # se encarga de validar la forma enviada, para redireccionar a otra pagina
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        
        flash("Nombre de usuario registrado con exito!")

        return redirect( url_for("index"))
        # return redirect("https://platzi.com")

    return render_template("login.html", **context)