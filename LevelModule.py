# LevelModule by @kelptaken
# This script is using GNU General Public License v3.0; see the LICENSE
# file for details.
# This script is also a part of GDInfo (https://github.com/kelptaken/GDInfo)


import requests as r
import json
from argparse import Namespace


def RetrieveLevelInfo(Level):
    try:
        # fetch level id (/api/level needs only id)
        Temp_jsonResponse = r.get('https://gdbrowser.com/api/search/' + Level + '?count=1')
        Temp_dict = json.loads(Temp_jsonResponse.text)
        Temp_levelID = str(Temp_dict[0]['id'])

        LevelInfo_jsonResponse = r.get('https://gdbrowser.com/api/level/' + Temp_levelID)
        LevelInfo_dict = json.loads(LevelInfo_jsonResponse.text)
        LevelInfo = Namespace(**LevelInfo_dict)
        return LevelInfo
    except BaseException:
        exit('Uh oh! RetrieveLevelInfo() caught an error. Is the level name valid?')  # ERROR7
    except KeyboardInterrupt:
        exit('\nBye!')


def LevelExportJson(Level):
    try:
        Temp_jsonResponse = r.get('https://gdbrowser.com/api/search/' + Level + '?count=1')
        Temp_dict = json.loads(Temp_jsonResponse.text)
        Temp_levelID = str(Temp_dict[0]['id'])

        LevelInfo_jsonResponse = r.get('https://gdbrowser.com/api/level/' + Temp_levelID)
        LevelExportJson_ResponseContent = LevelInfo_jsonResponse.text

        return LevelExportJson_ResponseContent
    except BaseException:
        exit('Uh oh! LevelExportJson() caught an error. Is the level name valid?')  # ERROR8
    except KeyboardInterrupt:
        exit('\nBye!')
