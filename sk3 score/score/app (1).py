from cs50 import SQL
# import tools utk website
from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)

db = SQL("sqlite:///score.db")

@app.route('/', methods=["GET", "POST"]) #root route
def index(): #function index
    if request.method == "POST":
        name = request.form.get("name")
        score = request.form.get("score")
        db.execute("INSERT INTO score (name, score) values(?,?)", name, score)
        return redirect("/")
    else:
        students = db.execute("select * from score")
        return render_template("index.html", students=students)
@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_data(id):
    if request.method == "GET":
        students = db.execute("SELECT * FROM score WHERE id = ?", id)[0]
        print(students)
        return render_template("edit.html", students=students)
    else:
        students_name = request.form.get("name")
        students_score = request.form.get("score")
        db.execute('UPDATE Score set name = ?, score = ? where id = ?', students_name, students_score, id)
        return redirect("/")
    
@app.route("/delete/<id>", methods=["GET"])
def delete(id):
    db.execute("delete from score where id = ?",id)
    return redirect("/")
