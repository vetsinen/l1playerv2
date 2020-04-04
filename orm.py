import pathlib
from os import listdir, rename
import sqlite3


DATABASE = str(pathlib.Path(__file__).parent.absolute()) + '/opinion'

def del_specific_symbols(str: str):
    return str.replace("'"," ").replace('"',' ').replace('`',' ')

def sync_trackfiles_to_db():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = f"update opinion set active = 0"
    cursor.execute(sql)
    db.commit()

    genres = {'sal': 'salsa casino', 'bac': 'bachata', 'kim': 'urban kiz', 'men': 'merengue'}
    staticpath = str(pathlib.Path(__file__).parent.absolute()) + '/static/mp3/'
    files = [f for f in listdir(staticpath)]
    for origfile in files:
        file = del_specific_symbols(origfile)
        rename(staticpath+origfile,staticpath+file)
        start = (file[:3])
        genre = ''
        if file[4] == 'a' and start in genres.keys():
            genre = genres[start]
        sql = f"insert into opinion (genre, trackname, active) values ('{genre}','{file[:-4]}',1);"
        try:
            cursor.execute(sql)
            db.commit()
        except BaseException:
            sql = f"update opinion set active=1 where trackname ='{file[:-4]}'"
            print(sql)
            cursor.execute(sql)
            # seems record was inserted before
    db.close()


def get_tracks():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    rez = [list(row) for row in cursor.execute("SELECT trackname,genre,velocity,votes FROM opinion WHERE active=1")]
    return rez


def save_opinion(track, genre, velocity):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = f"update opinion set genre = '{genre}', velocity = '{velocity}' where trackname = '{track}'"
    try:
        cursor.execute(sql)
        db.commit()
    except BaseException:
        pass

    db.close()


def save_vote(track):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = f"update opinion set votes = votes+1 where trackname = '{track}'"
    cursor.execute(sql)
    db.commit()
    db.close()

def cleardb():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = f"delete from option "
    cursor.execute(sql)
    db.commit()
    db.close()


if __name__ == '__main__':
    sync_trackfiles_to_db()
