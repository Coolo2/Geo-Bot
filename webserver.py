import flask
from threading import Thread
import os
import discord
import json

def webserver_run(client):
    t = Thread(target=run)
    t.start()
    global bot 
    bot = client

app = flask.Flask('', template_folder=os.path.abspath('./webserver/HTML'))
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["TEMPLATES_AUTO_RELOAD"] = True

async def replyTo(bot : discord.Bot, channelId : int, messageId : int, content : str = None, embed : discord.Embed = None):
    channel = bot.get_channel(channelId)
    message = await channel.fetch_message(messageId)

    await message.reply(content=content, embed=embed)

@app.route('/flags/<path:filename>')
def custom_image(filename):
    return flask.send_from_directory('resources/flags/', filename)

@app.route('/')
def home():
    return flask.render_template('index.html', last_updated=dir_last_updated('/static'))

@app.route('/reply/<path:channelId>/<path:messageId>')
def reply(channelId, messageId):
    args = flask.request.args.to_dict()

    content = args["content"] if "content" in args else None
    embed = None

    if "embed" in args:
        
        embedData = json.loads(args["embed"])
        embed = discord.Embed.from_dict(embedData)

    bot.loop.create_task(replyTo(bot, int(channelId), int(messageId), content, embed))
    return "hi"

def dir_last_updated(folder):
    try:
        return str(max(os.path.getmtime(os.path.join(root_path, f)) for root_path, dirs, files in os.walk(folder) for f in files))
    except:
        return 0

def run():

    app.run(host='0.0.0.0', port=5000) 
