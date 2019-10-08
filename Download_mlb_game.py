import psycopg2
import json
from MLB_Endpoints import *
from Orihttp import Ori_Response
import os
import time
from datetime import datetime, timedelta

for x in range(2700,2900):
    dl_date=datetime.today() - timedelta(days=x)
    if not (os.path.isfile('D:\\Sport_JSON\\MLB\\Games\\'+dl_date.strftime('%Y%m%d')+'.json')):
        game_info = Schedule(sport_Id=1,gamedate=dl_date.strftime('%Y-%m-%d'))
        with open('D:\\Sport_JSON\\MLB\\Games\\'+dl_date.strftime('%Y%m%d')+'.json', 'w') as fp:
            json.dump(game_info.data_sets.get_dict(), fp)
            time.sleep(0.1)

print ("Operation done successfully")