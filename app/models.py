from datetime import datetime
from app import db,ma

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String)
    tag = db.Column(db.String, nullable=False)
    resume = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False, default='default.jpeg')
    en_notion_id = db.Column(db.String, nullable=False)
    ar_notion_id = db.Column(db.String, nullable=False,
                             default='Not available')
    ar_darija_notion_id = db.Column(
        db.String, nullable=False, default='Not available')
    date_posted = db.Column(db.Date, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self):
        return f"Blog('{self.header}', '{self.tag}' , '{self.resume}')"


class BlogsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Blog