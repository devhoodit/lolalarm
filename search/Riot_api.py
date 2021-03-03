from . import APIcont

import json
import requests


class Riot_api(object):

      def __init__(self, api_key, region=APIcont.REGIONS['korea']):
            self.api_key = api_key
            self.region = region


      def  _request(self, api_url, params={}):
            args = {}
            for key, value in params.items():
                  if key not in args:
                        args[key] = value
            args['api_key'] = self.api_key
            header = {'X-Riot_token': self.api_key}
            
            
            
            response = requests.get(
                  APIcont.URL['base'].format(
                        proxy=self.region,
                        url=api_url
                        ),
                  params=args,
                  headers=header
                  )
            
            data, status = response.json(), response.status_code
            return data, status


      def get_summoner_by_name(self, name):
            api_url = APIcont.URL['summoner_by_name'].format(
                  version=APIcont.API_VERSIONS['summoner'],
                  names=name
                  )
            return self._request(api_url)




      # **kwargs form => champion / queue / season / beginIndex / endIndex
      def get_matchlist(self, account_id, kwargs):
            api_url = APIcont.URL['matchlsit_by_encryptedAccountid'].format(
                  version=APIcont.API_VERSIONS['match'],
                  encryptedAccountid=account_id
                  )
            
            return self._request(api_url, kwargs)

      def spectator(self, summoner_id):
            api_url = APIcont.URL['spectator'].format(
                  version=APIcont.API_VERSIONS['spectator'],
                  encryptedSummonerId=summoner_id
                  )
            return self._request(api_url)

      def league(self, summoner_id):
            api_url = APIcont.URL['league'].format(
                  version=APIcont.API_VERSIONS['league'],
                  encryptedSummonerId=summoner_id
                  )
            return self._request(api_url)

      def match(self, match_id):
            api_url = APIcont.URL['match'].format(
                  version=APIcont.API_VERSIONS['match'],
                  matchId=match_id
                  )
            return self._request(api_url)

      def match_timeline(self, match_id):
            api_url = APIcont.URL['match_timeline'].format(
                  version=APIcont.API_VERSIONS['match'],
                  matchId=match_id
                  )
            return self._request(api_url)
            


if __name__ == "__main__":
      test = Riot_api('')
      dump = asyncio.run(test.match('4749579464'))
      dump_list = list(dump)
      for index in dump_list:
            print(index)








      
