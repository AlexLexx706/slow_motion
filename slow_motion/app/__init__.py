import sys
from gevent.wsgi import WSGIServer
import flask
import os
import io
from slow_motion import settings


app = flask.Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
settings.req_count = 0


@app.route("/")
def hello():
    try:
        return flask.render_template('hello.html', count=settings.req_count)
    finally:
        settings.req_count += 1


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


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


def main():
    port = 8080
    print("start server on port:%s" % (port, ))
    http_server = WSGIServer(('', port), app)
    http_server.serve_forever()


if __name__ == '__main__':
    main()
