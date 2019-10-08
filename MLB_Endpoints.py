from _base import Endpoint
from MLB_http import MLBStatsHTTP
#from parameters import EndPeriod, StartPeriod


class Conferences(Endpoint):
    endpoint = 'conferences'
    def __init__(self,
                 conference_Id,
                 Season):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'conferenceId': conference_Id,
                'season': Season
            },
        )
        self.data_sets = self.mlb_response

class People(Endpoint):
    endpoint = 'people'
    def __init__(self,
                 person_Ids):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'personIds': person_Ids
            },
        )
        self.data_sets = self.mlb_response
        
class GameStatus(Endpoint):
    endpoint = 'gameStatus'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class BaseballStats(Endpoint):
    endpoint = 'baseballStats'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class GameTypes(Endpoint):
    endpoint = 'gameTypes'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class Languages(Endpoint):
    endpoint = 'languages'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class LeagueLeaderTypes(Endpoint):
    endpoint = 'leagueLeaderTypes'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class Metrics(Endpoint):
    endpoint = 'metrics'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class Platforms(Endpoint):
    endpoint = 'platforms'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class Positions(Endpoint):
    endpoint = 'positions'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class RosterTypes(Endpoint):
    endpoint = 'rosterTypes'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class ScheduleEventTypes(Endpoint):
    endpoint = 'scheduleEventTypes'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class SituationCodes(Endpoint):
    endpoint = 'situationCodes'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class StandingsTypes(Endpoint):
    endpoint = 'standingsTypes'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class StatGroups(Endpoint):
    endpoint = 'statGroups'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class StatTypes(Endpoint):
    endpoint = 'statTypes'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class Draft(Endpoint):
    endpoint = 'draft/2018'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class HomeRunDerby(Endpoint):
    endpoint = 'homeRunDerby/511101'
    def __init__(self):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={                
            },
        )
        self.data_sets = self.mlb_response
        
class League(Endpoint):
    endpoint = 'league'
    def __init__(self,
                 sport_Id):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={ 
                'sportId': sport_Id               
            },
        )
        self.data_sets = self.mlb_response
        
class Schedule(Endpoint):
    endpoint = 'schedule'
    def __init__(self,
                 sport_Id,
                 gamedate):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={ 
                'sportId': sport_Id,
                'date': gamedate                
            },
        )
        self.data_sets = self.mlb_response
        
class Seasons(Endpoint):
    endpoint = 'seasons'
    def __init__(self,
                 sport_Id):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={ 
                'sportId': sport_Id              
            },
        )
        self.data_sets = self.mlb_response
        
class Sports(Endpoint):
    endpoint = 'sports/1/players'
    def __init__(self,
                 Season):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={ 
                'season': Season             
            },
        )
        self.data_sets = self.mlb_response
        
class Standings(Endpoint):
    endpoint = 'standings'
    def __init__(self,
                 league_Id,
                 Season):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'leagueId': league_Id,
                'season': Season
            },
        )
        self.data_sets = self.mlb_response
        
class Teams(Endpoint):
    endpoint = 'teams'
    def __init__(self,
                 team_Id):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint+'/'+str(team_Id),
            parameters={
            },
        )
        self.data_sets = self.mlb_response
        
class Game(Endpoint):
    endpoint = 'game'
    def __init__(self,
                 game_pk):
        self.mlb_response = MLBStatsHTTP().send_api_request(
            endpoint=self.endpoint+'/'+str(game_pk)+'/boxscore',
            parameters={
            },
        )
        self.data_sets = self.mlb_response