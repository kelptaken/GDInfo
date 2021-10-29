import requests as r
import json

def LevelInfo(Level):
    LevelInfo_jsonResponse = r.get('https://gdbrowser.com/api/search/' + Level + '?count=1')
    LevelInfo_dict = json.loads(LevelInfo_jsonResponse.text)

    # Native variables
    # P. S. dict entries that contain numbers are automatically converted to str for easy concatenating
    LevelInfo_Name = LevelInfo_dict[0]['name']
    LevelInfo_ID = str(LevelInfo_dict[0]['id'])
    LevelInfo_Description = LevelInfo_dict[0]['description']
    LevelInfo_Creator = LevelInfo_dict[0]['author']
    LevelInfo_Difficulty = LevelInfo_dict[0]['difficulty']
    LevelInfo_Downloads = str(LevelInfo_dict[0]['downloads'])
    LevelInfo_Likes = str(LevelInfo_dict[0]['likes'])
    LevelInfo_Length = LevelInfo_dict[0]['length']
    LevelInfo_SongID = str(LevelInfo_dict[0]['customSong'])
    LevelInfo_SongCreator = LevelInfo_dict[0]['songAuthor']
    LevelInfo_SongName = LevelInfo_dict[0]['songName']
    LevelInfo_Objects = str(LevelInfo_dict[0]['objects'])
    LevelInfo_isFeatured = LevelInfo_dict[0]['featured']
    LevelInfo_isEpic = LevelInfo_dict[0]['epic']

    # Custom variables
    LevelInfo_Song = (LevelInfo_SongCreator + ' - ' + LevelInfo_SongName)
    LevelInfo_SongNewgroundsLink = ('https://www.newgrounds.com/audio/listen/' + LevelInfo_SongID)
    
    return LevelInfo_jsonResponse, LevelInfo_dict, LevelInfo_Name, LevelInfo_ID, LevelInfo_Description, LevelInfo_Creator, LevelInfo_Difficulty, LevelInfo_Downloads, LevelInfo_Likes, LevelInfo_Length, LevelInfo_SongID, LevelInfo_SongCreator, LevelInfo_SongName, LevelInfo_Objects, LevelInfo_isFeatured, LevelInfo_isEpic, LevelInfo_Song, LevelInfo_SongNewgroundsLink