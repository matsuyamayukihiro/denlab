from flask import Flask, render_template, request, session, redirect,url_for
from models.models import OnegaiContent, User
from models.database import db_session
from datetime import datetime
from app import key
from hashlib import sha256
import json

app = Flask(__name__)
app.secret_key = key.SECRET_KEY

#ログイン系
@app.route("/login",methods=["post"])  # ログイン機能
def login():
    user_name = request.form["user_name"]  # フォームに入力されたユーザ名を取得
    user = User.query.filter_by(user_name=user_name).first()  # そのユーザ名を持つDBレコードをusersテーブルから抽出しています
    if user:  # 入力された名前がDBより抽出した時
        password = request.form["password"]
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        if user.hashed_password == hashed_password:  # DB内のパス = 入力されたパスがという構図
            session["user_name"] = user_name  # セッション情報にユーザ名を追加
            return redirect(url_for("index"))  # メインページへ遷移
        else:
            return redirect(url_for("top", status="wrong_password"))
    else:
        return redirect(url_for("top", status="user_notfound"))

@app.route("/newcomer")  # 新規登録機能
def newcomer():
    status = request.args.get("status")
    return render_template("newcomer.html",status=status)

@app.route("/registar", methods=["post"])  # 新規登録機能
def registar():
    user_name = request.form["user_name"]  # ユーザ名orメアド登録も可能
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        return redirect(url_for("newcomer", status="exist_user"))
    else:
        password = request.form["password"]  # 入力されたパスワードの取得
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()  # 暗号化している
        user = User(user_name, hashed_password)
        db_session.add(user)  # DBに追加(userクラス)　
        db_session.commit()  # DBに反映
        session["user_name"] = user_name  # セッション情報にユーザ名を追加
        return redirect(url_for("index"))  # メインページへ遷移

@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("top", status="logout"))

# トップページ系
@app.route("/")
@app.route("/index")
def index():  # トップページ開く
    if "user_name" in session:
        name = session["user_name"]
        all_onegai = OnegaiContent.query.all()
        return render_template("index.html", name=name, all_onegai=all_onegai)
    else:
        return redirect(url_for("top", status="logout"))

# コラム系
@app.route("/column")   # コラム表示機能
def column():
    column = db_session.query(column).all  # コラム情報全件取得
    for row in column:  # 1カードずつjsonでデータ渡す
        column = {
            "column"+row: {
                "column_id": column.column_id,
                "column_username": column.column_username,
                "column_tag": column.column_tag,
                "column_image": column.column_image,
                "column_date": column.colum_date,
            }
         }

#@app.route("/good", methods = ['post'])    #いいねボタン処理
#def good_check():
    #post_person = post_liked.query.filter_by(id=request.form["update"]).first()#いいねされた投稿データに対して既にいいねした人呼び出し&変数(good_person)に代入
    #liked_person = liked_user.query.filter_by(id=request.form["update"]).first()#その投稿にいいねした人のデータの呼び出し&変数に代入(引数にはgoodを使用する)
    #liked_personといいねリクエスト者を照合
    #if post_person == liked_person:#既にいいねしている場合
        # #リストに名前があったら（既にいいねしてる）場合、ノーカウント

    #else:#リストに名前が無かったら、
        #liked_person = post(liked_person) #OnegaiContent=データ追加（引数は追加したいデータ）
        #db_session.add(liked_person)#引数は追加したい変数
        #db_session.commit() #追加データの反映#dbにユーザ名追加
    #good_person内の名前をカウント&変数(good_count)に代入
    #good_countを表示


@app.route("/add", methods=["post"])
def add():  # データベース内の各項目に入力値の追加
    title = request.form["title"]  # HTML内のデータ取得
    body = request.form["body"]
    content = OnegaiContent(title, body, datetime.now())  # OnegaiContent=データ追加（引数は追加したいデータ）
    db_session.add(content)  # 引数は追加したい変数
    db_session.commit()  # 追加データの反映
    return redirect(url_for("index"))

@app.route("/update", methods=["post"])
def update():
    content = OnegaiContent.query.filter_by(id=request.form["update"]).first()
    content.title = request.form["title"]
    content.body = request.form["body"]
    db_session.commit()
    return redirect(url_for("index"))


@app.route("/delete", methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    for id in id_list:
        content = OnegaiContent.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return redirect(url_for("index"))

@app.route("/top")
def top():
    status = request.args.get("status")
    return render_template("top.html", status=status)

#@app.route('/json')   #jsonファイル処理
#def json():
 #   a = open('sample.json')#jsonファイルオープン
  #  b = json.load(a)#データ代入
   # print(b)


if __name__ == "__main__":
    app.run(debug=True)
