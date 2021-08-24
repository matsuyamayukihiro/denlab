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
class column(Base):
    __tablename__ = 'column'
    column_id = Column(Integer, primary_key=True)   # id
    column_username = Column(String(128), unique=True)  # 投稿ユーザー名
    column_tag = Column(Text)  # ジャンル識別タグ
    column_title = Column(Text(30))  # コラムタイトル
    column_image = Column(Text) # 画像（パスで入力）
    column_date = Column(DateTime, default=datetime.now())  # 投稿日時

#初期化
    def __init__(self, column_id=None, column_username=None, column_tag=None, column_image=None, colum_date=None):
        self.column_id = column_id
        self.column_username = column_username
        self.column_tag = column_tag
        self.column_image = column_image
        self.colum_date = colum_date


# アイデア用
class idea(Base):  # アイデア管理用
    __tablename__ = 'idea'
    idea_id = Column(Integer, primary_key=True)
    idea_username = Column(String(128), unique=True)  # ユーザー名項目
    idea_tag = Column(Text)  # 工芸品ジャンル分けタグ
    idea_title = Column(Text(30))  # アイデアタイトル
    idea_discription = Column(Text(300))  # 詳細説明
    idea_image = Column(Text)  # 画像データ
    idea_date = Column(DateTime, default=datetime.now())  # 投稿日時

    def __init__(self, idea_id=None, idea_username=None, idea_tag=None, idea_title=None, idea_discription=None, idea_image=None, idea_date=None):
        self.idea_id = idea_id
        self.idea_username = idea_username  # ユーザー名項目
        self.idea_tag = idea_tag  # 工芸品ジャンル分けタグ
        self.idea_title = idea_title  # アイデアタイトル
        self.idea_discription = idea_discription  # 詳細説明
        self.idea_image = idea_image  # 画像データ
        self.idea_date = idea_date  # 投稿日時

class good_idea(Base):#いいねチェック用
    __tablename__ = 'good_idea'
    good_idea_id = Column(Integer, primary_key=True)  # いいね！した対象投稿のID
    good_idea_userid = Column(Integer, unique=True)  # いいね！した人自身のID
    good_idea_date = Column(DateTime, default=datetime.now())  # いいねした日時

#SELECT  ＊ FROM [投稿]
#LEFT OUTER JOIN [投稿ーいいね]
#ON [投稿].投稿ID = [投稿ーいいね].投稿ID
#WHERE 投稿ID ＝ １
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
