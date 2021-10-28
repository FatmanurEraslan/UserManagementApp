from application import app
from flask import render_template, flash, request, redirect
from .forms import UserForm
from application import db
from  bson import ObjectId

@app.route("/")
def get_users():
    users = []
    for user in db.user_flask.find():
         user["_id"] = str(user["_id"])
         users.append(user)
    return render_template("view.html",title = " User Management App ", users = users)


@app.route("/add_user", methods=["POST","GET"])
def add_user():
    if request.method == "POST":
        form = UserForm(request.form)
        user_name = form.name.data
        user_email = form.email.data
        user_department = form.department.data
        user_phone = form.phone.data
        db.user_flask.insert_one({
            "name": user_name,
            "email": user_email,
            "department": user_department,
            "phone": user_phone,
            

        })
        flash("User Succesfully added", "succes")
        return redirect("/")
    else:
         form = UserForm()
    return render_template("add_user.html",title='Add User', form = form)


 
@app.route("/update_user/<id>", methods=["POST","GET"])
def update_user(id):
    if request.method == "POST":
        form = UserForm(request.form)
        user_name = form.name.data
        user_email = form.email.data
        user_department = form.department.data
        user_phone = form.phone.data
        db.user_flask.find_one_and_update({"_id": ObjectId(id)}, {"$set":{
            "name": user_name,
            "email": user_email,
            "department": user_department,
            "phone": user_phone,
          
          }})
        flash("User Succesfully update", "succes")
        return redirect("/")
    else:
        form = UserForm()
        user = db.user_flask.find_one_or_404({"_id": ObjectId(id)})
        form.name.data = user.get("name", None)
        form.email.data = user.get("email", None)
        form.department.data = user.get("department", None)
        form.phone.data = user.get("phone", None)
    return render_template("add_user.html", title='Update User', form= form)


@app.route("/delete_user/<id>")
def delete_user(id):
    db.user_flask.find_one_and_delete({"_id": ObjectId(id)})
    flash("User deleted", "success")
    return redirect("/")






























