import json
from NBA_http import *
from Orihttp import Ori_Response
from scoreboardv2 import ScoreboardV2
import os
from datetime import datetime, timedelta
import time

for x in range(1,3000):
    dl_date=datetime.today() - timedelta(days=x)
    if not (os.path.isfile('D:\\Sport_JSON\\NBA\\Games\\'+dl_date.strftime('%Y%m%d')+'.json')):
        game_info = ScoreboardV2(game_date=dl_date)
        with open('D:\\Sport_JSON\\NBA\\Games\\'+dl_date.strftime('%Y%m%d')+'.json', 'w') as fp:
            json.dump(game_info.game_header.get_dict(), fp)
            time.sleep(0.1)

print ("Operation done successfully")
