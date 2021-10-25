import requests as r
import json

def levelInfo(level):
    levelJson = r.get('https://gdbrowser.com/api/search/' + level + '?count=1')
    levelInfo = json.loads(levelJson.text)

    return (levelInfo[0]['name'], levelInfo[0]['id'], levelInfo[0]['description'], levelInfo[0]['author'], levelInfo[0]['difficulty'], levelInfo[0]['downloads'], levelInfo[0]['likes'], levelInfo[0]['length'], levelInfo[0]['customSong'], levelInfo[0]['songAuthor'], levelInfo[0]['songName'], levelInfo[0]['objects'], levelInfo[0]['featured'], levelInfo[0]['epic'])