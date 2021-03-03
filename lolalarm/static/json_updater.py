import json
import random

class get_json(object):
      def __init__(self):
            with open('./json_cont/ddragon_version.json', 'r') as json_file:
                  self.version = json.load(json_file)

      def champion_num_data(self, num):
            with open('./json_cont/champion_num_data.json', 'r') as json_file:
                  jf = json.load(json_file)
            return jf[str(num)]

      def champion_skin(self, champion_id):
            with open('./json_cont/champion_skin.json', 'r') as json_file:
                  jf = json.load(json_file)
            return jf[champion_id]

      def random_champion(self):
            with open('./json_cont/champion_num_data.json' ,'r') as json_file:
                  champion_dict = json.load(json_file)
                  champion_key = str(random.sample(list(champion_dict.keys()), 1)[0])
                  champion_name, champion_id = champion_dict[champion_key]['kor'], champion_dict[champion_key]['id']
                  champion_skin_list = self.champion_skin(champion_id)
                  dump_rand = random.sample(champion_skin_list, 1)[0]
                  champion_skin_name, champion_skin_key = dump_rand['name'], dump_rand['num']
                  return champion_name, champion_skin_name, champion_id, champion_skin_key

                  





if __name__ == '__main__':
      test = get_json()
      test.random_champion()
