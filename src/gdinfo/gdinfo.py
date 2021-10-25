# GDInfo by @kelptaken
# This script is using GNU General Public License v3.0; see the LICENSE file for details. 

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
    levelFeatured = levelInfo[0]['featured']
    levelEpic = levelInfo[0]['epic']

    print()
    print('Имя: ' + levelName)
    print('ID: ' + levelId)
    print('Описание: ' + levelDesc)
    print('Создатель: ' + levelCreator)
    print('Сложность: ' + levelDifficulty)
    if levelFeatured == True:
        print('Featured - есть')
    elif levelFeatured == False:
        print('Featured - нет')
    else:
        print('levelFeatured: недостоверный ответ от сервера.')
    
    if levelEpic == True:
        print('Epic - есть')
    elif levelEpic == False:
        print('Epic - нет')
    else:
        print('levelEpic: недостоверный ответ от сервера.')
    print('Скачиваний: ' + str(levelDownloads))
    print('Лайков: ' + str(levelLikes))
    print('Длительность: ' + levelLength)
    print('Музыка: ' + levelSongAuthor + ' - ' + levelSongName)
    print('ID музыки: ' + str(levelSongID))
    print('Музыка на Newgrounds: https://www.newgrounds.com/audio/listen/' + str(levelSongID))
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

def levelSearchDebug():
    print('!!! ВКЛЮЧЕН РЕЖИМ РАЗРАБОТЧИКА !!!')
    levelInput = input('Введите название уровня или ID: ')
    levelJson = r.get('https://gdbrowser.com/api/search/' + levelInput + '?count=1')
    levelInfo = json.loads(levelJson.text)

    print()
    print('Request sent to: https://gdbrowser.com/api/search/' + levelInput + '?count=1')
    print('API response:')
    print(levelJson.text)
    print()
    print('Converted to dict:')
    print(levelInfo)

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
    levelFeatured = levelInfo[0]['featured']
    levelEpic = levelInfo[0]['epic']

    print()
    print('In vars:')
    print('levelName: ' + levelName)
    print('levelId: ' + levelId)
    print('levelDesc: ' + levelDesc)
    print('levelCreator: ' + levelCreator)
    print('levelDifficulty: ' + levelDifficulty)
    print('levelDownloads: ' + str(levelDownloads))
    print('levelLikes: ' + str(levelLikes))
    print('levelLength: ' + levelLength)
    print('levelMusic: ' + levelSongAuthor + ' - ' + levelSongName)
    print('levelSongID: ' + str(levelSongID))
    print('levelMusicNG: https://www.newgrounds.com/audio/listen/' + str(levelSongID))
    if levelObjects == 0:
        print('levelObjects = 0')
    else:
        print(str(levelObjects) + ' objects')
    
    if levelFeatured == True:
        print('levelFeatured: True')
    elif levelFeatured == False:
        print('levelFeatured: False')
    else:
        print('wrong_response')
    
    if levelEpic == True:
        print('levelEpic: True')
    elif levelEpic == False:
        print('levelEpic: False')
    else:
        print('wrong_response')
    print()

def accountSearchDebug():
    print('!!! ВКЛЮЧЕН РЕЖИМ РАЗРАБОТЧИКА !!!')
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
    print('Request sent to https://gdbrowser.com/api/profile/' + accountInput)
    print('API response:')
    print(accountJson.text)
    print()
    print('Converted to dict:')
    print(accountInfo)

    print()
    print('In vars:')
    print('accountName: ' + accountName)
    print('accountId: ' + str(accountId))
    print('accountPlayerID: ' + str(accountPlayerID))
    print('accountStars: ' + str(accountStars))
    print('accountDiamonds: ' + str(accountDiamonds))
    print('accountOffCoins: ' + str(accountOffCoins))
    print('accountUserCoins: ' + str(accountUserCoins))
    print('accountDemons: ' + str(accountDemons))
    print('accountCP: ' + str(accountCP))
    if accountIsModerator == 0:
        print('accountIsModerator = 0')
    elif accountIsModerator == 1:
        print('accountIsModerator = 1')
    elif accountIsModerator == 2:
        print('accountIsModerator = 2')
    else:
        print('wrong_response')
    
    print()
    
    print('security: ')
    if accountFriendRequests == True:
        print('accountFriendRequests = True')
    else:
        print('accountFriendRequests = False')
    
    if accountMessages == 'all':
        print('accountMessages = all')
    elif accountMessages == 'friends':
        print('accountMessages = friends')
    elif accountMessages == 'off':
        print('accountMessages = off')
    else:
        print('wrong_response')
    
    if accountCommentHistory == 'all':
        print('accountCommentHistory = all')
    elif accountCommentHistory == 'friends':
        print('accountCommentHistory = friends')
    elif accountCommentHistory == 'off':
        print('accountCommentHistory = off')
    else:
        print('wrong_response')
        
    print()
    
    print('social:')
    if accountYouTube != 'None':
        print('accountYouTube: ' + accountYouTube)
    else:
        print('accountYouTube: None')
    if accountTwitter != 'None':
        print('accountTwitter: ' + accountTwitter)
    else:
        print('accountTwitter: None')
    if accountTwitch != 'None':
        print('accountTwitch: ' + accountTwitch)
    else:
        print('accountTwitch: None')
    print()

def accountIconDL():
    iconDlInput = input(str('Введите имя аккаунта, с которого взять иконку: '))
    print('Выберите тип иконки:')
    print('1. cube')
    print('2. ship')
    print('3. ball')
    print('4. ufo')
    print('5. wave')
    print('6. robot')
    print('7. spider')
    iconDlTypeInput = input(str('Тип иконки: '))
    url = 'https://gdbrowser.com/icon/' + iconDlInput

    if iconDlTypeInput == '1':
        iconDlResult = r.get(url + '?form=cube')
        open(iconDlInput + '_' + iconDlTypeInput + '.png', 'wb').write(iconDlResult.content)
        print('Успешно!')
    elif iconDlTypeInput == '2':
        iconDlResult = r.get(url + '?form=ship')
        open(iconDlInput + '_' + iconDlTypeInput + '.png', 'wb').write(iconDlResult.content)
        print('Успешно!')
    elif iconDlTypeInput == '3':
        iconDlResult = r.get(url + '?form=ball')
        open(iconDlInput + '_' + iconDlTypeInput + '.png', 'wb').write(iconDlResult.content)
        print('Успешно!')
    elif iconDlTypeInput == '4':
        iconDlResult = r.get(url + '?form=ufo')
        open(iconDlInput + '_' + iconDlTypeInput + '.png', 'wb').write(iconDlResult.content)
        print('Успешно!')
    elif iconDlTypeInput == '5':
        iconDlResult = r.get(url + '?form=wave')
        open(iconDlInput + '_' + iconDlTypeInput + '.png', 'wb').write(iconDlResult.content)
        print('Успешно!')
    elif iconDlTypeInput == '6':
        iconDlResult = r.get(url + '?form=robot')
        open(iconDlInput + '_' + iconDlTypeInput + '.png', 'wb').write(iconDlResult.content)
        print('Успешно!')
    elif iconDlTypeInput == '7':
        iconDlResult = r.get(url + '?form=spider')
        open(iconDlInput + '_' + iconDlTypeInput + '.png', 'wb').write(iconDlResult.content)
        print('Успешно!')


print('GDInfo, v1.4')
print('Доступные опции:')
print('1. вывести информацию об уровне')
print('2. вывести информацию о пользователе')
print('3. экспортировать информацию об уровне в JSON-файл')
print('4. экспортировать информацию об аккаунте в JSON-файл')
print('5. вывести информацию об уровне (режим разработчика)')
print('6. вывести информацию о пользователе (режим разработчика)')
print('7. скачать иконку пользователя')

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
    elif choiceInput == '5':
        levelSearchDebug()
    elif choiceInput == '6':
        accountSearchDebug()
    elif choiceInput == '7':
        accountIconDL()
    else:
        print('Неверный ответ!') 
