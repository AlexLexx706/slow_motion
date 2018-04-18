from gevent.wsgi import WSGIServer
import flask
import os
from slow_motion import settings


app = flask.Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def hello():
    global counter
    return flask.render_template('hello.html', counter=counter)


@app.route('/picture.jpg')
def image():
    return flask.send_from_directory(*os.path.split(settings.out_file))


def main():
    port = 8080
    print("start server on port:%s" % (port, ))
    http_server = WSGIServer(('', port), app)
    http_server.serve_forever()


if __name__ == '__main__':
    main()
