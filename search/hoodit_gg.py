from .Riot_api import Riot_api
from lolalarm.static.json_updater import get_json







class api_info(object):
      

      def __init__(self, api_key):
            self.api = Riot_api(api_key)


      def profile_search_by_name(self, name):
            self.profile_info = self.api.get_summoner_by_name(name)
            return self.profile_info

       # **kwargs form => champion / queue / season / beginIndex / endIndex
      def matchlist(self, account_id, **kwargs):
            return self.api.get_matchlist(account_id, kwargs)


      def spectator(self, summoner_id):
            return self.api.spectator(summoner_id)


      def league(self, summoner_id):
            return self.api.league(summoner_id)


      def match_id(self, match_id):
            match_data, status = self.api.match(match_id)
            # id = 100 = blue / id = 200 = red
            blue_team = []
            red_team = []
            name_list = []
            
            participants_info = match_data['participantIdentities']
            for index in match_data['participantIdentities']:
                  name_list.append(index['player']['summonerName'])
            n = 0
            for index in match_data["participants"]:
                  team_id = index['teamId']
                  dump_dict = {'name': name_list[n],
                               'teamId': team_id,
                               'championId': index['championId'],
                               'spell1Id': index['spell1Id'],
                               'spell2Id': index['spell2Id'],
                               'kills': index['stats']['kills'],
                               'deaths': index['stats']['deaths'],
                               'assists': index['stats']['assists']
                               }
                  if team_id == 100:
                        blue_team.append(dump_dict)
                  else:
                        red_team.append(dump_dict)
                  n += 1
            team_num = match_data['teams'][0]['teamId']
            team_win = match_data['teams'][0]['win']
            if team_win == 'Win':
                  if team_num == 100:
                        win_team = 'blue'
                  else:
                        win_team = 'red'
            else:
                   if team_num == 100:
                        win_team = 'red'
                   else:
                        win_team = 'blue'
            print(blue_team)
            print(red_team)
            print(win_team)
            #import json
            #with open('match_data_example.json', 'w', encoding="utf-8") as outfile:
            #json.dump(match_data, outfile, indent=4)
            return blue_team, red_team, win_team


      def match_timeline(self, match_id):
            timeline, status = self.api.match_timeline(match_id)
            #import json
            #with open('match_timeline_example.json', 'w', encoding="utf-8") as outfile:
            #json.dump(timeline, outfile, indent=4)


            return
            





if __name__ == "__main__":
      test = api_info('RGAPI-839b8944-a432-4339-8f35-50e8017267c7')
      asyncio.run(test.match_timeline('4749579464'))

