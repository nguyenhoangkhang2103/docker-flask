# Company/__init__.py
from flask import Flask

app = Flask(__name__)

from company.core.views import core # blueprint
from company.Count_visitor.views import views # blueprint
app.register_blueprint(core)
app.register_blueprint(views)
