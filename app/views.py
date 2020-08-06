from app import app

from flask import render_template, request, redirect, jsonify, make_response

import os

from datetime import datetime

from werkzeug.utils import secure_filename


@app.template_filter("clean_date")
def clean_date(dt):
  return dt.strftime("%d %b %Y")


@app.route("/")
def index():
  
  #app.config["SECRET_KEY"] = "adjajdnjasndjandjansdjn"
  #app.config["DB_USERNAME"] = "dbtotalsubastas"
  print(f"Hola")
  
  return render_template("public/index.html")



@app.route("/jinja")
def jinja():

  my_name = "Javier"

  age=20

  langs=["Python","Javascript","Bash","C","Ruby"]

  friends = {
    "Tom":30,
    "Amy":60,
    "Tony":56,
    "Clarissa":23
  }

  colours = ("Red","Green")

  cool = True

  class GitRemote:
    def __init__(self, name, description, url):
      self.name = name
      self.description = description
      self.url = url
    
    def pull(self):
      return f"Pullin repo {self.name}"

    def clone(self):
      return f"Clonning into {self.url}"

  my_remote = GitRemote(
    name="Flask Jinja",
    description="Template design tutorial",
    url="https://github.com/julian-nash/jinja.git"
  )

  def repeat(x, qty):
    return x * qty

  date = datetime.utcnow()

  my_html = "<h1>THIS IS SOME HTML</h1>"

  suspicious = "<script>alert('YO GOT HACKED');</script>"

  return render_template(
    "public/jinja.html", 
    my_name=my_name,
    age=age,
    langs=langs,
    friends=friends,
    colours=colours,
    cool=cool,
    GitRemote=GitRemote,
    repeat=repeat,
    my_remote=my_remote,
    date=date,
    my_html=my_html,
    suspicious=suspicious
  )

@app.route("/about")
def about():
  return "<h1 style='color:red'> About Me!!! <h1>"

@app.route("/sign-up", methods=["GET","POST"])
def sign_up():
  if request.method == "POST":
    req = request.form
    print(req)
    username = req["username"]
    email = req.get("email")
    password = request.form["password"]
    print(username," - ",email," - ", password)
    return redirect(request.url)

  return render_template("public/sign_up.html")

users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creatof of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}


@app.route("/profile/<username>")
def profile(username):
  user = None
  if username in users:
    user = users[username]
  return render_template("public/profile.html", username=username, user=user)


@app.route("/multiple/<foo>/<bar>/<baz>")
def multiple(foo, bar, baz):
  return f"foo is {foo}, bar is {bar}, baz is {baz}"

@app.route("/json", methods=["POST"])
def json():
  if request.is_json:
    req = request.get_json()
    response = {
      "message": "JSON recevied",
      "name": req.get("name")
    }
    res = make_response(jsonify(response), 200)
    return res
  else:
    res = make_response(jsonify({"message": "No JSON recevied!"}), 400)
    return res

@app.route("/guestbook")
def guestbook():
  return render_template("public/guestbook.html")


# Simulo que expongo un api
@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():

  req = request.get_json()

  print(req)

  res = make_response(jsonify(req), 200)
  return res


@app.route("/query")
def query():

  if request.args:

    args = request.args

    serialized = ", ".join(f"{k}: {v}" for k, v in args.items())

    return f"(query) {serialized}", 200
    # if "title" in args:
    #   title = request.args.get("title")

  else:

    return "No query received", 200


app.config["IMAGE_UPLOADS"] = "/Users/javierdiaz/Dropbox/Belcorp/VirtualCoach/FLASK/app/static/img/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024

def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_image_filesize(filesize):

    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


@app.route("/upload_image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            if "filesize" in request.cookies:

                if not allowed_image_filesize(request.cookies["filesize"]):
                    print("Filesize exceeded maximum limit")
                    return redirect(request.url)

                image = request.files["image"]

                if image.filename == "":
                    print("No filename")
                    return redirect(request.url)

                if allowed_image(image.filename):
                    filename = secure_filename(image.filename)

                    image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                    print("Image saved")

                    return redirect(request.url)

                else:
                    print("That file extension is not allowed")
                    return redirect(request.url)

    return render_template("public/upload_image.html")


from flask import send_from_directory, abort


@app.route("/get-image/<image_name>")
def get_image(image_name):
  return "Thanks"
