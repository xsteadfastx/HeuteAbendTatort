#from __future__ import unicode_literals
import datetime
import cPickle as pickle
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from tatort_fundus import Episode, naechste_wiederholungen, tatort_today


def air_today():
    today = datetime.date.today().isoformat()
    if os.path.exists(today+'.p'):
        temp_file = open(today+'.p', 'rb')
        today_list = pickle.load(temp_file)
    else:
        today_list = []
        temp_file = open(today+'.p', 'wb+')
        for i in tatort_today():
            episode = Episode(i[4].encode('utf8'))
            i = list(i)
            i.append(episode.summary)
            today_list.append(i)
        pickle.dump(today_list, temp_file)

    temp_file.close()
    return today_list


app = Flask(__name__)
Bootstrap(app)
    
@app.route('/')
def home():
    episodes = air_today()
    return render_template('index.html', episodes = episodes)


#if __name__ == '__main__':
#    create_app().run(debug=True)
