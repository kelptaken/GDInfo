# GDInfo by @kelptaken
# This script is using GNU General Public License v3.0; see the LICENSE
# file for details.

import requests as r
import json
from colorama import init, Fore, Style

# Define some handy color vars
dim = Style.DIM
red = Fore.RED
green = Fore.GREEN
bold = Style.BRIGHT
r_style = Style.RESET_ALL
r_color = Fore.RESET

# Show level info
def LevelInfo(Level):
    LevelInfo_jsonResponse = r.get(
        'https://gdbrowser.com/api/search/' + Level + '?count=1')
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


    # Show the info
    print()
    print(bold + 'Name: ' + r_style + LevelInfo_Name)
    print(bold +'ID: ' + r_style + LevelInfo_ID)
    print(bold + 'Description: ' + r_style + LevelInfo_Description)
    print(bold + 'Creator: ' + r_style + LevelInfo_Creator)
    print(bold + 'Difficulty: ' + r_style + LevelInfo_Difficulty)
    if LevelInfo_isFeatured == True:
        print(green + '☑ ' + r_color + bold + 'Featured: ' + r_style + 'true')
    elif LevelInfo_isFeatured == False:
        print(red + '✕ ' + r_color + bold + 'Featured: ' + r_style + 'false')
    else:
        print(bold + 'Featured: ' + r_style + 'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')

    if LevelInfo_isEpic == True:
        print(green + '☑ ' + r_color + bold + 'Epic: ' + r_style + 'true')
    elif LevelInfo_isEpic == False:
        print(red + '✕ ' + r_color + bold + 'Epic: ' + r_style + 'false')
    else:
        print(bold + 'Epic: ' + r_style + 'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')
    
    print(bold + 'Downloads: ' + r_style + LevelInfo_Downloads)
    print(bold + 'Likes: ' + r_style + LevelInfo_Likes)
    print(bold + 'Length: ' + r_style + LevelInfo_Length)
    print(bold + 'Song: ' + r_style + LevelInfo_Song)
    print(bold +'Song ID:  ' + r_style + LevelInfo_SongID)
    print(bold + 'Song on Newgrounds: ' + r_style + LevelInfo_SongNewgroundsLink)
    
    if LevelInfo_Objects == '0':
        print(bold + 'Objects: ' + r_style + 'unknown, level copying may be locked')
    else:
        print(bold + 'Objects: ' + r_style + LevelInfo_Objects)
    print()


def AccountInfo(Account):
    AccountInfo_jsonResponse = r.get('https://gdbrowser.com/api/profile/' + accountInput)
    AccountInfo_dict = json.loads(AccountInfo_jsonResponse.text)

    AccountInfo_Name = AccountInfo_dict['username']
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
    levelExportJsonGet = r.get(
        'https://gdbrowser.com/api/search/' +
        levelExportJsonInput +
        '?count=1')
    levelExportJsonFile = open(levelExportJsonInput + '.json', 'w')
    levelExportJsonFile.write(levelExportJsonGet.text)
    levelExportJsonFile.close()
    print('Успешно!')


def accountExportJson():
    accountExportJsonInput = input('Выберите аккаунт: ')
    accountExportJsonGet = r.get(
        'https://gdbrowser.com/api/profile/' +
        accountExportJsonInput)
    accountExportJsonFile = open(accountExportJsonInput + '.json', 'w')
    accountExportJsonFile.write(accountExportJsonGet.text)
    accountExportJsonFile.close()
    print('Успешно!')


def LevelInfoDebug():
    print('!!! ВКЛЮЧЕН РЕЖИМ РАЗРАБОТЧИКА !!!')
    levelInput = input('Введите название уровня или ID: ')
    levelJson = r.get(
        'https://gdbrowser.com/api/search/' +
        levelInput +
        '?count=1')
    LevelInfo_dict = json.loads(levelJson.text)

    print()
    print(
        'Request sent to: https://gdbrowser.com/api/search/' +
        levelInput +
        '?count=1')
    print('API response:')
    print(levelJson.text)
    print()
    print('Converted to dict:')
    print(LevelInfo_dict)

    levelName = LevelInfo_dict[0]['name']
    levelId = LevelInfo_dict[0]['id']
    levelDescription = LevelInfo_dict[0]['description']
    levelCreator = LevelInfo_dict[0]['author']
    levelDifficulty = LevelInfo_dict[0]['difficulty']
    levelDownloads = LevelInfo_dict[0]['downloads']
    levelLikes = LevelInfo_dict[0]['likes']
    levelLength = LevelInfo_dict[0]['length']
    levelSongID = LevelInfo_dict[0]['customSong']
    levelSongAuthor = LevelInfo_dict[0]['songAuthor']
    levelSongName = LevelInfo_dict[0]['songName']
    levelObjects = LevelInfo_dict[0]['objects']
    levelFeatured = LevelInfo_dict[0]['featured']
    levelEpic = LevelInfo_dict[0]['epic']

    print()
    print('In vars:')
    print('levelName: ' + levelName)
    print('levelId: ' + levelId)
    print('levelDescription: ' + levelDescription)
    print('levelCreator: ' + levelCreator)
    print('levelDifficulty: ' + levelDifficulty)
    print('levelDownloads: ' + str(levelDownloads))
    print('levelLikes: ' + str(levelLikes))
    print('levelLength: ' + levelLength)
    print('levelMusic: ' + levelSongAuthor + ' - ' + levelSongName)
    print('levelSongID: ' + str(levelSongID))
    print(
        'levelMusicNG: https://www.newgrounds.com/audio/listen/' +
        str(levelSongID))
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
        open(
            iconDlInput +
            '_' +
            iconDlTypeInput +
            '.png',
            'wb').write(
            iconDlResult.content)
        print('Успешно!')
    elif iconDlTypeInput == '2':
        iconDlResult = r.get(url + '?form=ship')
        open(
            iconDlInput +
            '_' +
            iconDlTypeInput +
            '.png',
            'wb').write(
            iconDlResult.content)
        print('Успешно!')
    elif iconDlTypeInput == '3':
        iconDlResult = r.get(url + '?form=ball')
        open(
            iconDlInput +
            '_' +
            iconDlTypeInput +
            '.png',
            'wb').write(
            iconDlResult.content)
        print('Успешно!')
    elif iconDlTypeInput == '4':
        iconDlResult = r.get(url + '?form=ufo')
        open(
            iconDlInput +
            '_' +
            iconDlTypeInput +
            '.png',
            'wb').write(
            iconDlResult.content)
        print('Успешно!')
    elif iconDlTypeInput == '5':
        iconDlResult = r.get(url + '?form=wave')
        open(
            iconDlInput +
            '_' +
            iconDlTypeInput +
            '.png',
            'wb').write(
            iconDlResult.content)
        print('Успешно!')
    elif iconDlTypeInput == '6':
        iconDlResult = r.get(url + '?form=robot')
        open(
            iconDlInput +
            '_' +
            iconDlTypeInput +
            '.png',
            'wb').write(
            iconDlResult.content)
        print('Успешно!')
    elif iconDlTypeInput == '7':
        iconDlResult = r.get(url + '?form=spider')
        open(
            iconDlInput +
            '_' +
            iconDlTypeInput +
            '.png',
            'wb').write(
            iconDlResult.content)
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

while True:
    choiceInput = input('> ')
    if choiceInput == '1':
        LevelInput = input('Level name or ID: ')
        LevelInfo(LevelInput)
    elif choiceInput == '2':
        accountSearch()
    elif choiceInput == '3':
        levelExportJson()
    elif choiceInput == '4':
        accountExportJson()
    elif choiceInput == '5':
        LevelInfoDebug()
    elif choiceInput == '6':
        accountSearchDebug()
    elif choiceInput == '7':
        accountIconDL()
    else:
        print('Неверный ответ!')