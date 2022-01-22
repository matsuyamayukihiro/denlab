from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(128), unique=False)  # ユーザ名
    hashed_password = Column(String(128), unique=True)  # ユーザパスワード

    def __init__(self, user_name=None, hashed_password=None):
        self.user_name = user_name
        self.hashed_password = hashed_password  # パスワードハッシュ化

    def __repr__(self):
        return '<Name %r>' % self.user_name


class columns(Base):
    __tablename__ = 'Columns'
    columns_id = Column(Integer, primary_key=True)
    columns_title = Column(String(128), unique=True)  # コラムタイトル
    columns_username = Column(Text)  # 投稿者名
    columns_discription = Column(Text(300))  # 詳細説明
    columns_images1 = Column(Text)  # 画像
    columns_images2 = Column(Text)  # 画像
    columns_images3 = Column(Text)  # 画像
    columns_images4 = Column(Text)  # 画像
    columns_images5 = Column(Text)  # 画像
    columns_date = Column(DateTime, default=datetime.now())

    def __init__(self, columns_title=None, columns_username=None, columns_discription=None, columns_images1=None,
                 columns_images2=None, columns_images3=None, columns_images4=None, columns_images5=None, columns_date=None):
        self.columns_title = columns_title
        self.columns_username = columns_username
        self.columns_discription = columns_discription
        self.columns_images1 = columns_images1
        self.columns_images2 = columns_images2
        self.columns_images3 = columns_images3
        self.columns_images4 = columns_images4
        self.columns_images5 = columns_images5
        self.columns_date = columns_date

    def __repr__(self):
        return '<Title %r>' % self.columns_title


class ideas(Base):
    __tablename__ = 'Idea'
    idea_id = Column(Integer, primary_key=True)
    idea_username = Column(String(128), unique=False)  # ユーザー名項目
    idea_title = Column(Text(30))  # アイデアタイトル
    idea_discription = Column(Text(300))  # 詳細説明
    idea_image1 = Column(Text)  # 画像データ
    idea_image2 = Column(Text)  # 画像データ
    idea_good = Column(Integer, unique=False)  # 貰ったいいね数
    idea_date = Column(DateTime, default=datetime.now())  # 投稿日時

    def __init__(self, idea_username=None, idea_title=None, idea_discription=None, idea_image1=None, idea_image2=None,
                 idea_good=None, idea_date=None):
        self.idea_username = idea_username
        self.idea_title = idea_title
        self.idea_discription = idea_discription
        self.idea_image1 = idea_image1
        self.idea_image2 = idea_image2  # 画像データ
        self.idea_good = idea_good
        self.idea_date = idea_date

    def __repr__(self):
        return '<Title1 %r>' % self.idea_title
