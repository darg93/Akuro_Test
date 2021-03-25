import json
from datetime import datetime
from datetime import timedelta

def get_json_file():

    with open('punto2.entrada.json') as file:
        info=json.load(file)
    
    return info

def main(info):

    date_str = info["date"]
    date_int = datetime.strptime(date_str,'%Y-%m-%d') + timedelta(days=22)
    print (date_int)


if __name__ == "__main__":
    
    info=get_json_file()
    main(info)