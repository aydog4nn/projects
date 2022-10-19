import re
from flask import Flask,render_template,redirect,flash,url_for,session,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,validators,FloatField
app = Flask(__name__)
app.secret_key = "movies"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "movies"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

class MoviesForm(Form):

    isim = StringField("Film İsmi",validators=[validators.Length(min = 1,max = 50)])
    kategori = StringField("Kategori",validators=[validators.Length(min = 1,max = 30)])
    puan =  FloatField("Puan")
    eleştiri = TextAreaField("Film Hakkında Eleştirileriniz")

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/viewed")
def viewed():

    cursor = mysql.connection.cursor()
    sorgu = "SELECT * FROM movies"
    result = cursor.execute(sorgu)

    if result > 0:

        movies = cursor.fetchall()
        return render_template("viewed.html",movies = movies)

    else:

        return render_template("viewed.html")

@app.route("/add",methods = ["GET","POST"])
def add():

    form = MoviesForm(request.form)
    if request.method == "POST" and form.validate():

        isim = form.isim.data
        eleştiri = form.eleştiri.data
        kategori = form.kategori.data
        puan = form.puan.data
        

        cursor = mysql.connection.cursor()
        sorgu = "INSERT INTO movies(isim,kategori,puan,eleştiri) VALUES(%s,%s,%s,%s)"
        cursor.execute(sorgu,(isim,kategori,puan,eleştiri))
        mysql.connection.commit()
        cursor.close()
        flash("Film başarıyla eklendi!","success")
        return redirect(url_for("viewed"))
    
    return render_template("addmovies.html",form = form)

@app.route("/search",methods = ["GET","POST"])
def search():

    if request.method == "GET":
        return redirect(url_for("index"))
    else:
        keyword = request.form.get("keyword")
        cursor = mysql.connection.cursor()
        sorgu = "SELECT * FROM movies where title like '%" + keyword + "%' "
        result = cursor.execute(sorgu)

        if result == 0:
            flash("Aranan kelimeye uygun film bulunamadı.","warning")
            return redirect(url_for("viewed"))
        else:
            movies = cursor.fetchall()
            return render_template("search.html",movies = movies)

@app.route("/viewed/<string:id>")
def movie(id):

    cursor = mysql.connection.cursor()
    sorgu = "SELECT * FROM movies where id = %s"
    result = cursor.execute(sorgu,(id,))

    if result > 0:
        movie = cursor.fetchone()
        return render_template("movie.html",movie=movie)
    else:
        return render_template("movie.html")
@app.route("/edit/<string:id>",methods = ["GET","POST"])
def edit(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "SELECT * FROM movies where id = %s"
        result = cursor.execute(sorgu,(id,))
        if result == 0:
            flash("Böyle bir film bulunmuyor","danger")
            return redirect(url_for("index"))
        else:
            movie = cursor.fetchone()
            form = MoviesForm()
            form.isim.data = movie["isim"]
            form.puan.data = movie["puan"]
            form.eleştiri.data = movie["eleştiri"]
            return render_template("edit.html",form = form)

    else:

        form = MoviesForm(request.form)
        yeniIsım = form.isim.data
        yeniPuan = form.puan.data
        yeniEleştiri = form.eleştiri.data

        cursor = mysql.connection.cursor()
        sorgu2 = "UPDATE movies set isim = %s,puan = %s,eleştiri = %s where id = %s"
        cursor.execute(sorgu2,(yeniIsım,yeniPuan,yeniEleştiri,id))
        mysql.connection.commit()
        flash("Film başarıyla güncellendi","success")
        return redirect(url_for("viewed"))

@app.route("/delete/<string:id>")
def delete(id):

    cursor = mysql.connection.cursor()
    sorgu = "DELETE FROM movies where id =%s"
    cursor.execute(sorgu,(id,))
    mysql.connection.commit()
    flash("Film başarıyla silindi!","success")
    return redirect(url_for("viewed"))
   
if __name__ == "__main__":
    app.run(debug=True)