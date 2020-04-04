from flask import Flask
from flask import render_template
from orm import get_tracks, save_opinion, save_vote
from random import randrange

app = Flask(__name__)


def process_names(files):
    rez = []
    for f in files:
        a = f
        a = a[:-4]
        # if (a[4:7]) == 'a-v':
        rez.append(a)
    return rez


@app.route('/')
def index():
    backimg = '/static/backgrounds/back'+str(randrange(6)).zfill(2)+'.jpg'
    print(backimg)
    return render_template('index.html', tracks=get_tracks(),backimg=backimg)


@app.route('/opinion/<track>/<genre>', methods=['POST'])
def opinion(track, genre):
    velocity = 'normal'
    msg = f"track {track} is a {genre} with {velocity} velocity"
    print(msg)
    save_opinion(track, genre, velocity)
    return msg

@app.route('/vote/<track>', methods=['POST'])
def vote(track):
    save_vote(track)
    return 'voted'

if __name__ == '__main__':
    app.run()
