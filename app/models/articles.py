"""
記事モデル
"""
from app.models.abstract import AbstractModel


class ArticleModel(AbstractModel):
    def __init__(self, config):
        super(ArticleModel, self).__init__(config)

    def fetch_recent_articles(self, limit=5):
        """
        最新の記事を取得する．デフォルトでは最新5件まで
        :param limit: 取得する記事の数
        :return:
        """
        sql = "SELECT * FROM articles ORDER BY created_at DESC LIMIT %s"
        return self.fetch_all(sql, limit)

    def fetch_article_by_id(self, article_id):
        """
        指定されたIDの記事を取得
        :param article_id: 取得したい記事のID
        :return: 指定された記事のID
        """
        sql = "SELECT * FROM articles INNER JOIN users u on articles.user_id = u.id WHERE articles.id=%s"
        return self.fetch_one(sql, article_id)

    # def create_article(self, user_id, title, body):
    #     """
    #     新しく記事を作成する
    #     :param user_id: 投稿したユーザのOD
    #     :param title: 記事のタイトル
    #     :param body: 記事の本文
    #     :return: None
    #     """
    #     sql = "INSERT INTO articles(user_id, title, body) VALUE (%s, %s, %s);"
    #     self.execute(sql, user_id, title, body)

    def search_music(self, user_id, feeling, time):
        """
        新しく記事を作成する
        :param user_id: 投稿したユーザのOD
        :param title: 記事のタイトル
        :param body: 記事の本文
        :return: None
        """
        sql = "INSERT INTO p_articles(user_id, feeling, time) VALUE (%s, %s, %s);"
        self.execute(sql, user_id, feeling, time)

    def in_music(self, user_id, music_title, artist, feeling, time, recommend, spotify_url):
        """
        新しく記事を作成する
        :param user_id: 投稿したユーザのOD
        :param music_title: 曲名
        :param artist: アーティスト名
        :param feeling: 感情
        :param time: 時間
        :param recommend: おすすめ理由
        :param music_url: spotifyの楽曲URL
        :return: None
        """
        sql = "INSERT INTO articles(user_id, music_title, artist, feeling, time, recommend, spotify_url) VALUE (%s, %s, %s, %s, %s, %s, %s);"
        self.execute(sql, user_id, music_title, artist, feeling, time, recommend, spotify_url)

    def recommend_music(self, feeling, time):
        """
        おすすめの楽曲を探す
        :param user_id: 投稿したユーザのOD
        :param feeling: 感情
        :param time: 時間
        :return: None
        """
        sql = "SELECT * FROM articles WHERE feeling=%s AND time=%s ORDER BY RAND() LIMIT 1;"
        return self.fetch_one(sql, feeling, time)
