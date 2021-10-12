import requests as r 
import json
aboba = 'bebra'

def levelSearch():
    levelInput = input('Введите название уровня или ID: ')
    levelJson = r.get('https://gdbrowser.com/api/search/' + levelInput + '?count=1')
    levelInfo = json.loads(levelJson.text)

    levelName = levelInfo[0]['name']
    levelId = levelInfo[0]['id']
    levelDesc = levelInfo[0]['description']
    levelCreator = levelInfo[0]['author']
    levelDifficulty = levelInfo[0]['difficulty']
    levelDownloads = levelInfo[0]['downloads']
    levelLikes = levelInfo[0]['likes']
    levelLength = levelInfo[0]['length']
    levelSongID = levelInfo[0]['customSong']
    levelSongAuthor = levelInfo[0]['songAuthor']
    levelSongName = levelInfo[0]['songName']
    levelObjects = levelInfo[0]['objects']

    print()
    print('Имя: ' + levelName)
    print('ID: ' + levelId)
    print('Описание: ' + levelDesc)
    print('Создатель: ' + levelCreator)
    print('Сложность: ' + levelDifficulty)
    print('Скачиваний: ' + str(levelDownloads))
    print('Лайков: ' + str(levelLikes))
    print('Длительность: ' + levelLength)
    print('Музыка: ' + levelSongAuthor + ' - ' + levelSongName)
    print('ID музыки: ' + str(levelSongID))
    if levelObjects == 0:
        print('Объектов: неизвестно, копирование уровня ограничено')
    else:
        print('Объектов: ' + str(levelObjects))
    print()

def accountSearch():
    accountInput = input('Введите имя аккаунта или ID: ')
    accountJson = r.get('https://gdbrowser.com/api/profile/' + accountInput)
    accountInfo = json.loads(accountJson.text)
    
    accountName = accountInfo['username']
    accountId = accountInfo['accountID']
    accountPlayerID = accountInfo['playerID']
    accountStars = accountInfo['stars']
    accountDiamonds = accountInfo['diamonds']
    accountOffCoins = accountInfo['coins']
    accountUserCoins = accountInfo['userCoins']
    accountDemons = accountInfo['demons']
    accountCP = accountInfo['cp']
    accountFriendRequests = accountInfo['friendRequests']
    accountMessages = accountInfo['messages']
    accountCommentHistory = accountInfo['commentHistory']
    accountIsModerator = accountInfo['moderator']
    accountYouTube = str(accountInfo['youtube'])
    accountTwitter = str(accountInfo['twitter'])
    accountTwitch = str(accountInfo['twitch'])

    print()
    print('Имя: ' + accountName)
    print('ID аккаунта: ' + str(accountId))
    print('ID игрока: ' + str(accountPlayerID))
    print('Звёзд: ' + str(accountStars))
    print('Алмазов: ' + str(accountDiamonds))
    print('Оф. монеток: ' + str(accountOffCoins))
    print('Польз. монеток: ' + str(accountUserCoins))
    print('Демонов: ' + str(accountDemons))
    print('КП: ' + str(accountCP))
    if accountIsModerator == 0:
        print('Аккаунт не является модератором.')
    elif accountIsModerator == 1:
        print('Аккаунт является обычным модератором. ')
    elif accountIsModerator == 2:
        print('Аккаунт является старшим модератором. ')
    else:
        print('moderator: Недостоверный ответ от сервера. ')
    
    print()
    
    print('Приватность: ')
    if accountFriendRequests == True:
        print('Пользователь разрешил добавлять себя в друзья.')
    else:
        print('Пользователь запретил добавлять себя в друзья.')
    
    if accountMessages == 'all':
        print('Пользователь разрешил писать ему сообщения всем.')
    elif accountMessages == 'friends':
        print('Пользователь разрешил писать ему сообщения только друзьям.')
    elif accountMessages == 'off':
        print('Пользователь запретил писать ему сообщения.')
    else:
        print('accountMessages: Недостоверный ответ от сервера.')
    
    if accountCommentHistory == 'all':
        print('Пользователь разрешил всем смотреть историю комментариев.')
    elif accountCommentHistory == 'friends':
        print('Пользователь разрешил смотреть историю комментариев только друзьям.')
    elif accountCommentHistory == 'off':
        print('Пользователь запретил смотреть историю комментариев.')
    else:
        print('accountCommentHistory: Недостоверный ответ от сервера.')
        
    print()
    
    print('Соцсети:')
    if accountYouTube != 'None':
        print('YouTube: https://youtube.com/channel/' + accountYouTube)
    else:
        print('К аккаунту не привязан YouTube.')
    if accountTwitter != 'None':
        print('Twitter: https://twitter.com/' + accountTwitter)
    else:
        print('К аккаунту не привязан Twitter.')
    if accountTwitch != 'None':
        print('Twitch: https://twitch.tv/' + accountTwitch)
    else:
        print('К аккаунту не привязан Twitch.')
    print()

def levelExportJson():
    levelExportJsonInput = input('Выберите уровень: ')
    levelExportJsonGet = r.get('https://gdbrowser.com/api/search/' + levelExportJsonInput + '?count=1')
    levelExportJsonFile = open(levelExportJsonInput + '.json', 'w')
    levelExportJsonFile.write(levelExportJsonGet.text)
    levelExportJsonFile.close()
    print('Успешно!')

def accountExportJson():
    accountExportJsonInput = input('Выберите аккаунт: ')
    accountExportJsonGet = r.get('https://gdbrowser.com/api/profile/' + accountExportJsonInput)
    accountExportJsonFile = open(accountExportJsonInput + '.json', 'w')
    accountExportJsonFile.write(accountExportJsonGet.text)
    accountExportJsonFile.close()
    print('Успешно!')

print('GDInfo, v. 1.0')
print('Доступные опции:')
print('1. вывести информацию об уровне')
print('2. вывести информацию о пользователе')
print('3. экспортировать информацию об уровне в JSON-файл')
print('4. экспортировать информацию об аккаунте в JSON-файл')

while aboba == 'bebra':
    choiceInput = input('> ')
    if choiceInput == '1':
        levelSearch()
    elif choiceInput == '2':
        accountSearch()
    elif choiceInput == '3':
        levelExportJson()
    elif choiceInput == '4':
        accountExportJson()
    else:
        print('Неверный ответ!')