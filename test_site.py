import datetime, os
from bottle import route, run, template, static_file, error

BASE_DIR = os.path.dirname(__file__) + os.path.sep
test_site_host = os.environ['test_site_host'] or 'localhost'
test_site_port = os.environ['test_site_port'] or 8080

@route('/')
def index():
    message = test_site_host
    now_time = datetime.datetime.now()
    cur_hour = now_time.hour
    return template('index',
                    cur_hour=cur_hour,
                    msg=message)

@route('/static/<filename>')
def server_static(filename):
    static_dir = BASE_DIR + 'static'
    return static_file(filename,
                       root=static_dir)

@route('/images/<filename>')
def server_static_dir(filename):
    img_dir = BASE_DIR + 'images'
    return static_file(filename,
                       root=img_dir,
                       mimetype='image/jpg')

@error(404)
@error(403)
def mistake(code):
    return 'Error on page'

if __name__ == "__main__":
   run(host=test_site_host, port=test_site_port, debug=True)