from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import hoodit_gg
from lolalarm.static import json_updater, IMGcont


# Create your views here.

API_KEY = 'RGAPI-2c21b396-b148-40d8-8891-cd86764b6853'

def index(request):
    return render(request, 'search/index.html', {"sample":"sample"})


def info(request, user_name):
    
    json_conv = json_updater.get_json()
    ddragon_version = json_conv.version['version']
    
    search_tool = hoodit_gg.api_info(API_KEY)
    
    profile, status= search_tool.profile_search_by_name(user_name)
    print(profile)
    if status == 404:
        return HttpResponse("찾으시는 소환사 이름이 없습니다.")
    
    elif status != 200:
        return HttpResponse("Error - {}".format(status))
    
    else:
        
        summoner_id = profile['id']
        summoner_level = profile['summonerLevel']
        icon_id = profile['profileIconId']
        account_id = profile['accountId']
        
        icon_url = IMGcont.URL['profile_icon'].format(
            version=ddragon_version,
            IconId=icon_id
            )
        
        profile_league, status = search_tool.league(summoner_id)
        
        profile_solorank_info = None
        profile_flexrank_info = None

        if len(profile_league) == 2:
            if profile_league[0]['queueType'] == 'RANKED_SOLO_5x5':  
                profile_solorank_info, profile_flexrank_info = profile_league
            else:
                profile_flexrank_info, profile_solorank_info = profile_league
                        
        elif len(profile_league) == 1:
            if profile_league[0]['queueType'] == 'RANKED_SOLO_5x5':
                profile_solorank_info = profile_league[0]
            else:
                profile_flexrank_info = profile_league[0]
        
        solo_rank_tier = None
        flex_rank_tier = None
        
        if profile_solorank_info != None:
            solo_rank_tier = profile_solorank_info["tier"]
        if profile_flexrank_info != None:
            flex_rank_tier = profile_flexrank_info["tier"]
           
        contents = {
            "summoner_name": user_name,
            "summoner_level": summoner_level,
            "profile_icon": icon_url,
            "solo_rank_tier": solo_rank_tier,
            "flex_rank_tier": flex_rank_tier           
        }
        
        return render(request, 'search/info.html', contents)
        