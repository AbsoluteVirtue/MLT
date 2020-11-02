import json
# import os
#
# entries = os.scandir("data/")


def composers_data():

    with open("data/composers.json", "r", encoding='utf-8') as fp:
        ret = json.load(fp)

    return ret
