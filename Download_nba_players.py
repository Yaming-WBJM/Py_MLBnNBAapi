import psycopg2
import json
from NBA_http import *
from Orihttp import Ori_Response
from commonplayerinfo import CommonPlayerInfo
import os
import time

conn = psycopg2.connect(database="sportge", user="postgres", password="4Rfv7ujm", host="127.0.0.1", port="5432")
print ("Opened database successfully")
cur = conn.cursor()

cur.execute("SELECT player_id from nba_players")
rows = cur.fetchall()
for row in rows:
    if not (os.path.isfile('D:\\Sport_JSON\\NBA\\Players\\'+str(row[0])+'.json')):
        player_info = CommonPlayerInfo(player_id=row[0])
        with open('D:\\Sport_JSON\\NBA\\Players\\'+str(row[0])+'.json', 'w') as fp:
            json.dump(player_info.common_player_info.get_dict(), fp)
            
        time.sleep(1)

print ("Operation done successfully")
conn.close()