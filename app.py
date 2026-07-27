from flask import Flask, render_template, request, redirect, url_for, flash, session

import sqlite3

app = Flask(__name__)

app.secret_key = "aether_super_secret_key"

@app.route("/")
def home():
    return render_template("home.html", active_page="home")

@app.route("/lets-connect")
def lets_connect():
    return render_template("lets_connect.html")

@app.route("/projects/aether-studio")
def aether_project():
    return render_template("aether_project.html")

@app.route("/projects/notes-app")
def notes_project():
    return render_template("notes_project.html")

@app.route("/contact", methods=["POST"])
def contact():

    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    connection = sqlite3.connect("aether.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO messages(name, email, message)
        VALUES(?, ?, ?)
        """,
        (name, email, message)
    )

    connection.commit()

    connection.close()

    flash("✅ Thanks! Your message has been received.")

    return redirect(url_for("home"))

@app.route("/messages")
def messages():
    
    if not session.get("logged_in"):

        return redirect(url_for("login"))

    connection = sqlite3.connect("aether.db")

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM messages")

    messages = cursor.fetchall()

    connection.close()

    return render_template("messages.html", messages=messages, active_page="messages")

@app.route("/delete/<int:id>")
def delete(id):

    connection = sqlite3.connect("aether.db")

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM messages WHERE id=?",
        (id,)
    )

    connection.commit()

    connection.close()

    return redirect("/messages")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        
        password = request.form["password"]

        if password == "aether123":

            session["logged_in"] = True

            return redirect(url_for("messages"))
        
        else:

            flash("Wrong Password!")

            return redirect(url_for("login"))
        
    return render_template("login.html", active_page="login")

@app.route("/logout")
def logout():

    session.pop("logged_in", None)

    return redirect("/")

@app.errorhandler(404)
def page_not_found(error):

    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)