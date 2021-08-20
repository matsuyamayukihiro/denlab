from sqlalchemy import Column, Integer, String, Text, DateTime #何のデータを扱いたいか?でimportするものは変わる
from models.database import Base
from datetime import datetime

class User(Base):#ログイン用
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(128), unique=True) #ユーザー名項目
    hashed_password = Column(String(128)) #

    def __init__(self, user_name=None, hashed_password=None):
        self.user_name = user_name
        self.hashed_password = hashed_password

    def __repr__(self):
        return '<Name %r>' % (self.user_name)

#DBの中身(カラム)を作っている
class OnegaiContent(Base):  #扱う情報を定義するクラス
    __tablename__ = 'onegaicontents'
    id = Column(Integer, primary_key=True) #Column(扱うデータ型,??)  Integer整数型　DB内の行を識別
    title = Column(String(128), unique=True)
    body = Column(Text)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, title=None, body=None, date=None, count=0): #カラム内の各値の初期化処理
        self.title = title
        self.body = body
        self.date = date
        self.count = 0

    def __repr__(self):
        return '<Title %r>' % (self.title)

#class post(Base):#投稿管理用
    #__tablename__ = 'post'
    #post_id = Column(Integer, primary_key=True)
    #liked_person = Column(String(128), unique=True) #ユーザー名項目
    #投稿詳細
    #投稿画像

#class post_liked(Base):#いいねチェック用
    #__tablename__ = 'post_liked'
    #liked_id = Column(Integer, primary_key=True)
    #good_person = Column(String(128), unique=True) #ユーザー名項目
    #

#class liked_user(Base):#いいねした人管理用
    #__tablename__ = 'post_liked'
    #liked_id = Column(Integer, primary_key=True)
    #good_person = Column(String(128), unique=True) #ユーザー名項目

#以下を追加
#追加終わり
