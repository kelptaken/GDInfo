import requests as r
import json

def LevelInfo(Level):
    LevelInfo_jsonResponse = r.get('https://gdbrowser.com/api/search/' + Level + '?count=1')
    LevelInfo_dict = json.loads(LevelInfo_jsonResponse.text)

    # Native variables
    # P. S. dict entries that contain numbers are automatically converted to str for easy concatenating
    LevelInfo_Name = str(LevelInfo_dict[0]['name'])
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


def LevelInfoAdvanced(Level):
    # fetch level id (/api/level needs only id)
    Temp_jsonResponse = r.get('https://gdbrowser.com/api/search/' + Level + '?count=1')
    Temp_dict = json.loads(Temp_jsonResponse.text)
    Temp_levelID = str(Temp_dict[0]['id'])

    LevelInfo_jsonResponse = r.get('https://gdbrowser.com/api/level/' + Temp_levelID)
    LevelInfo_dict = json.loads(LevelInfo_jsonResponse.text)

    # Native variables
    # P. S. dict entries that contain numbers are automatically converted to str for easy concatenating
    LevelInfo_Name = str(LevelInfo_dict['name'])
    LevelInfo_ID = str(LevelInfo_dict['id'])
    LevelInfo_Stars = str(LevelInfo_dict['stars'])
    LevelInfo_RequestedStars = str(LevelInfo_dict['starsRequested'])
    LevelInfo_Orbs = str(LevelInfo_dict['orbs'])
    LevelInfo_Diamonds = str(LevelInfo_dict['diamonds'])
    LevelInfo_Description = LevelInfo_dict['description']
    LevelInfo_Creator = LevelInfo_dict['author']
    LevelInfo_GameVersion = LevelInfo_dict['gameVersion']
    LevelInfo_LevelVersion = str(LevelInfo_dict['version'])
    LevelInfo_Difficulty = LevelInfo_dict['difficulty']
    if LevelInfo_Difficulty == 'Extreme Demon':
        LevelInfo_DemonListPosition = str(LevelInfo_dict['demonList'])
    else:
        LevelInfo_DemonListPosition = 'N/A'
    LevelInfo_Downloads = str(LevelInfo_dict['downloads'])
    LevelInfo_Likes = str(LevelInfo_dict['likes'])
    LevelInfo_Coins = str(LevelInfo_dict['coins'])
    LevelInfo_verifiedCoins = LevelInfo_dict['verifiedCoins']
    LevelInfo_Length = LevelInfo_dict['length']
    
    LevelInfo_SongID = str(LevelInfo_dict['customSong'])

    # Check if the level song is official to prevent exception
    if LevelInfo_SongID == '0':
        LevelInfo_SongCreator = LevelInfo_dict['songAuthor']
        LevelInfo_SongName = LevelInfo_dict['songName']
        LevelInfo_SongSize = 'N/A'
        LevelInfo_SongRawLink = 'N/A'
        LevelInfo_SongNewgroundsLink = 'N/A'
    else:
        LevelInfo_SongCreator = LevelInfo_dict['songAuthor']
        LevelInfo_SongName = LevelInfo_dict['songName']
        LevelInfo_SongSize = LevelInfo_dict['songSize']
        LevelInfo_SongRawLink = LevelInfo_dict['songLink']
        LevelInfo_SongNewgroundsLink = 'https://newgrounds.com/audio/listen/' + LevelInfo_SongID

    if LevelInfo_dict['objects'] == 0:
        LevelInfo_Objects = 'unknown, level copying may be locked'
    else:
        LevelInfo_Objects = str(LevelInfo_dict['objects'])
    LevelInfo_isLarge = LevelInfo_dict['large']
    LevelInfo_isFeatured = LevelInfo_dict['featured']
    LevelInfo_isEpic = LevelInfo_dict['epic']

    # Custom variables
    LevelInfo_Song = (LevelInfo_SongCreator + ' - ' + LevelInfo_SongName)

    
    return LevelInfo_jsonResponse, LevelInfo_dict, LevelInfo_Name, LevelInfo_ID, LevelInfo_Stars, LevelInfo_RequestedStars, LevelInfo_Orbs, LevelInfo_Diamonds, LevelInfo_GameVersion, LevelInfo_LevelVersion, LevelInfo_Description, LevelInfo_Creator, LevelInfo_Difficulty, LevelInfo_DemonListPosition, LevelInfo_Downloads, LevelInfo_Likes, LevelInfo_Coins, LevelInfo_verifiedCoins, LevelInfo_Length, LevelInfo_SongID, LevelInfo_SongCreator, LevelInfo_SongName, LevelInfo_SongSize, LevelInfo_SongRawLink, LevelInfo_Objects, LevelInfo_isLarge, LevelInfo_isFeatured, LevelInfo_isEpic, LevelInfo_Song, LevelInfo_SongNewgroundsLink


def LevelExportJson(Level):
    LevelExportJson_Response = r.get('https://gdbrowser.com/api/search/' + Level + '?count=1')
    LevelExportJson_ResponseContent = LevelExportJson_Response.text

    return LevelExportJson_ResponseContent
