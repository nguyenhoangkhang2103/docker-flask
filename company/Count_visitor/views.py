# Count_visitor/Views.py
from flask import render_template,request,Blueprint
import time, redis

views = Blueprint("views", __name__)
cache = redis.Redis(host='redis-server', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@views.route("/count")
def count_visitors():
    count = get_hit_count()
    return render_template("count.html",count=count)
