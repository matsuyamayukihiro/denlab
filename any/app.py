# フロントとバックエンド連携を行うpg 松山担当
from flask import Flask, render_template, request
from flask import session, redirect, url_for
from any import key
from hashlib import sha256
from models.models import columns, ideas, User
from models.database import db_session
from datetime import datetime
from bs4 import BeautifulSoup
from urllib import request as Request

# Flaskオブジェクトの生成
app = Flask(__name__)
app.secret_key = key.SECRET_KEY  # セッション情報の暗号化


# ログイン画面表示処理
@app.route("/login.html")
def login_face():
    return render_template("login.html")


def miss(status2):
    return render_template("login.html", status=status2)


# ログイン画面へ遷移
@app.route("/login", methods=["post"])
def login():  # ログイン処理
    user_name = request.form["user_name"]
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        password = request.form["password"]
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        if user.hashed_password == hashed_password:  # ログインできた場合
            session["user_name"] = user_name
            status = "login"
            return home1(status)  # 一度ホーム画面へ
        else:
            status2 = "wrong_password"
            return miss(status2)  # パスワードのみご入力したとき、もう一度ログイン画面へ
    else:
        status2 = "wrong_password"
        return miss(status2)  # ユーザ名、パスのどちらも間違えた際はアカウント登録してるかチェック


@app.route("/registar", methods=["post"])  # 新規ユーザ登録処理
def registar():
    user_name = request.form["user_name"]
    user = User.query.filter_by(user_name=user_name).first()
    if user:  # DB内に既に登録済みの時、その旨メッセージ出す
        newcomer_status = "exist_user"
        return newcomer_face1(newcomer_status)
    else:  # DB内に新ユーザ情報の登録
        password = request.form["password"]
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        user = User(user_name, hashed_password)
        db_session.add(user)
        db_session.commit()
        session["user_name"] = user_name
        status = "post"
        return home1(status)


# アカウント新規登録画面表示処理
@app.route("/newcomer.html")
def newcomer_face():
    return render_template("newcomer.html")


def newcomer_face1(newcomer_status):
    return render_template("newcomer.html", newcomer_status=newcomer_status)


@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("miss", status="logout"))


# 「/home」へアクセスがあった場合に、「home.html」を返す
@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


def home1(status):
    return render_template("home.html", status=status)


# コラムページ表示
@app.route("/column.html")
def column():
    all_onegai = columns.query.all()
    return render_template("column.html", all_onegai=all_onegai)


# コラムページ表示
def post_column(stutas):
    all_onegai = columns.query.all()
    return render_template("column.html", all_onegai=all_onegai, stutas=stutas)


# コラムコンテンツ表示
@app.route("/column_display.html", methods=["post"])
def column_display():
    nb = request.form['column_id']  # アイデアID取得
    url = 'https://denlab2.herokuapp.com/column.html'
    response = Request.urlopen(url)
    soup = BeautifulSoup(response)
    column = soup.find_all('section', class_='card-list')
    title = column[int(nb)].select('h2.card-title')[0].text
    response.close()
    column_input = db_session.query(columns).filter(columns.columns_title == title).all()
    return render_template("column_display.html", column_all=column_input)


# コラム新規登録画面表示
@app.route("/new_column_post.html")
def face():
    if "user_name" in session:  # ログインしているときにのみ、新規投稿画面を表示
        return render_template("new_column_post.html")

    else:
        return render_template("login.html")


# コラム新規登録処理
@app.route("/add", methods=["post"])
def add():  # フォームより情報取得
    columns_title = request.form["title"]  # コラムタイトル
    columns_username = request.form["name"]  # 投稿者名
    columns_discription = request.form["discription"]  # 詳細説明
    columns_images1 = request.form["url1"]  # 画像
    columns_images2 = request.form["url2"]  # 画像
    columns_images3 = request.form["url3"]  # 画像
    columns_images4 = request.form["url4"]  # 画像
    columns_images5 = request.form["url5"]  # 画像
    column_content = columns(columns_title, columns_username, columns_discription, columns_images1, columns_images2, columns_images3, columns_images4,
                             columns_images5, datetime.now())
    db_session.add(column_content)
    db_session.commit()
    stutas = "post"
    return post_column(stutas)


# アイデアページ表示
@app.route("/idea.html")
def idea():
    all_idea = ideas.query.all()
    return render_template("idea.html", all_idea=all_idea)


# アイデアページ表示
def post_idea(stutas1):
    all_idea = ideas.query.all()
    return render_template("idea.html", all_idea=all_idea, stutas=stutas1)


# アイデアコンテンツ表示
@app.route("/idea_display.html", methods=["post"])
def idea_display():
    nb = request.form['idea_id']  # アイデアID取得
    url = 'https://denlab2.herokuapp.com/idea.html'
    response = Request.urlopen(url)
    soup = BeautifulSoup(response)
    idea = soup.find_all('section', class_='card-list')
    title = idea[int(nb)].select('h2.card-title')[0].text
    response.close()
    idea_input = db_session.query(ideas).filter(ideas.idea_title == title).all()
    return render_template("idea_display.html", idea_all=idea_input)


# アイデア新規登録画面表示
@app.route("/new_idea_post.html")
def idea_face():
    if "user_name" in session:
        return render_template("new_idea_post.html")

    else:
        return render_template("login.html")


# アイデア新規登録
@app.route("/addidea", methods=["post"])
def add_idea():  # フォームより情報取得
    idea_title = request.form["title"]  # コラムタイトル
    idea_username = request.form["name"]  # 投稿者名
    idea_discription = request.form["discription"]  # 詳細説明
    idea_images1 = request.form["url1"]  # 画像
    idea_images2 = request.form["url2"]  # 画像
    idea_good = 0
    idea_content = ideas(idea_title, idea_username, idea_discription, idea_images1, idea_images2, idea_good, datetime.now())
    db_session.add(idea_content)
    db_session.commit()
    stutas1 = "post"
    return post_idea(stutas1)
