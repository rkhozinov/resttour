from flask import Flask, render_template, request, redirect, url_for
from redis import Redis
from config import Config as cfg

app = Flask(__name__)
app.config.from_object(cfg)

redis = Redis(host=cfg.DB_HOST,
              port=cfg.DB_PORT)


@app.route('/', methods=['GET', 'POST'])
def hellos_count():
    if request.method == 'POST':
        redis.incr('hellos')
        return redirect(url_for('hellos_count'))

    return render_template('index.html',
                           hellos_count=int(redis.get('hellos')))


if __name__ == "__main__":
    app.run(debug=cfg.DEBUG)
