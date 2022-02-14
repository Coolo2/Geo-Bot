import flask
from threading import Thread
import os

def webserver_run(client):
    t = Thread(target=run)
    t.start()
    global bot 
    bot = client

app = flask.Flask('', template_folder=os.path.abspath('./webserver/HTML'))
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/flags/<path:filename>')
def custom_image(filename):
    return flask.send_from_directory('resources/flags/', filename)

@app.route('/')
def home():
    return flask.render_template('index.html', last_updated=dir_last_updated('/static'))

def dir_last_updated(folder):
    try:
        return str(max(os.path.getmtime(os.path.join(root_path, f)) for root_path, dirs, files in os.walk(folder) for f in files))
    except:
        return 0

def run():

    app.run(host='0.0.0.0', port=5000) 
