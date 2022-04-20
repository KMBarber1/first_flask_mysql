from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User


@app.route("/")
def i():
    return redirect("/users")


@app.route("/users")
def index():
    list_of_users = User.get_all()
    print(list_of_users)

    return render_template("index.html", all_users = list_of_users)

@app.route("/users/new")
def new_user():
    return render_template("new_user.html")

@app.route("/users/create", methods = ["POST"])
def create_user():
    print(request.form)
    user_id = User.create(request.form)

    return redirect(f"/users/{user_id}/show")

@app.route("/users/<int:user_id>/show")
def show_user(user_id):
    return render_template("show_user.html", this_user = User.get_one({"id": user_id}))

@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    return render_template("edit_user.html", this_user = User.get_one({"id": user_id}))

# @app.route("/users/<int:user_id>/info")
# def info_user(user_id):
#     return render_template("info_user.html", this_user = User.get_one({"id": user_id}))

@app.route("/users/<int:user_id>/update", methods = ["POST"])
def update_user(user_id):
    updated_data = {
        **request.form,
        "id": user_id
    }
    User.update(request.form)

    return redirect(f"/users/{user_id}/show")




# @app.route("/users/show", methods = ["POST"])
# def create_user():
#     print(request.form)
#     user_id = User.create(request.form)

#     return redirect(f"/users/{user_id}/edit")




@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    User.delete({"id":user_id})

    return redirect("/users")