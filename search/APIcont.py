URL = {
      'base': 'https://{proxy}.api.riotgames.com/lol/{url}',
      'summoner_by_name': 'summoner/v{version}/summoners/by-name/{names}',
      'matchlsit_by_encryptedAccountid': 'match/v{version}/matchlists/by-account/{encryptedAccountid}',
      'spectator': 'spectator/v{version}/active-games/by-summoner/{encryptedSummonerId}',
      'league': 'league/v{version}/entries/by-summoner/{encryptedSummonerId}',
      'match': 'match/v{version}/matches/{matchId}',
      'match_timeline': 'match/v{version}/timelines/by-match/{matchId}'
}

API_VERSIONS = {
      'summoner': '4',
      'match': '4',
      'spectator': '4',
      'league': '4'
}

REGIONS = {
      'korea': 'kr'
}
