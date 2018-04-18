import sys
from gevent.wsgi import WSGIServer
import flask
import os
import io
from slow_motion import settings


app = flask.Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def hello():
    return flask.render_template('hello.html')


@app.route('/picture.jpg')
def image():
    if sys.platform == 'win32':
        strIO = io.BytesIO(settings.img_buffer)
        return flask.send_file(
            strIO,
            attachment_filename="picture.jpg",
            as_attachment=True)
    strIO = io.BytesIO(settings.img_buffer)
    return flask.send_file(
        strIO,
        attachment_filename="picture.png",
        as_attachment=True)


def main():
    port = 8080
    print("start server on port:%s" % (port, ))
    http_server = WSGIServer(('', port), app)
    http_server.serve_forever()


if __name__ == '__main__':
    main()
