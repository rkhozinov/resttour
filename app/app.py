from flask import Flask
from redis import Redis
from config import Config as cfg

app = Flask(__name__)
app.config.from_object(cfg)

redis = Redis(host=cfg.DB_HOST,
              port=cfg.DB_PORT)

@app.route('/', methods=['GET', 'POST'])
def hellos_count():
  redis.incr('hellos')
  return 'hellos count {}'.format(redis.get('hellos'))

if __name__ == "__main__":
  app.run(debug=cfg.DEBUG)
