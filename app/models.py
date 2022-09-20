from datetime import datetime
from app import db, ma
import requests


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String)
    tag = db.Column(db.String, nullable=False)
    resume = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False, default='default.jpeg')
    en_notion_id = db.Column(db.String, nullable=False)
    en_notion = db.Column(db.String)
    ar_notion_id = db.Column(db.String, nullable=False,
                             default='Not available')
    ar_notion = db.Column(db.String)
    ar_darija_notion_id = db.Column(
        db.String, nullable=False, default='Not available')
    darija_notion = db.Column(db.String)
    date_posted = db.Column(db.Date, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self):
        return f"Blog('{self.header}', '{self.tag}' , '{self.resume}')"


class BlogsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Blog


def FetchNotionApi(notio_id):
    if notio_id:
        url_api = f'https://notion-api.splitbee.io/v1/page/{notio_id}'
        req = requests.get(url_api)
        return req.content
    else:
        return 'No data !'
