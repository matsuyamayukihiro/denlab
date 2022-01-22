from models.database import db_session
from models.models import ideas, columns, User

c1 = User("コラムテスト", "名前", "説明文", "https://redcat-denlabo.s3.ap-northeast-1.amazonaws.com/%E3%82%B3%E3%83%A9%E3%83%A0%EF%BC%91%EF%BC%88%E8%B6%8A%E5%89%8D%E5%92%8C%E7%B4%99+x+%E5%AE%87%E5%AE%99%EF%BC%89+(0).jpg", "https://redcat-denlabo.s3.ap-northeast-1.amazonaws.com/%E3%82%B3%E3%83%A9%E3%83%A0%EF%BC%91%EF%BC%88%E8%B6%8A%E5%89%8D%E5%92%8C%E7%B4%99+x+%E5%AE%87%E5%AE%99%EF%BC%89+(0).jpg", "https://redcat-denlabo.s3.ap-northeast-1.amazonaws.com/%E3%82%B3%E3%83%A9%E3%83%A0%EF%BC%91%EF%BC%88%E8%B6%8A%E5%89%8D%E5%92%8C%E7%B4%99+x+%E5%AE%87%E5%AE%99%EF%BC%89+(0).jpg" ,"https://redcat-denlabo.s3.ap-northeast-1.amazonaws.com/%E3%82%B3%E3%83%A9%E3%83%A0%EF%BC%91%EF%BC%88%E8%B6%8A%E5%89%8D%E5%92%8C%E7%B4%99+x+%E5%AE%87%E5%AE%99%EF%BC%89+(0).jpg", "https://redcat-denlabo.s3.ap-northeast-1.amazonaws.com/%E3%82%B3%E3%83%A9%E3%83%A0%EF%BC%91%EF%BC%88%E8%B6%8A%E5%89%8D%E5%92%8C%E7%B4%99+x+%E5%AE%87%E5%AE%99%EF%BC%89+(0).jpg")
db_session.add(c1)
db_session.commit()
db_session.close()
print("完了")
