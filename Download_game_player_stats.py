import psycopg2
import json
from NBA_http import *
from Orihttp import Ori_Response
from boxscoretraditionalv2 import BoxScoreTraditionalV2
import os
import time

conn = psycopg2.connect(database="sportge", user="postgres", password="4Rfv7ujm", host="127.0.0.1", port="5432")
print ("Opened database successfully")
cur = conn.cursor()

cur.execute("SELECT game_id from nba_games")
rows = cur.fetchall()
for row in rows:
    if not (os.path.isfile('D:\\Sport_JSON\\NBA\\Game_player_stats\\'+str(row[0]).strip()+'.json')):
        game_info = BoxScoreTraditionalV2(game_id=str(row[0]).strip())
        with open('D:\\Sport_JSON\\NBA\\Game_player_stats\\'+str(row[0]).strip()+'.json', 'w') as fp:
            json.dump(game_info.player_stats.get_dict(), fp)
        time.sleep(0.1)

print ("Operation done successfully")
conn.close()