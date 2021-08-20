from sqlalchemy import create_engine #データとの接続情報をコントロール
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
#データベースファイルの構築 DBエンジン搭載
databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'onegai.db') #database.pyと同じパスにonegai.dbというファイルを絶対パス(os.path.abspath)で定義
engine = create_engine('sqlite:///' + databese_file, convert_unicode=True)#databese_fileDB構築
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))#DB接続の仕方の構築
Base = declarative_base()#データベース基盤作成
Base.query = db_session.query_property()#そこにDBの情報を流し込む


def init_db():
    import models.models
    Base.metadata.create_all(bind=engine)#データベース初期化
