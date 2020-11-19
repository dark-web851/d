from flask import Flask , render_template,request,flash,redirect,url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

UPLOAD_FOLDER = os.path.join("media","uploads")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/",methods = ["GET","POST"])
def hello():
    if request.method == "POST" :
        print(request.files)
        if 'file' not in request.files: 
            flash("No file")
            return redirect(request.url)
        file = request.files['file']
        fname = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"],fname))
        return redirect(request.url)

    return render_template('web.html')

@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')

app.run(debug=True)
