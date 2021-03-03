import requests
import json
import re
import URLcont
import os






def save_as_json(data, path): #help to save file as json
      with open(path + '.json', 'w', encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4)



def ddragon_version():
      dict_data = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json
      version_dict['version'] = dict_data[0]
      save_as_json(version_dict, 'ddragon_version')
      print('update data dragon done')



def champion_list(): #this is data of all champion list(simple info attach too)      this form is data: champion_id all of champion_id is english only

      #this data include/ champion_id / name / story / simple info

      #champion info list as korean
      #new version, it didnt return english version
      json_dict = requests.get(
            URLcont.URL['champion_list'].format(
                  region=URLcont.REGION['korea'],
                  version=ddragon_version
                  )
            ).json()
      
            
      save_as_json(json_dict, 'champion_list') #champion list always return korean info / if you want add another region check URLcont
      print('export champion info data done')
      





def queues(): #queue data as json
      json_dict = requests.get(
            URLcont.URL['queues']
            ).json()

      queues_dict = {}
      
      for index in json_dict:
            queues_dict[index['queueId']] = {'map': index['map'], 'description': index['description']}

      save_as_json(json_dict, 'queue')
      print('export queues data done')
      


def seasons(): #season data as json
      json_dict = requests.get(
            URLcont.URL['seasons']
            ).json()

      seasons_dict = {}

      for index in json_dict:
            seasons_dict[index['id']] = {'season': index['season']}

      save_as_json(seasons_dict, 'seasons_data')
      print('export seasons data done')


#this func will be use to for
def champion_data(champion_id): #use champion_id, get all info of champion (ex. champion_stats / skill / skin info e.t.c.)
      try:
            champion_req = requests.get(
                  URLcont.URL['champion_data'].format(
                        version=ddragon_version,
                        region=URLcont.REGION['korea'],
                        champion_id=champion_id
                        )
                  )     
            champion_data = champion_req.json()
      except:
            print(champion_id, 'has problem, code -', champion_data.status_code)
      else:
            save_as_json(champion_data, './champion_data_list/' + champion_id)
            print(champion_id, 'import sucess')
      

def get_champion_data_list():

      champion_list = requests.get(
            URLcont.URL['champion_list'].format(
                  version=ddragon_version,
                  region=URLcont.REGION['korea']                  
                  )
            ).json()['data']

      for index in champion_list.keys():
            champion_data(champion_list[index]['id'])
            
      print('each champion data import done')



#it have champion id and champion kor name, champion eng name
def champion_num_data():

      
      eng_data = requests.get(
            URLcont.URL['champion_list'].format(
                  region=URLcont.REGION['us'],
                  version=ddragon_version
                  )
            ).json()['data']

      kor_data = requests.get(
            URLcont.URL['champion_list'].format(
                  region=URLcont.REGION['korea'],
                  version=ddragon_version
                  )
            ).json()['data']

      champion_id_list = list(eng_data.keys())


      champion_id_dict = {}
      
      for index in champion_id_list:
            champion_id_dict[eng_data[index]['key']] = {'id':index, 'eng':eng_data[index]['name'], 'kor':kor_data[index]['name']}
            # this data form => {key: {id:value, eng:value, kor: value}}
            
      save_as_json(champion_id_dict, 'champion_num_data')


def champion_skin():
      list_dir = os.listdir('./champion_data_list')

      skin_dict = {}
      
      for index in list_dir:
            with open('./champion_data_list/' + index) as json_file:
                  champion_id = index.split('.')[0]
                  json_data = json.load(json_file)
                  champion_skin_list = json_data['data'][champion_id]['skins']
                  skin_dict[champion_id] = champion_skin_list

      save_as_json(skin_dict, 'champion_skin')
      print(champion skins info export done)
                  
                  







if __name__ == '__main__':
      ddragon_version = json.load(open('ddragon_version.json', 'r'))['version']
      print('data dragon version -', ddragon_version)
      champion_skin()
