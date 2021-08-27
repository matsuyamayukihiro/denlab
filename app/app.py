from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from sqlalchemy.sql.base import ColumnCollection
from sqlalchemy import or_,desc
from models.models import *
from models.database import db_session
from datetime import datetime
from app import key
from hashlib import sha256

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


app = Flask(__name__)
app.secret_key = key.SECRET_KEY
app.config['JSON_AS_ASCII'] = False  # 日本語を使えるように

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
    return render_template("newcomer.html", status=status)

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

    user = session.query(User).all()
    profile_user_name = user.query("SELECT users.user_name FROM users")  # ニックネームデータ抽出
    profile_hashed_password = user.query("SELECT users.user_name FROM users")  # ハッシュタグデータ抽出
# フロント受け渡し用jsonファイル作成
    profile = {
        {"profile1":
            {"name": profile_user_name, "pass": profile_hashed_password},
         "profile2":
            {"name": profile_user_name, "pass": profile_hashed_password},
         "profile3":
            {"name": profile_user_name, "pass": profile_hashed_password}
         }
    }
    return jsonify(profile, profile)  # profile.jsonにjsonデータ返す

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
    # columns = db_session.\
    #     query(Columns).\
    #     filter(or_(Columns.column_id == 0,Columns.column_id == 1)).\
    #     order_by(Columns.column_id).\
    #     all() # データ取ってくる
    query = db_session.query(Columns)
    
    columns = query.all()
    count = query.count()
        
    
    list = {}
    for i,row in enumerate(columns):
        list["column" + str(i)] = row.toDict() 

    list["count"] = count
    return jsonify(list)



  # アイデア出し系
@app.route("/idea", methods=['post'])  # アイデア表示
def idea():  # 投稿アイデア表示機能
    idea = session.query("SELECT idea_id, idea_username, idea_tag, idea_title, idea_discription, idea_image, idea_good, idea_date\
                        (SELECT count (*) FROM idea WHERE good_idea.good_idea_id=idea.idea_id)as good")  # データ抽出
    idea = {
        "idea1": {
            "idea_id": idea.query.filter_by("SELECT idea_id FROM idea WHERE idea.idea_id=0"),
            "idea_username": idea.query.filter_by("SELECT idea_username FROM idea WHERE idea.idea_id=0"),
            "idea_tag": idea.query.filter_by("SELECT idea_tag FROM idea WHERE idea.idea_id=0"),
            "idea_title": idea.query.filter_by("SELECT idea_title FROM idea WHERE idea.idea_id=0"),
            "idea_discription": idea.query.filter_by("SELECT idea_discription FROM idea WHERE idea.idea_id=0"),
            "idea_image": idea.query.filter_by("SELECT idea_image FROM idea WHERE idea.idea_id=0"),
            "idea_good": idea.query.filter_by("SELECT good FROM idea WHERE idea.idea_id=0"),
            "idea_date": idea.query.filter_by("SELECT idea_date FROM idea WHERE idea.idea_id=0")
        },
        "idea2": {
            "idea_id": idea.query.filter_by("SELECT idea_id FROM idea WHERE idea.idea_id=1"),
            "idea_username": idea.query.filter_by("SELECT idea_username FROM idea WHERE idea.idea_id=1"),
            "idea_tag": idea.query.filter_by("SELECT idea_tag FROM idea WHERE idea.idea_id=1"),
            "idea_title": idea.query.filter_by("SELECT idea_title FROM idea WHERE idea.idea_id=1"),
            "idea_discription": idea.query.filter_by("SELECT idea_discription FROM idea WHERE idea.idea_id=1"),
            "idea_image": idea.query.filter_by("SELECT idea_image FROM idea WHERE idea.idea_id=1"),
            "idea_good": idea.query.filter_by("SELECT idea_good FROM idea WHERE idea.idea_id=1"),
            "idea_date": idea.query.filter_by("SELECT idea_date FROM idea WHERE idea.idea_id=1")
        },
        "idea3": {
            "idea_id": idea.query.filter_by("SELECT idea_id FROM idea WHERE idea.idea_id=2"),
            "idea_username": idea.query.filter_by("SELECT idea_username FROM idea WHERE idea.idea_id=2"),
            "idea_tag": idea.query.filter_by("SELECT idea_tag FROM idea WHERE idea.idea_id=2"),
            "idea_title": idea.query.filter_by("SELECT idea_title FROM idea WHERE idea.idea_id=2"),
            "idea_discription": idea.query.filter_by("SELECT idea_discription FROM idea WHERE idea.idea_id=2"),
            "idea_image": idea.query.filter_by("SELECT idea_image FROM idea WHERE idea.idea_id=2"),
            "idea_good": idea.query.filter_by("SELECT idea_good FROM idea WHERE idea.idea_id=2"),
            "idea_date": idea.query.filter_by("SELECT idea_date FROM idea WHERE idea.idea_id=2")
        }
    }
    return jsonify(idea)  # jsonデータ返す

@app.route("/good_add", methods=['post'])  # いいね機能
def good_add():  # 投稿アイデア表示機能
    good_idea_id = request.form["request_idea_id"]  # いいねリクエストした対象投稿idデータ取得
    good_idea_userid = request.form["request_idea_userid"]  # いいねリクエストしたユーザidデータ取得
    good_idea_date = request.form["request_date_id"]  # いいねリクエストした日時データ取得
    good_idea_check = session.query("SELECT * FROM idea\
                                    LEFT OUTER JOIN good_idea\
                                    ON idea.idea_id = good_idea.good_idea_id\
                                    WHERE idea.idea_id = 0\
                                    SELECT COUNT(idea.idea_id=good_idea_id) FROM idea")  # いいねした人idといいねされた対象投稿のidを連結したテーブル

    if(good_idea_id == good_idea_check.good_idea_id and good_idea_userid == good_idea_check.good_idea_userid):  # いいねした人+いいねした投稿がどちらも一致している
        delete = session.query.filter_by(good_idea_id == good_idea.good_idea_id and good_idea_userid == good_idea.good_idea_userid).all()  # リクエスト者idと対になるidを持つレコードを抽出
        db_session.delete(delete)  # 消す
        db_session.commit()  # 反映

    else:  #　リストに名前が無かったら、
        good_person = good_idea(good_idea_id=idea.idea_id, good_idea_userid=good_idea_userid, good_idea_date=good_idea_date)  #　いいねリクエスト者データに入れる要素代入（引数は追加したいデータ）
        db_session.add(good_person)  # 引数は追加したい変数
        db_session.commit()  # 追加データの反映


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


if __name__ == "__main__":
    app.run(debug=True)
