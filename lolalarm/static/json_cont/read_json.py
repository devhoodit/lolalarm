import json
import re


def open_and_read(path):
      data = json.load(open(path, 'r', encoding='utf-8'))
      string = json.dumps(data, ensure_ascii=False, indent=4)
      print(string)


if __name__ == "__main__":
      while True:
            file_path = input('path? - ')
            try:
                  open_and_read(file_path) 
            except:
                  print('read error, wrong path')
