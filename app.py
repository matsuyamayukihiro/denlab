from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from models.models import *
from models.database import db_session
from datetime import datetime
import key
from hashlib import sha256

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
            [{"name": profile_user_name, "pass": profile_hashed_password}],
        "profile2":
            [{"name": profile_user_name, "pass": profile_hashed_password}],
        "profile3":
            [{"name": profile_user_name, "pass": profile_hashed_password}]
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
    column = session.query(column).all()  # データ取ってくる
    column = {
        {"column0": {
            "column_id": column.query.filter_by("SELECT column_id FROM column WHERE column.column_id=0"),
            "column_username": column.query.filter_by("SELECT column_username FROM column WHERE column.column_id=0"),
            "column_tag": column.query.filter_by("SELECT column_tag FROM column WHERE column.column_id=0"),
            "column_title": column.query.filter_by("SELECT column_title FROM column WHERE column.column_id=0"),
            "column_image1": column.query.filter_by("SELECT column_image1 FROM column WHERE column.column_id=0"),
            "column_image2": column.query.filter_by("SELECT column_image2 FROM column WHERE column.column_id=0"),
            "column_image3": column.query.filter_by("SELECT column_image3 FROM column WHERE column.column_id=0"),
            "column_image4": column.query.filter_by("SELECT column_image4 FROM column WHERE column.column_id=0"),
            "column_image5": column.query.filter_by("SELECT column_image5 FROM column WHERE column.column_id=0"),
            "column_image6": column.query.filter_by("SELECT column_image6 FROM column WHERE column.column_id=0"),
            "column_image7": column.query.filter_by("SELECT column_image7 FROM column WHERE column.column_id=0"),
            "column_image8": column.query.filter_by("SELECT column_image8 FROM column WHERE column.column_id=0"),
            "column_image9": column.query.filter_by("SELECT column_image9 FROM column WHERE column.column_id=0"),
            "column_image10": column.query.filter_by("SELECT column_image10 FROM column WHERE column.column_id=0"),
            "column_date": column.query.filter_by("SELECT column_date FROM column WHERE column.column_id=0")
            },
            "column1": {
                "column_id": column.query.filter_by("SELECT column_id FROM column WHERE column.column_id=1"),
                "column_username": column.query.filter_by("SELECT column_username FROM column WHERE column.column_id=1"),
                "column_tag": column.query.filter_by("SELECT column_tag FROM column WHERE column.column_id=1"),
                "column_title": column.query.filter_by("SELECT column_title FROM column WHERE column.column_id=1"),
                "column_image1": column.query.filter_by("SELECT column_image1 FROM column WHERE column.column_id=1"),
                "column_image2": column.query.filter_by("SELECT column_image2 FROM column WHERE column.column_id=1"),
                "column_image3": column.query.filter_by("SELECT column_image3 FROM column WHERE column.column_id=1"),
                "column_image4": column.query.filter_by("SELECT column_image4 FROM column WHERE column.column_id=1"),
                "column_image5": column.query.filter_by("SELECT column_image5 FROM column WHERE column.column_id=1"),
                "column_image6": column.query.filter_by("SELECT column_image6 FROM column WHERE column.column_id=1"),
                "column_image7": column.query.filter_by("SELECT column_image7 FROM column WHERE column.column_id=1"),
                "column_image8": column.query.filter_by("SELECT column_image8 FROM column WHERE column.column_id=1"),
                "column_image9": column.query.filter_by("SELECT column_image9 FROM column WHERE column.column_id=1"),
                "column_image10": column.query.filter_by("SELECT column_image10 FROM column WHERE column.column_id=1"),
                "column_date": column.query.filter_by("SELECT column_date FROM column WHERE column.column_id=1")
            },
            "column2": {
                "column_id": column.query.filter_by("SELECT column_id FROM column WHERE column.column_id=2"),
                "column_username": column.query.filter_by("SELECT column_username FROM column WHERE column.column_id=2"),
                "column_tag": column.query.filter_by("SELECT column_tag FROM column WHERE column.column_id=2"),
                "column_title": column.query.filter_by("SELECT column_title FROM column WHERE column.column_id=2"),
                "column_image1": column.query.filter_by("SELECT column_image1 FROM column WHERE column.column_id=2"),
                "column_image2": column.query.filter_by("SELECT column_image2 FROM column WHERE column.column_id=2"),
                "column_image3": column.query.filter_by("SELECT column_image3 FROM column WHERE column.column_id=2"),
                "column_image4": column.query.filter_by("SELECT column_image4 FROM column WHERE column.column_id=2"),
                "column_image5": column.query.filter_by("SELECT column_image5 FROM column WHERE column.column_id=2"),
                "column_image6": column.query.filter_by("SELECT column_image6 FROM column WHERE column.column_id=2"),
                "column_image7": column.query.filter_by("SELECT column_image7 FROM column WHERE column.column_id=2"),
                "column_image8": column.query.filter_by("SELECT column_image8 FROM column WHERE column.column_id=2"),
                "column_image9": column.query.filter_by("SELECT column_image9 FROM column WHERE column.column_id=2"),
                "column_image10": column.query.filter_by("SELECT column_image10 FROM column WHERE column.column_id=2"),
                "column_date": column.query.filter_by("SELECT column_date FROM column WHERE column.column_id=2")
            },
            "column3": {
                "column_id": column.query.filter_by("SELECT column_id FROM column WHERE column.column_id=3"),
                "column_username": column.query.filter_by("SELECT column_username FROM column WHERE column.column_id=3"),
                "column_tag": column.query.filter_by("SELECT column_tag FROM column WHERE column.column_id=3"),
                "column_title": column.query.filter_by("SELECT column_title FROM column WHERE column.column_id=3"),
                "column_image1": column.query.filter_by("SELECT column_image1 FROM column WHERE column.column_id=3"),
                "column_image2": column.query.filter_by("SELECT column_image2 FROM column WHERE column.column_id=3"),
                "column_image3": column.query.filter_by("SELECT column_image3 FROM column WHERE column.column_id=3"),
                "column_image4": column.query.filter_by("SELECT column_image4 FROM column WHERE column.column_id=3"),
                "column_image5": column.query.filter_by("SELECT column_image5 FROM column WHERE column.column_id=3"),
                "column_image6": column.query.filter_by("SELECT column_image6 FROM column WHERE column.column_id=3"),
                "column_image7": column.query.filter_by("SELECT column_image7 FROM column WHERE column.column_id=3"),
                "column_image8": column.query.filter_by("SELECT column_image8 FROM column WHERE column.column_id=3"),
                "column_image9": column.query.filter_by("SELECT column_image9 FROM column WHERE column.column_id=3"),
                "column_image10": column.query.filter_by("SELECT column_image10 FROM column WHERE column.column_id=3"),
                "column_date": column.query.filter_by("SELECT column_date FROM column WHERE column.column_id=3")
            },
            "column4": {
                "column_id": column.query.filter_by("SELECT column_id FROM column WHERE column.column_id=4"),
                "column_username": column.query.filter_by("SELECT column_username FROM column WHERE column.column_id=4"),
                "column_tag": column.query.filter_by("SELECT column_tag FROM column WHERE column.column_id=4"),
                "column_title": column.query.filter_by("SELECT column_title FROM column WHERE column.column_id=4"),
                "column_image1": column.query.filter_by("SELECT column_image1 FROM column WHERE column.column_id=4"),
                "column_image2": column.query.filter_by("SELECT column_image2 FROM column WHERE column.column_id=4"),
                "column_image3": column.query.filter_by("SELECT column_image3 FROM column WHERE column.column_id=4"),
                "column_image4": column.query.filter_by("SELECT column_image4 FROM column WHERE column.column_id=4"),
                "column_image5": column.query.filter_by("SELECT column_image5 FROM column WHERE column.column_id=4"),
                "column_image6": column.query.filter_by("SELECT column_image6 FROM column WHERE column.column_id=4"),
                "column_image7": column.query.filter_by("SELECT column_image7 FROM column WHERE column.column_id=4"),
                "column_image8": column.query.filter_by("SELECT column_image8 FROM column WHERE column.column_id=4"),
                "column_image9": column.query.filter_by("SELECT column_image9 FROM column WHERE column.column_id=4"),
                "column_image10": column.query.filter_by("SELECT column_image10 FROM column WHERE column.column_id=4"),
                "column_date": column.query.filter_by("SELECT column_date FROM column WHERE column.column_id=4")
            },
            "column5": {
                "column_id": column.query.filter_by("SELECT column_id FROM column WHERE column.column_id=5"),
                "column_username": column.query.filter_by("SELECT column_username FROM column WHERE column.column_id=5"),
                "column_tag": column.query.filter_by("SELECT column_tag FROM column WHERE column.column_id=5"),
                "column_title": column.query.filter_by("SELECT column_title FROM column WHERE column.column_id=5"),
                "column_image1": column.query.filter_by("SELECT column_image1 FROM column WHERE column.column_id=5"),
                "column_image2": column.query.filter_by("SELECT column_image2 FROM column WHERE column.column_id=5"),
                "column_image3": column.query.filter_by("SELECT column_image3 FROM column WHERE column.column_id=5"),
                "column_image4": column.query.filter_by("SELECT column_image4 FROM column WHERE column.column_id=5"),
                "column_image5": column.query.filter_by("SELECT column_image5 FROM column WHERE column.column_id=5"),
                "column_image6": column.query.filter_by("SELECT column_image6 FROM column WHERE column.column_id=5"),
                "column_image7": column.query.filter_by("SELECT column_image7 FROM column WHERE column.column_id=5"),
                "column_image8": column.query.filter_by("SELECT column_image8 FROM column WHERE column.column_id=5"),
                "column_image9": column.query.filter_by("SELECT column_image9 FROM column WHERE column.column_id=5"),
                "column_image10": column.query.filter_by("SELECT column_image10 FROM column WHERE column.column_id=5"),
                "column_date": column.query.filter_by("SELECT column_date FROM column WHERE column.column_id=5")
            },
            "column6": {
                "column_id": column.query.filter_by("SELECT column_id FROM column WHERE column.column_id=6"),
                "column_username": column.query.filter_by("SELECT column_username FROM column WHERE column.column_id=6"),
                "column_tag": column.query.filter_by("SELECT column_tag FROM column WHERE column.column_id=6"),
                "column_title": column.query.filter_by("SELECT column_title FROM column WHERE column.column_id=6"),
                "column_image1": column.query.filter_by("SELECT column_image1 FROM column WHERE column.column_id=6"),
                "column_image2": column.query.filter_by("SELECT column_image2 FROM column WHERE column.column_id=6"),
                "column_image3": column.query.filter_by("SELECT column_image3 FROM column WHERE column.column_id=6"),
                "column_image4": column.query.filter_by("SELECT column_image4 FROM column WHERE column.column_id=6"),
                "column_image5": column.query.filter_by("SELECT column_image5 FROM column WHERE column.column_id=6"),
                "column_image6": column.query.filter_by("SELECT column_image6 FROM column WHERE column.column_id=6"),
                "column_image7": column.query.filter_by("SELECT column_image7 FROM column WHERE column.column_id=6"),
                "column_image8": column.query.filter_by("SELECT column_image8 FROM column WHERE column.column_id=6"),
                "column_image9": column.query.filter_by("SELECT column_image9 FROM column WHERE column.column_id=6"),
                "column_image10": column.query.filter_by("SELECT column_image10 FROM column WHERE column.column_id=6"),
                "column_date": column.query.filter_by("SELECT column_date FROM column WHERE column.column_id=6")
            },
            "column7": {
                "column_id": column.query.filter_by("SELECT column_id FROM column WHERE column.column_id=7"),
                "column_username": column.query.filter_by("SELECT column_username FROM column WHERE column.column_id=7"),
                "column_tag": column.query.filter_by("SELECT column_tag FROM column WHERE column.column_id=7"),
                "column_title": column.query.filter_by("SELECT column_title FROM column WHERE column.column_id=7"),
                "column_image1": column.query.filter_by("SELECT column_image1 FROM column WHERE column.column_id=7"),
                "column_image2": column.query.filter_by("SELECT column_image2 FROM column WHERE column.column_id=7"),
                "column_image3": column.query.filter_by("SELECT column_image3 FROM column WHERE column.column_id=7"),
                "column_image4": column.query.filter_by("SELECT column_image4 FROM column WHERE column.column_id=7"),
                "column_image5": column.query.filter_by("SELECT column_image5 FROM column WHERE column.column_id=7"),
                "column_image6": column.query.filter_by("SELECT column_image6 FROM column WHERE column.column_id=7"),
                "column_image7": column.query.filter_by("SELECT column_image7 FROM column WHERE column.column_id=7"),
                "column_image8": column.query.filter_by("SELECT column_image8 FROM column WHERE column.column_id=7"),
                "column_image9": column.query.filter_by("SELECT column_image9 FROM column WHERE column.column_id=7"),
                "column_image10": column.query.filter_by("SELECT column_image10 FROM column WHERE column.column_id=7"),
                "column_date": column.query.filter_by("SELECT column_date FROM column WHERE column.column_id=7")
            },
            "column8": {
                "column_id": column.query.filter_by("SELECT column_id FROM column WHERE column.column_id=8"),
                "column_username": column.query.filter_by("SELECT column_username FROM column WHERE column.column_id=8"),
                "column_tag": column.query.filter_by("SELECT column_tag FROM column WHERE column.column_id=8"),
                "column_title": column.query.filter_by("SELECT column_title FROM column WHERE column.column_id=8"),
                "column_image1": column.query.filter_by("SELECT column_image1 FROM column WHERE column.column_id=8"),
                "column_image2": column.query.filter_by("SELECT column_image2 FROM column WHERE column.column_id=8"),
                "column_image3": column.query.filter_by("SELECT column_image3 FROM column WHERE column.column_id=8"),
                "column_image4": column.query.filter_by("SELECT column_image4 FROM column WHERE column.column_id=8"),
                "column_image5": column.query.filter_by("SELECT column_image5 FROM column WHERE column.column_id=8"),
                "column_image6": column.query.filter_by("SELECT column_image6 FROM column WHERE column.column_id=8"),
                "column_image7": column.query.filter_by("SELECT column_image7 FROM column WHERE column.column_id=8"),
                "column_image8": column.query.filter_by("SELECT column_image8 FROM column WHERE column.column_id=8"),
                "column_image9": column.query.filter_by("SELECT column_image9 FROM column WHERE column.column_id=8"),
                "column_image10": column.query.filter_by("SELECT column_image10 FROM column WHERE column.column_id=8"),
                "column_date": column.query.filter_by("SELECT column_date FROM column WHERE column.column_id=8")
            },
            "column9": {
                "column_id": column.query.filter_by("SELECT column_id FROM column WHERE column.column_id=9"),
                "column_username": column.query.filter_by("SELECT column_username FROM column WHERE column.column_id=9"),
                "column_tag": column.query.filter_by("SELECT column_tag FROM column WHERE column.column_id=9"),
                "column_title": column.query.filter_by("SELECT column_title FROM column WHERE column.column_id=9"),
                "column_image1": column.query.filter_by("SELECT column_image1 FROM column WHERE column.column_id=9"),
                "column_image2": column.query.filter_by("SELECT column_image2 FROM column WHERE column.column_id=9"),
                "column_image3": column.query.filter_by("SELECT column_image3 FROM column WHERE column.column_id=9"),
                "column_image4": column.query.filter_by("SELECT column_image4 FROM column WHERE column.column_id=9"),
                "column_image5": column.query.filter_by("SELECT column_image5 FROM column WHERE column.column_id=9"),
                "column_image6": column.query.filter_by("SELECT column_image6 FROM column WHERE column.column_id=9"),
                "column_image7": column.query.filter_by("SELECT column_image7 FROM column WHERE column.column_id=9"),
                "column_image8": column.query.filter_by("SELECT column_image8 FROM column WHERE column.column_id=9"),
                "column_image9": column.query.filter_by("SELECT column_image9 FROM column WHERE column.column_id=9"),
                "column_image10": column.query.filter_by("SELECT column_image10 FROM column WHERE column.column_id=9"),
                "column_date": column.query.filter_by("SELECT column_date FROM column WHERE column.column_id=9")
            },
            "column10": {
                "column_id": column.query.filter_by("SELECT column_id FROM column WHERE column.column_id=10"),
                "column_username": column.query.filter_by("SELECT column_username FROM column WHERE column.column_id=10"),
                "column_tag": column.query.filter_by("SELECT column_tag FROM column WHERE column.column_id=10"),
                "column_title": column.query.filter_by("SELECT column_title FROM column WHERE column.column_id=10"),
                "column_image1": column.query.filter_by("SELECT column_image1 FROM column WHERE column.column_id=10"),
                "column_image2": column.query.filter_by("SELECT column_image2 FROM column WHERE column.column_id=10"),
                "column_image3": column.query.filter_by("SELECT column_image3 FROM column WHERE column.column_id=10"),
                "column_image4": column.query.filter_by("SELECT column_image4 FROM column WHERE column.column_id=10"),
                "column_image5": column.query.filter_by("SELECT column_image5 FROM column WHERE column.column_id=10"),
                "column_image6": column.query.filter_by("SELECT column_image6 FROM column WHERE column.column_id=10"),
                "column_image7": column.query.filter_by("SELECT column_image7 FROM column WHERE column.column_id=10"),
                "column_image8": column.query.filter_by("SELECT column_image8 FROM column WHERE column.column_id=10"),
                "column_image9": column.query.filter_by("SELECT column_image9 FROM column WHERE column.column_id=10"),
                "column_image10": column.query.filter_by("SELECT column_image10 FROM column WHERE column.column_id=10"),
                "column_date": column.query.filter_by("SELECT column_date FROM column WHERE column.column_id=10")
            },
            "column11": {
                "column_id": column.query.filter_by("SELECT column_id FROM column WHERE column.column_id=11"),
                "column_username": column.query.filter_by("SELECT column_username FROM column WHERE column.column_id=11"),
                "column_tag": column.query.filter_by("SELECT column_tag FROM column WHERE column.column_id=11"),
                "column_title": column.query.filter_by("SELECT column_title FROM column WHERE column.column_id=11"),
                "column_image1": column.query.filter_by("SELECT column_image1 FROM column WHERE column.column_id=11"),
                "column_image2": column.query.filter_by("SELECT column_image2 FROM column WHERE column.column_id=11"),
                "column_image3": column.query.filter_by("SELECT column_image3 FROM column WHERE column.column_id=11"),
                "column_image4": column.query.filter_by("SELECT column_image4 FROM column WHERE column.column_id=11"),
                "column_image5": column.query.filter_by("SELECT column_image5 FROM column WHERE column.column_id=11"),
                "column_image6": column.query.filter_by("SELECT column_image6 FROM column WHERE column.column_id=11"),
                "column_image7": column.query.filter_by("SELECT column_image7 FROM column WHERE column.column_id=11"),
                "column_image8": column.query.filter_by("SELECT column_image8 FROM column WHERE column.column_id=11"),
                "column_image9": column.query.filter_by("SELECT column_image9 FROM column WHERE column.column_id=11"),
                "column_image10": column.query.filter_by("SELECT column_image10 FROM column WHERE column.column_id=11"),
                "column_date": column.query.filter_by("SELECT column_date FROM column WHERE column.column_id=11")
            }

        }
    }
    return jsonify(column)  # profile.jsonにjsonデータ返す


  # アイデア出し系
def idea():  # 投稿アイデア表示機能
    good_idea_check = session.query("SELECT * FROM idea\
                                       LEFT OUTER JOIN good_idea\
                                       ON idea.idea_id = good_idea.good_idea_id\
                                       WHERE idea.idea_id = 1\
                                       SELECT COUNT(idea_good) FROM idea")  # いいねした人idといいねされた対象投稿のidを連結したテーブル

    idea_id = good_idea_check.query("SELECT idea.idea_id FROM idea").all  # 抽出
    idea_username = good_idea_check.query("SELECT idea.idea_username FROM idea")
    idea_tag = good_idea_check.query("SELECT idea.idea_tag FROM idea")
    idea_title = good_idea_check.query("SELECT idea.column_image FROM idea")
    idea_discription = good_idea_check.query("SELECT idea.idea_discription FROM idea")
    idea_title = good_idea_check.query("SELECT idea.idea_title FROM idea")
    idea_image = good_idea_check.query("SELECT idea.column_image FROM idea")
    idea_good = good_idea_check.query("SELCT idea.idea_good FROM idea")  # 貰ったいいね数
    idea_date = good_idea_check.query("SELECT idea.idea_date FROM idea")

    idea = {
        "idea1": {
            "idea_id1": idea_id,
            "idea_username1": idea_username,
            "idea_tag1": idea_tag,
            "idea_discription1": idea_discription,
            "idea_image1": idea_image,
            "good_idea_check1": good_idea_check,
            "idea_date1": idea_date
        },
        "idea2": {
            "idea_id2": idea_id,
            "idea_username2": idea_username,
            "idea_tag2": idea_tag,
            "idea_discription2": idea_discription,
            "idea_image2": idea_image,
            "good_idea_check2": good_idea_check,
            "idea_date2": idea_date
        },
        "idea3": {
            "idea_id3": idea_id,
            "idea_username3": idea_username,
            "idea_tag3": idea_tag,
            "idea_discription3": idea_discription,
            "idea_image3": idea_image,
            "good_idea_check3": good_idea_check,
            "idea_date3": idea_date
        }
    }
    return jsonify(idea)  # jsonデータ返す
@app.route("/good_check", methods = ['post'])  #いいね機能
def good_check():
    good_idea_id = request.form["request_id"]  # いいねリクエストした対象投稿idデータ取得
    good_idea_userid = request.form["request_idea_id"]  #　いいねリクエストしたユーザidデータ取得
    good_idea_date = request.form["request_date_id"]  #  いいねリクエストした日時データ取得

    if(good_idea_id == good_idea.good_idea_id and good_idea_userid == good_idea.good_idea_userid):  # いいねした人+いいねした投稿がどちらも一致している
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
