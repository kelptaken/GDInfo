# GDInfo by @kelptaken
# This script is using GNU General Public License v3.0; see the LICENSE
# file for details.

from typing import Match, cast
import requests as r
import json
from colorama import init, Fore, Style
from modules import LevelInfo
from modules import AccountInfo
from modules import ExportJson

# Define some handy vars
dim = Style.DIM
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
bold = Style.BRIGHT
r_style = Style.RESET_ALL
r_color = Fore.RESET
debug_success = bold + green + '[·] ' + r_color + r_style
debug_info = bold + blue + '[·] ' + r_color + r_style
debug_fail = bold + red + '[!] ' + r_color + r_style

def ShowLevelInfo(Level):
    # The thing below is taking all the variables from LevelInfo module
    LevelInfo_jsonResponse, LevelInfo_dict, LevelInfo_Name, LevelInfo_ID, LevelInfo_Description, LevelInfo_Creator, LevelInfo_Difficulty, LevelInfo_Downloads, LevelInfo_Likes, LevelInfo_Length, LevelInfo_SongID, LevelInfo_SongCreator, LevelInfo_SongName, LevelInfo_Objects, LevelInfo_isFeatured, LevelInfo_isEpic, LevelInfo_Song, LevelInfo_SongNewgroundsLink = LevelInfo.LevelInfo(Level)


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


def ShowAccountInfo(Account):
    # Take vars from AccountInfo
    AccountInfo_jsonResponse, AccountInfo_dict, AccountInfo_Name, AccountInfo_AccountID, AccountInfo_PlayerID, AccountInfo_Stars, AccountInfo_Diamonds, AccountInfo_OffCoins, AccountInfo_UserCoins, AccountInfo_Demons, AccountInfo_CP, AccountInfo_IsModerator, AccountInfo_Privacy_FriendRequests, AccountInfo_Privacy_Messages, AccountInfo_Privacy_CommentHistory, AccountInfo_SM_YouTube, AccountInfo_SM_Twitter, AccountInfo_SM_Twitch = AccountInfo.AccountInfo(Account)

    # Show info
    print()
    print(bold + 'Name: ' + r_style + AccountInfo_Name)
    print(bold + 'Account ID: ' + r_style + AccountInfo_AccountID)
    print(bold + 'Player ID: ' + r_style + AccountInfo_PlayerID)
    print(bold + 'Stars: ' + r_style + AccountInfo_Stars)
    print(bold + 'Diamonds: ' + r_style + AccountInfo_Diamonds)
    print(bold + 'Coins: ' + r_style + AccountInfo_OffCoins)
    print(bold + 'User coins: ' + r_style + AccountInfo_UserCoins)
    print(bold + 'Demons: ' + r_style + AccountInfo_Demons)
    print('Creator points: ' + AccountInfo_CP)
    if AccountInfo_IsModerator == 0:
        print(red + '✕ ' + r_color + bold + 'Moderator: ' + r_style + 'false')
    elif AccountInfo_IsModerator == 1:
        print(green + '☑ ' + r_color + bold + 'Moderator: ' + r_style + 'true, regular mod')
    elif AccountInfo_IsModerator == 2:
        print(green + '☑ ' + r_color + bold + 'Moderator: ' + r_style + 'true, elder mod')
    else:
        print(bold + 'Moderator: ' + r_style + 'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')

    print()

    # Privacy block
    print('Privacy: ')

    # Friend requests
    if AccountInfo_Privacy_FriendRequests == True:
        print(green + '☑ ' + r_color + bold + 'Friend requests: ' + r_style + 'allowed')
    else:
        print(red + '✕ ' + r_color + bold + 'Friend requests: ' + r_style + 'not allowed')

    # Messages
    if AccountInfo_Privacy_Messages == 'all':
        print(green + '☑ ' + r_color + bold + 'Messages: ' + r_style + 'anyone')
    elif AccountInfo_Privacy_Messages == 'friends':
        print(yellow + '□ ' + r_color + bold + 'Messages: ' + r_style + 'only friends')
    elif AccountInfo_Privacy_Messages == 'off':
        print(red + '✕ ' + r_color + bold + 'Messages: ' + r_style + 'off')
    else:
        print(bold + 'Messages: ' + r_style + 'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')

    # Comment history
    if AccountInfo_Privacy_CommentHistory == 'all':
        print(green + '☑ ' + r_color + bold + 'Comment history: ' + r_style + 'anyone')
    elif AccountInfo_Privacy_CommentHistory == 'friends':
        print(yellow + '□ ' + r_color + bold + 'Comment history: ' + r_style + 'only friends')
    elif AccountInfo_Privacy_CommentHistory == 'off':
        print(red + '✕ ' + r_color + bold + 'Comment history: ' + r_style + 'off')
    else:
        print(bold + 'Comment history: ' + r_style + 'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')

    print()

    # Social media
    print('Social media:')
    
    # YouTube
    if AccountInfo_SM_YouTube != 'None':
        print(bold + 'YouTube: ' + r_style + 'https://youtube.com/channel/' + AccountInfo_SM_YouTube)
    else:
        print(bold + 'YouTube: ' + r_style + 'not linked.')

    # Twitter
    if AccountInfo_SM_Twitter != 'None':
        print(bold + 'Twitter: ' + r_style + 'https://twitter.com/' + AccountInfo_SM_Twitter)
    else:
        print(bold + 'Twitter: ' + r_style + 'not linked.')

    # Twitch
    if AccountInfo_SM_Twitch != 'None':
        print(bold + 'Twitch: ' + r_style + 'https://twitch.tv/' + AccountInfo_SM_Twitch)
    else:
        print(bold + 'Twitch: ' + r_style + 'not linked. ')
    print()


def ExportLevelJson(Level):
    LevelExportJson_Content = ExportJson.LevelExportJson(Level)
    LevelExportJson_File = open(Level + '.json', 'w')
    LevelExportJson_File.write(LevelExportJson_Content)
    LevelExportJson_File.close()
    print('Success!')


def ExportAccountJson(Account):
    AccountExportJson_Content = ExportJson.AccountExportJson(Account)
    AccountExportJson_File = open(Account + '.json', 'w')
    AccountExportJson_File.write(AccountExportJson_Content)
    AccountExportJson_File.close()
    print('Success!')


def LevelInfoDebug(Level):
    print(bold + '!!! DEBUG MODE ON !!!' + r_style)

    print(debug_info + bold + 'Calling LevelInfo.LevelInfo(Level) to get variables...' + r_style)
    LevelInfo_jsonResponse, LevelInfo_dict, LevelInfo_Name, LevelInfo_ID, LevelInfo_Description, LevelInfo_Creator, LevelInfo_Difficulty, LevelInfo_Downloads, LevelInfo_Likes, LevelInfo_Length, LevelInfo_SongID, LevelInfo_SongCreator, LevelInfo_SongName, LevelInfo_Objects, LevelInfo_isFeatured, LevelInfo_isEpic, LevelInfo_Song, LevelInfo_SongNewgroundsLink = LevelInfo.LevelInfo(Level)
    print(debug_success + bold + 'Success!' + r_style)
    print()
    print(debug_info + bold + 'Server response code: ' + str(LevelInfo_jsonResponse) + r_style)
    print(debug_info + bold + 'Server response content: ' + r_style)
    print(LevelInfo_jsonResponse.text)
    print()
    print(debug_info + bold + 'Parsing...' + r_style)
    print(LevelInfo_dict)
    print()
    print(debug_success + bold + 'Success!' + r_style)

    print()
    print(bold + 'LevelInfo_Name: ' + r_style + LevelInfo_Name)
    print(bold + 'LevelInfo_ID: ' + r_style + LevelInfo_ID)
    print(bold + 'LevelInfo_Description: ' + r_style + LevelInfo_Description)
    print(bold + 'LevelInfo_Creator: ' + r_style + LevelInfo_Creator)
    print(bold + 'LevelInfo_Difficulty: ' + r_style + LevelInfo_Difficulty)
    if LevelInfo_isFeatured == True:
        print(green + '☑ ' + r_color + bold + 'LevelInfo_isFeatured: ' + r_style + 'True')
    elif LevelInfo_isFeatured == False:
        print(red + '✕ ' + r_color + bold + 'LevelInfo_isFeatured: ' + r_style + 'False')
    else:
        print(bold + 'LevelInfo_isFeatured: ' + r_style + '"else" state in the code happened.')
        print(debug_fail + bold + "Looks like there's a problem with LevelInfo_isFeatured." + r_style)

    if LevelInfo_isEpic == True:
        print(green + '☑ ' + r_color + bold + 'LevelInfo_isEpic: ' + r_style + 'true')
    elif LevelInfo_isEpic == False:
        print(red + '✕ ' + r_color + bold + 'LevelInfo_isEpic: ' + r_style + 'false')
    else:
        print(bold + 'LevelInfo_isEpic: ' + r_style + '"else" state in the code happened.')
        print(debug_fail + bold + "Looks like there's a problem with LevelInfo_isEpic." + r_style)
    
    print(bold + 'LevelInfo_Downloads: ' + r_style + LevelInfo_Downloads)
    print(bold + 'LevelInfo_Likes: ' + r_style + LevelInfo_Likes)
    print(bold + 'LevelInfo_Length: ' + r_style + LevelInfo_Length)
    print(bold + 'LevelInfo_Song: ' + r_style + LevelInfo_Song)
    print(bold +'LevelInfo_SongID:  ' + r_style + LevelInfo_SongID)
    print(bold + 'LevelInfo_SongNewgroundsLink: ' + r_style + LevelInfo_SongNewgroundsLink)
    
    if LevelInfo_Objects == '0':
        print(bold + 'LevelInfo_Objects: ' + r_style + '0')
        print(debug_info + bold + '0 objects. It looks like level copying is locked or unavailable.')
    else:
        print(bold + 'LevelInfo_Objects: ' + r_style + LevelInfo_Objects)
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


print(bold + yellow + 'GDInfo, v1.99' + r_color + r_style + dim + '  by kelptaken' + r_style)
print(bold + 'Available options:' + r_style)
print(bold + '1. ' + r_style + 'Level info')
print(bold + '2. ' + r_style + 'Account info')
print(bold + '3. ' + r_style + 'Export level info in JSON')
print(bold + '4. ' + r_style + 'Export account info in JSON')
print(bold + '5. ' + r_style + 'Level info ' + dim + '(debug mode)' + r_style)
print(bold + '6. ' + r_style + 'Account info ' + dim + '(debug mode)' + r_style)
print(bold + '7. ' + r_style + 'Download user icon')

while True:
    choiceInput = input('> ')
    if choiceInput == '1':
        LevelInput = input('Level name or ID: ')
        ShowLevelInfo(LevelInput)
    elif choiceInput == '2':
        AccountInput = input('Account name or ID: ')
        ShowAccountInfo(AccountInput)
    elif choiceInput == '3':
        LevelInput = input('Level name or ID: ')
        ExportLevelJson(LevelInput)
    elif choiceInput == '4':
        ExportAccountJson(AccountInput)
    elif choiceInput == '5':
        LevelInput = input('Level name or ID: ')
        LevelInfoDebug(LevelInput)
    elif choiceInput == '6':
        accountSearchDebug()
    elif choiceInput == '7':
        accountIconDL()
    else:
        print('Неверный ответ!')