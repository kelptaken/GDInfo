import requests as r
import json
import levelInfo

levelName, levelID, levelDescription, levelCreator, levelDifficulty, levelDownloads, levelLikes, levelLength, levelSongID, levelSongAuthor, levelSongName, levelObjects, levelFeatured, levelEpic = levelInfo.levelInfo('bloodbath')
print(levelName)
print(levelID)