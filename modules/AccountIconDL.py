import requests as r
import json

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