from puppycompanyblog import db
from puppycompanyblog.models import User,BlogPost
db.create_all()
db.session.commit()

