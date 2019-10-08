from Orihttp import Ori_Response
from MLB_Endpoints import *
import json

#print("Hello Python.")

#player_info = Conferences(conference_Id=302,Season='2018')
player_info = Sports(Season='2011')
#print(player_info.data_sets.get_json())
with open('D:\\MLB_Players2011.json', 'w') as fp:
    json.dump(player_info.data_sets.get_dict(), fp)