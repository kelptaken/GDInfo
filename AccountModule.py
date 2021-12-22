# AccountModule by @kelptaken
# This script is using GNU General Public License v3.0; see the LICENSE
# file for details.
# This script is also a part of GDInfo (https://github.com/kelptaken/GDInfo)


import requests as r
import json
from argparse import Namespace



def RetrieveAccountInfo(Account):
    try:
        AccountInfo_jsonResponse = r.get('https://gdbrowser.com/api/profile/' + Account)
        AccountInfo_dict = json.loads(AccountInfo_jsonResponse.text)

        AccountInfo = Namespace(**AccountInfo_dict)
        return AccountInfo
    except BaseException:
        print('Uh oh! RetrieveAccountInfo() caught an error. Is the level name valid?')
        exit() # ERROR9



def AccountIconDL(Account, Type):
    url = 'https://gdbrowser.com/icon/' + Account

    try:
        match Type:
            case '1':
                AccountIconDL_Response = r.get(url + '?form=cube')
                AccountIconDL_Icon = AccountIconDL_Response.content
                return AccountIconDL_Icon
            case '2':
                AccountIconDL_Response = r.get(url + '?form=ship')
                AccountIconDL_Icon = AccountIconDL_Response.content
                return AccountIconDL_Icon

            case '3':
                AccountIconDL_Response = r.get(url + '?form=ball')
                AccountIconDL_Icon = AccountIconDL_Response.content
                return AccountIconDL_Icon
    
            case '4':
                AccountIconDL_Response = r.get(url + '?form=ufo')
                AccountIconDL_Icon = AccountIconDL_Response.content
                return AccountIconDL_Icon
    
            case '5':
                AccountIconDL_Response = r.get(url + '?form=wave')
                AccountIconDL_Icon = AccountIconDL_Response.content
                return AccountIconDL_Icon
    
            case '6':
                AccountIconDL_Response = r.get(url + '?form=robot')
                AccountIconDL_Icon = AccountIconDL_Response.content
                return AccountIconDL_Icon

            case '7':
                AccountIconDL_Response = r.get(url + '?form=spider')
                AccountIconDL_Icon = AccountIconDL_Response.content
                return AccountIconDL_Icon
    except BaseException:
        print("Looks like your Python version is 3.9 or below. Please install Python 3.10")
        exit()
        



def AccountExportJson(Account):
    AccountExportJson_Response = r.get('https://gdbrowser.com/api/profile/' + Account)
    AccountExportJson_ResponseContent = AccountExportJson_Response.text

    return AccountExportJson_ResponseContent
