from sqlalchemy import Column, Integer, String, Text, DateTime  # 何のデータを扱いたいか?でimportするものは変わる
from models.database import Base
from datetime import datetime

# ログイン用
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)  # id
    user_name = Column(String(128), unique=True)  # ユーザー名項目
    hashed_password = Column(String(128))  # セキュリティ化したパスワード

    def __init__(self, user_name=None, hashed_password=None):
        self.user_name = user_name  # 初期化
        self.hashed_password = hashed_password  # 初期化

    def __repr__(self):
        return '<Name %r>' % (self.user_name)  # ???


#コラム用
class Columns(Base):
    __tablename__ = 'column'
    column_id = Column(Integer, primary_key=True)   # id
    column_username = Column(String(128), unique=True)  # 投稿ユーザー名
    column_tag = Column(Text)  # ジャンル識別タグ
    column_title = Column(Text(30))  # コラムタイトル
    column_image1 = Column(Text) # 画像（パスで入力）
    column_image2 = Column(Text)  # 画像（パスで入力）
    column_image3 = Column(Text)  # 画像（パスで入力）
    column_image4 = Column(Text)  # 画像（パスで入力）
    column_image5 = Column(Text)  # 画像（パスで入力）
    column_image6 = Column(Text)  # 画像（パスで入力）
    column_image7 = Column(Text)  # 画像（パスで入力）
    column_image8 = Column(Text)  # 画像（パスで入力）
    column_image9 = Column(Text)  # 画像（パスで入力）
    column_image10 = Column(Text)  # 画像（パスで入力）
    column_date = Column(DateTime, default=datetime.now())  # 投稿日時

    def toDict(self):
        return {
                "column_id": self.column_id,
                "column_username": self.column_username,
                "column_tag": self.column_tag,
                "column_title": self.column_title,
                "column_image1": self.column_image1,
                "column_image2": self.column_image2,
                "column_image3": self.column_image3,
                "column_image4": self.column_image4,
                "column_image5": self.column_image5,
                "column_image6": self.column_image6,
                "column_image7": self.column_image7,
                "column_image8": self.column_image8,
                "column_image9": self.column_image9,
                "column_image10": self.column_image10,
                "column_date": self.column_date
        }

#初期化
    def __init__(self, column_id=None, column_username=None, column_tag=None, column_image1=None, column_image2=None, column_image3=None, column_image4=None, column_image5=None, column_image6=None, column_image7=None, column_image8=None, column_image9=None, column_image10=None, column_date=None):
        self.column_id = column_id
        self.column_username = column_username
        self.column_tag = column_tag
        self.column_image1 = column_image1  # 画像（パスで入力）
        self.column_image2 = column_image2  # 画像（パスで入力）
        self.column_image3 = column_image3  # 画像（パスで入力）
        self.column_image4 = column_image4  # 画像（パスで入力）
        self.column_image5 = column_image5  # 画像（パスで入力）
        self.column_image6 = column_image6  # 画像（パスで入力）
        self.column_image7 = column_image7  # 画像（パスで入力）
        self.column_image8 = column_image8  # 画像（パスで入力）
        self.column_image9 = column_image9  # 画像（パスで入力）
        self.column_image10 = column_image10  # 画像（パスで入力）
        self.column_date = column_date


# アイデア用
class idea(Base):  # アイデア管理用
    __tablename__ = 'idea'
    idea_id = Column(Integer, primary_key=True)
    idea_username = Column(String(128), unique=True)  # ユーザー名項目
    idea_tag = Column(Text)  # 工芸品ジャンル分けタグ
    idea_title = Column(Text(30))  # アイデアタイトル
    idea_discription = Column(Text(300))  # 詳細説明
    idea_image = Column(Text)  # 画像データ
    idea_good = Column(Integer, unique=False)  # 貰ったいいね数
    idea_date = Column(DateTime, default=datetime.now())  # 投稿日時

    def __init__(self, idea_id=None, idea_username=None, idea_tag="和紙", idea_title=None, idea_discription=None, idea_image=None, idea_good=None, idea_date=None):
        self.idea_id = idea_id
        self.idea_username = idea_username  # ユーザー名項目
        self.idea_tag = idea_tag  # 工芸品ジャンル分けタグ今回は和紙限定
        self.idea_title = idea_title  # アイデアタイトル
        self.idea_discription = idea_discription  # 詳細説明
        self.idea_image = idea_image  # 画像データ
        self.idea_good = idea_good  # 貰ったいいね数
        self.idea_date = idea_date  # 投稿日時

class good_idea(Base):#いいねチェック用
    __tablename__ = 'good_idea'
    good_idea_id = Column(Integer, primary_key=True)  # いいね！した対象投稿のID
    good_idea_userid = Column(Integer, unique=True)  # いいね！した人自身のID
    good_idea_date = Column(DateTime, default=datetime.now())  # いいねした日時

    def __init__(self, good_idea_id=None, good_idea_userid=None, good_idea_date=None):
        self.good_idea_id = good_idea_id
        self.good_idea_userid = good_idea_userid  # ユーザー名項目
        self.good_idea_date = good_idea_date  # 工芸品ジャンル分けタグ

# 後々消すやつ
class OnegaiContent(Base):
    __tablename__ = 'onegaicontents'
    id = Column(Integer, primary_key=True)  # Column(扱うデータ型,??)  Integer整数型　DB内の行を識別
    title = Column(String(128), unique=True)
    body = Column(Text(200))
    date = Column(DateTime, default=datetime.now())

    def __init__(self, title=None, body=None, date=None):  # カラム内の各値の初期化処理
        self.title = title
        self.body = body
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)
