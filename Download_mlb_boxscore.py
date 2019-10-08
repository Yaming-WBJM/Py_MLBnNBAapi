import psycopg2
import json
from MLB_Endpoints import *
from Orihttp import Ori_Response
import os
import time

conn = psycopg2.connect(database="sportge", user="postgres", password="4Rfv7ujm", host="127.0.0.1", port="5432")
print ("Opened database successfully")
cur = conn.cursor()

cur.execute("SELECT game_id from mlb_games")
rows = cur.fetchall()
for row in rows:
    if not (os.path.isfile('D:\\Sport_JSON\\MLB\\Boxscore\\'+str(row[0])+'.json')):
        game_info = Game(game_pk=row[0])
        with open('D:\\Sport_JSON\\MLB\\Boxscore\\'+str(row[0])+'.json', 'w') as fp:
            json.dump(game_info.data_sets.get_dict(), fp)
        time.sleep(0.1)

print ("Operation done successfully")
conn.close()