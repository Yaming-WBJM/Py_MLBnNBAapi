import json
from NBA_http import *
from Orihttp import Ori_Response
#from commonplayerinfo import CommonPlayerInfo
#from commonallplayers import CommonAllPlayers
from commonallplayers import CommonAllPlayers

#print("Hello Python.")

#player_info = CommonPlayerInfo(player_id=2544)201939
#with open('D:\\test.json', 'w') as fp:
#    json.dump(player_info.common_player_info.get_json(), fp)
#    print(player_info.player_headline_stats.get_json())
    
#all_players = CommonAllPlayers()
#with open('D:\\all_players.json', 'w') as fp:
#    json.dump(all_players.common_all_players.get_json(), fp)game_id='0021701218'
#    print(all_players.common_all_players.get_json())

player_info = CommonAllPlayers()
#print(player_info.video_status.get_json())
with open('D:\\NBA_Players.json', 'w') as fp:
    json.dump(player_info.common_all_players.get_dict(), fp)
