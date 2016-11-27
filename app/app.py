from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port='6379')

@app.route('/', methods=['GET', 'POST'])
def hellos_count():
  redis.incr('hellos')
  return 'hellos count {}'.format(redis.get('hellos'))

if __name__ == "__main__":
  app.run(debug=True)
