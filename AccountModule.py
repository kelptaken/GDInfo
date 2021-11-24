# AccountModule by @kelptaken
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


def RetrieveAccountInfo(Account):
    print(bold + '[RetrieveAccountInfo] ' + r_color + debug_info + 'Getting data from server...')
    AccountInfo_jsonResponse = r.get('https://gdbrowser.com/api/profile/' + Account)
    print(bold + '[RetrieveAccountInfo] ' + r_color + debug_info + 'Parsing...')
    AccountInfo_dict = json.loads(AccountInfo_jsonResponse.text)

    print(bold + '[RetrieveAccountInfo] ' + r_color + debug_info + 'Defining namespace...')
    AccountInfo = Namespace(**AccountInfo_dict)
    print(bold + '[RetrieveAccountInfo] ' + r_color + debug_info + 'Giving info to main script...')
    return AccountInfo



def AccountIconDL(Account, Type):
    url = 'https://gdbrowser.com/icon/' + Account

    if Type == '1':
        AccountIconDL_Response = r.get(url + '?form=cube')
        AccountIconDL_Icon = AccountIconDL_Response.content
        return AccountIconDL_Icon
    
    elif Type == '2':
        AccountIconDL_Response = r.get(url + '?form=ship')
        AccountIconDL_Icon = AccountIconDL_Response.content
        return AccountIconDL_Icon
    
    elif Type == '3':
        AccountIconDL_Response = r.get(url + '?form=ball')
        AccountIconDL_Icon = AccountIconDL_Response.content
        return AccountIconDL_Icon
    
    elif Type == '4':
        AccountIconDL_Response = r.get(url + '?form=ufo')
        AccountIconDL_Icon = AccountIconDL_Response.content
        return AccountIconDL_Icon
    
    elif Type == '5':
        AccountIconDL_Response = r.get(url + '?form=wave')
        AccountIconDL_Icon = AccountIconDL_Response.content
        return AccountIconDL_Icon
    
    elif Type == '6':
        AccountIconDL_Response = r.get(url + '?form=robot')
        AccountIconDL_Icon = AccountIconDL_Response.content
        return AccountIconDL_Icon

    elif Type == '7':
        AccountIconDL_Response = r.get(url + '?form=spider')
        AccountIconDL_Icon = AccountIconDL_Response.content
        return AccountIconDL_Icon



def AccountExportJson(Account):
    AccountExportJson_Response = r.get('https://gdbrowser.com/api/profile/' + Account)
    AccountExportJson_ResponseContent = AccountExportJson_Response.text

    return AccountExportJson_ResponseContent
