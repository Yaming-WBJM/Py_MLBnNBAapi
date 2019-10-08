from _base import Endpoint
from MLB_http import MLBStatsHTTP
#from parameters import EndPeriod, StartPeriod


class People(Endpoint):
    endpoint = 'people'
    #expected_data = {'AvailableVideo': ['VIDEO_AVAILABLE_FLAG'], 'PlayByPlay': ['GAME_ID', 'EVENTNUM', 'EVENTMSGTYPE', 'EVENTMSGACTIONTYPE', 'PERIOD', 'WCTIMESTRING', 'PCTIMESTRING', 'HOMEDESCRIPTION', 'NEUTRALDESCRIPTION', 'VISITORDESCRIPTION', 'SCORE', 'SCOREMARGIN', 'PERSON1TYPE', 'PLAYER1_ID', 'PLAYER1_NAME', 'PLAYER1_TEAM_ID', 'PLAYER1_TEAM_CITY', 'PLAYER1_TEAM_NICKNAME', 'PLAYER1_TEAM_ABBREVIATION', 'PERSON2TYPE', 'PLAYER2_ID', 'PLAYER2_NAME', 'PLAYER2_TEAM_ID', 'PLAYER2_TEAM_CITY', 'PLAYER2_TEAM_NICKNAME', 'PLAYER2_TEAM_ABBREVIATION', 'PERSON3TYPE', 'PLAYER3_ID', 'PLAYER3_NAME', 'PLAYER3_TEAM_ID', 'PLAYER3_TEAM_CITY', 'PLAYER3_TEAM_NICKNAME', 'PLAYER3_TEAM_ABBREVIATION']}

    def __init__(self,
                 person_Ids):
                 #start_period=StartPeriod.default):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'personIds': person_Ids,
            },
        )
        self.data_sets = self.mlb_response
