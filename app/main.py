from flask import Flask
from redis import Redis

redisDB = Redis(host='redis-db', port=6379)

app = Flask(__name__)

@app.route("/")
def hello_world():
    redisDB.incr('count')
    count = str(redisDB.get('count'), encoding='utf-8')
    return f"<p>Hello, World! {count}</p>"