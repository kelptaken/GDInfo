import requests as r
import json

def LevelExportJson(Level):
    LevelExportJson_Response = r.get('https://gdbrowser.com/api/search/' + Level + '?count=1')
    LevelExportJson_ResponseContent = LevelExportJson_Response.text

    return LevelExportJson_ResponseContent

def AccountExportJson(Account):
    AccountExportJson_Response = r.get('https://gdbrowser.com/api/profile/' + Account)
    AccountExportJson_ResponseContent = AccountExportJson_Response.text

    return AccountExportJson_ResponseContent