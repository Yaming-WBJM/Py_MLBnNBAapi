import psycopg2
import json
from NBA_http import *
from Orihttp import Ori_Response
from teamdetails import TeamDetails
import os
import time

conn = psycopg2.connect(database="sportge", user="postgres", password="4Rfv7ujm", host="127.0.0.1", port="5432")
print ("Opened database successfully")
cur = conn.cursor()

cur.execute("SELECT team_id from nba_teams")
rows = cur.fetchall()
for row in rows:
    if not (os.path.isfile('D:\\Sport_JSON\\NBA\\Teams\\'+str(row[0])+'.json')):
        team_info = TeamDetails(team_id=row[0])
        with open('D:\\Sport_JSON\\NBA\\Teams\\'+str(row[0])+'.json', 'w') as fp:
            json.dump(team_info.team_background.get_dict(), fp)
        time.sleep(1)

print ("Operation done successfully")
conn.close()