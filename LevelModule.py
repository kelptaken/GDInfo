# LevelModule by @kelptaken
# This script is using GNU General Public License v3.0; see the LICENSE
# file for details.
# This script is also a part of GDInfo (https://github.com/kelptaken/GDInfo)


import requests as r
import json
from colorama import init, Fore, Style
from argparse import Namespace


# Define some handy vars
dim = Style.DIM
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
bold = Style.BRIGHT
r_style = Style.RESET_ALL
r_color = Fore.RESET
debug_success = bold + green + '[·] ' + r_color + r_style
debug_info = bold + blue + '[·] ' + r_color + r_style
debug_fail = bold + red + '[!] ' + r_color + r_style
info_true = green + '☑ ' + r_color
info_false = red + '✕ ' + r_color


def RetrieveLevelInfo(Level):
    # fetch level id (/api/level needs only id)
    print(bold + '[RetrieveLevelInfo] ' + r_color + debug_info + 'Preparing [1/3]...')
    Temp_jsonResponse = r.get('https://gdbrowser.com/api/search/' + Level + '?count=1')
    print(bold + '[RetrieveLevelInfo] ' + r_color + debug_info + 'Preparing [2/3]...')
    Temp_dict = json.loads(Temp_jsonResponse.text)
    print(bold + '[RetrieveLevelInfo] ' + r_color + debug_info + 'Preparing [3/3]...')
    Temp_levelID = str(Temp_dict[0]['id'])

    print(bold + '[RetrieveLevelInfo] ' + r_color + debug_info + 'Getting data from server...')
    LevelInfo_jsonResponse = r.get('https://gdbrowser.com/api/level/' + Temp_levelID)
    print(bold + '[RetrieveLevelInfo] ' + r_color + debug_info + 'Parsing...')
    LevelInfo_dict = json.loads(LevelInfo_jsonResponse.text)
    print(bold + '[RetrieveLevelInfo] ' + r_color + debug_info + 'Defining namespace...')
    LevelInfo = Namespace(**LevelInfo_dict)
    print(bold + '[RetrieveLevelInfo] ' + r_color + debug_info + 'Giving info to main script...')
    return LevelInfo

def LevelExportJson(Level):
    Temp_jsonResponse = r.get('https://gdbrowser.com/api/search/' + Level + '?count=1')
    Temp_dict = json.loads(Temp_jsonResponse.text)
    Temp_levelID = str(Temp_dict[0]['id'])

    LevelInfo_jsonResponse = r.get('https://gdbrowser.com/api/level/' + Temp_levelID)
    LevelExportJson_ResponseContent = LevelInfo_jsonResponse.text

    return LevelExportJson_ResponseContent
