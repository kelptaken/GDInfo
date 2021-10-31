# GDInfo by @kelptaken
# This script is using GNU General Public License v3.0; see the LICENSE
# file for details.

import requests as r
import json
from colorama import init, Fore, Style
from modules import Level
from modules import Account

init(convert=True) # now colors work on windows!

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


def ShowOptions():
    print(bold + yellow + 'GDInfo, v1.99' + r_color + r_style + dim + '  by kelptaken' + r_style)
    print(bold + 'Available options:' + r_style)
    print(bold + '0. (help): ' + r_style + 'Show available options')
    print(bold + '1. ' + r_style + 'Level info')
    print(bold + '2. ' + r_style + 'Account info')
    print(bold + '3. ' + r_style + 'Export level info in JSON')
    print(bold + '4. ' + r_style + 'Export account info in JSON')
    print(bold + '5. ' + r_style + 'Level info ' + dim + '(debug mode)' + r_style)
    print(bold + '6. ' + r_style + 'Account info ' + dim + '(debug mode)' + r_style)
    print(bold + '7. ' + r_style + 'Download user icon')

### FUNCTIONALITY ###

def LevelInfo_Output(Level):
    # The thing below is taking all the variables from LevelInfo module
    LevelInfo_jsonResponse, LevelInfo_dict, LevelInfo_Name, LevelInfo_ID, LevelInfo_Description, LevelInfo_Creator, LevelInfo_Difficulty, LevelInfo_Downloads, LevelInfo_Likes, LevelInfo_Length, LevelInfo_SongID, LevelInfo_SongCreator, LevelInfo_SongName, LevelInfo_Objects, LevelInfo_isFeatured, LevelInfo_isEpic, LevelInfo_Song, LevelInfo_SongNewgroundsLink = Level.LevelInfo(
        Level)

    # Show the info
    print()
    print(bold + 'Name: ' + r_style + LevelInfo_Name)
    print(bold + 'ID: ' + r_style + LevelInfo_ID)
    print(bold + 'Description: ' + r_style + LevelInfo_Description)
    print(bold + 'Creator: ' + r_style + LevelInfo_Creator)
    print(bold + 'Difficulty: ' + r_style + LevelInfo_Difficulty)
    if LevelInfo_isFeatured == True:
        print(green + '☑ ' + r_color + bold + 'Featured: ' + r_style + 'true')
    elif LevelInfo_isFeatured == False:
        print(red + '✕ ' + r_color + bold + 'Featured: ' + r_style + 'false')
    else:
        print(bold + 'Featured: ' + r_style +
              'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')

    if LevelInfo_isEpic == True:
        print(green + '☑ ' + r_color + bold + 'Epic: ' + r_style + 'true')
    elif LevelInfo_isEpic == False:
        print(red + '✕ ' + r_color + bold + 'Epic: ' + r_style + 'false')
    else:
        print(bold + 'Epic: ' + r_style +
              'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')

    print(bold + 'Downloads: ' + r_style + LevelInfo_Downloads)
    print(bold + 'Likes: ' + r_style + LevelInfo_Likes)
    print(bold + 'Length: ' + r_style + LevelInfo_Length)
    print(bold + 'Song: ' + r_style + LevelInfo_Song)
    print(bold + 'Song ID:  ' + r_style + LevelInfo_SongID)
    print(bold + 'Song on Newgrounds: ' +
          r_style + LevelInfo_SongNewgroundsLink)

    if LevelInfo_Objects == '0':
        print(bold + 'Objects: ' + r_style +
              'unknown, level copying may be locked')
    else:
        print(bold + 'Objects: ' + r_style + LevelInfo_Objects)
    print()


def AccountInfo_Output(Account):
    # Take vars from AccountInfo
    AccountInfo_jsonResponse, AccountInfo_dict, AccountInfo_Name, AccountInfo_AccountID, AccountInfo_PlayerID, AccountInfo_Stars, AccountInfo_Diamonds, AccountInfo_OffCoins, AccountInfo_UserCoins, AccountInfo_Demons, AccountInfo_CP, AccountInfo_IsModerator, AccountInfo_Privacy_FriendRequests, AccountInfo_Privacy_Messages, AccountInfo_Privacy_CommentHistory, AccountInfo_SM_YouTube, AccountInfo_SM_Twitter, AccountInfo_SM_Twitch = Account.AccountInfo(
        Account)

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
        print(green + '☑ ' + r_color + bold +
              'Moderator: ' + r_style + 'true, regular mod')
    elif AccountInfo_IsModerator == 2:
        print(green + '☑ ' + r_color + bold +
              'Moderator: ' + r_style + 'true, elder mod')
    else:
        print(bold + 'Moderator: ' + r_style +
              'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')

    print()

    # Privacy block
    print('Privacy: ')

    # Friend requests
    if AccountInfo_Privacy_FriendRequests == True:
        print(green + '☑ ' + r_color + bold +
              'Friend requests: ' + r_style + 'allowed')
    else:
        print(red + '✕ ' + r_color + bold +
              'Friend requests: ' + r_style + 'not allowed')

    # Messages
    if AccountInfo_Privacy_Messages == 'all':
        print(green + '☑ ' + r_color + bold +
              'Messages: ' + r_style + 'anyone')
    elif AccountInfo_Privacy_Messages == 'friends':
        print(yellow + '□ ' + r_color + bold +
              'Messages: ' + r_style + 'only friends')
    elif AccountInfo_Privacy_Messages == 'off':
        print(red + '✕ ' + r_color + bold + 'Messages: ' + r_style + 'off')
    else:
        print(bold + 'Messages: ' + r_style +
              'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')

    # Comment history
    if AccountInfo_Privacy_CommentHistory == 'all':
        print(green + '☑ ' + r_color + bold +
              'Comment history: ' + r_style + 'anyone')
    elif AccountInfo_Privacy_CommentHistory == 'friends':
        print(yellow + '□ ' + r_color + bold +
              'Comment history: ' + r_style + 'only friends')
    elif AccountInfo_Privacy_CommentHistory == 'off':
        print(red + '✕ ' + r_color + bold +
              'Comment history: ' + r_style + 'off')
    else:
        print(bold + 'Comment history: ' + r_style +
              'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')

    print()

    # Social media
    print('Social media:')

    # YouTube
    if AccountInfo_SM_YouTube != 'None':
        print(bold + 'YouTube: ' + r_style +
              'https://youtube.com/channel/' + AccountInfo_SM_YouTube)
    else:
        print(bold + 'YouTube: ' + r_style + 'not linked.')

    # Twitter
    if AccountInfo_SM_Twitter != 'None':
        print(bold + 'Twitter: ' + r_style +
              'https://twitter.com/' + AccountInfo_SM_Twitter)
    else:
        print(bold + 'Twitter: ' + r_style + 'not linked.')

    # Twitch
    if AccountInfo_SM_Twitch != 'None':
        print(bold + 'Twitch: ' + r_style +
              'https://twitch.tv/' + AccountInfo_SM_Twitch)
    else:
        print(bold + 'Twitch: ' + r_style + 'not linked. ')
    print()


def LevelExportJson_Output(Level):
    LevelExportJson_Content = Level.LevelExportJson(Level)
    LevelExportJson_File = open(Level + '.json', 'w')
    LevelExportJson_File.write(LevelExportJson_Content)
    LevelExportJson_File.close()
    print('Success!')


def ExportAccountJson(Account):
    AccountExportJson_Content = Account.AccountExportJson(Account)
    AccountExportJson_File = open(Account + '.json', 'w')
    AccountExportJson_File.write(AccountExportJson_Content)
    AccountExportJson_File.close()
    print('Success!')


def LevelInfoDebug(Level):
    print(bold + '!!! DEBUG MODE !!!' + r_style)

    print(debug_info + bold +
          'Calling Level.LevelInfo(Level) to get variables...' + r_style)
    LevelInfo_jsonResponse, LevelInfo_dict, LevelInfo_Name, LevelInfo_ID, LevelInfo_Description, LevelInfo_Creator, LevelInfo_Difficulty, LevelInfo_Downloads, LevelInfo_Likes, LevelInfo_Length, LevelInfo_SongID, LevelInfo_SongCreator, LevelInfo_SongName, LevelInfo_Objects, LevelInfo_isFeatured, LevelInfo_isEpic, LevelInfo_Song, LevelInfo_SongNewgroundsLink = Level.LevelInfo(Level)
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
        print(green + '☑ ' + r_color + bold +
              'LevelInfo_isFeatured: ' + r_style + 'True')
    elif LevelInfo_isFeatured == False:
        print(red + '✕ ' + r_color + bold +
              'LevelInfo_isFeatured: ' + r_style + 'False')
    else:
        print(bold + 'LevelInfo_isFeatured: ' + r_style +
              '"else" state in the code happened.')
        print(debug_fail + bold +
              "Looks like there's a problem with LevelInfo_isFeatured." + r_style)

    if LevelInfo_isEpic == True:
        print(green + '☑ ' + r_color + bold +
              'LevelInfo_isEpic: ' + r_style + 'true')
    elif LevelInfo_isEpic == False:
        print(red + '✕ ' + r_color + bold +
              'LevelInfo_isEpic: ' + r_style + 'false')
    else:
        print(bold + 'LevelInfo_isEpic: ' + r_style +
              '"else" state in the code happened.')
        print(debug_fail + bold +
              "Looks like there's a problem with LevelInfo_isEpic." + r_style)

    print(bold + 'LevelInfo_Downloads: ' + r_style + LevelInfo_Downloads)
    print(bold + 'LevelInfo_Likes: ' + r_style + LevelInfo_Likes)
    print(bold + 'LevelInfo_Length: ' + r_style + LevelInfo_Length)
    print(bold + 'LevelInfo_Song: ' + r_style + LevelInfo_Song)
    print(bold + 'LevelInfo_SongID:  ' + r_style + LevelInfo_SongID)
    print(bold + 'LevelInfo_SongNewgroundsLink: ' +
          r_style + LevelInfo_SongNewgroundsLink)

    if LevelInfo_Objects == '0':
        print(bold + 'LevelInfo_Objects: ' + r_style + '0')
        print(debug_info + bold +
              '0 objects. It looks like level copying is locked or unavailable.')
    else:
        print(bold + 'LevelInfo_Objects: ' + r_style + LevelInfo_Objects)
    print()


def AccountInfoDebug(Account):
    print(bold + '!!! DEBUG MODE !!!' + r_style)
    print(debug_info + bold + 'Calling Account.AccountInfo(Account) to get variables...' + r_style)
    AccountInfo_jsonResponse, AccountInfo_dict, AccountInfo_Name, AccountInfo_AccountID, AccountInfo_PlayerID, AccountInfo_Stars, AccountInfo_Diamonds, AccountInfo_OffCoins, AccountInfo_UserCoins, AccountInfo_Demons, AccountInfo_CP, AccountInfo_IsModerator, AccountInfo_Privacy_FriendRequests, AccountInfo_Privacy_Messages, AccountInfo_Privacy_CommentHistory, AccountInfo_SM_YouTube, AccountInfo_SM_Twitter, AccountInfo_SM_Twitch = Account.AccountInfo(Account)
    print(debug_success + bold + 'Success!' + r_style)
    print()
    print(debug_info + bold + 'Server response code: ' + r_style + str(AccountInfo_jsonResponse))
    print()
    print(debug_info + bold + 'Server response content: ' + r_style)
    print(AccountInfo_jsonResponse.text)
    print()
    print(debug_info + bold + 'Parsing...' + r_style)
    print(AccountInfo_dict)
    print()
    print(debug_success + bold + 'Success!' + r_style)
    print()
    print(bold + 'AccountInfo_Name: ' + r_style + AccountInfo_Name)
    print(bold + 'AccountInfo_AccountID: ' + r_style + AccountInfo_AccountID)
    print(bold + 'AccountInfo_PlayerID: ' + r_style + AccountInfo_PlayerID)
    print(bold + 'AccountInfo_Stars: ' + r_style + AccountInfo_Stars)
    print(bold + 'AccountInfo_Diamonds: ' + r_style + AccountInfo_Diamonds)
    print(bold + 'AccountInfo_OffCoins: ' + r_style + AccountInfo_OffCoins)
    print(bold + 'AccountInfo_UserCoins: ' + r_style + AccountInfo_UserCoins)
    print(bold + 'AccountInfo_Demons: ' + r_style + AccountInfo_Demons)
    print('AccountInfo_CP: ' + AccountInfo_CP)
    if AccountInfo_IsModerator == 0:
        print(red + '✕ ' + r_color + bold + 'AccountInfo_isModerator: ' + r_style + '0')
    elif AccountInfo_IsModerator == 1:
        print(green + '☑ ' + r_color + bold + 'AccountInfo_isModerator: ' + r_style + '1')
    elif AccountInfo_IsModerator == 2:
        print(green + '☑ ' + r_color + bold + 'AccountInfo_isModerator: ' + r_style + '2')
    else:
        print(bold + 'AccountInfo_isModerator: ' + r_style + '"else" state in the code happened.')

    print()

    # Privacy block
    print('Privacy: ')

    # Friend requests
    if AccountInfo_Privacy_FriendRequests == True:
        print(green + '☑ ' + r_color + bold + 'AccountInfo_Privacy_FriendRequests: ' + r_style + 'True')
    else:
        print(red + '✕ ' + r_color + bold + 'AccountInfo_Privacy_FriendRequests: ' + r_style + 'False')

    # Messages
    if AccountInfo_Privacy_Messages == 'all':
        print(green + '☑ ' + r_color + bold + 'AccountInfo_Privacy_Messages: ' + r_style + 'all')
    elif AccountInfo_Privacy_Messages == 'friends':
        print(yellow + '□ ' + r_color + bold + 'AccountInfo_Privacy_Messages: ' + r_style + 'friends')
    elif AccountInfo_Privacy_Messages == 'off':
        print(red + '✕ ' + r_color + bold + 'AccountInfo_Privacy_Messages: ' + r_style + 'off')
    else:
        print(bold + 'AccountInfo_Privacy_Messages: ' + r_style + '"else" state in the code happened. ')

    # Comment history
    if AccountInfo_Privacy_CommentHistory == 'all':
        print(green + '☑ ' + r_color + bold + 'AccountInfo_Privacy_CommentHistory: ' + r_style + 'all')
    elif AccountInfo_Privacy_CommentHistory == 'friends':
        print(yellow + '□ ' + r_color + bold + 'AccountInfo_Privacy_CommentHistory: ' + r_style + 'friends')
    elif AccountInfo_Privacy_CommentHistory == 'off':
        print(red + '✕ ' + r_color + bold + 'AccountInfo_Privacy_CommentHistory: ' + r_style + 'off')
    else:
        print(bold + 'Comment history: ' + r_style + '"else" state in the code happened.')

    print()

    # Social media
    print('Social media:')

    # YouTube
    if AccountInfo_SM_YouTube != 'None':
        print(bold + 'AccountInfo_SM_YouTube: ' + r_style +
              'https://youtube.com/channel/' + AccountInfo_SM_YouTube)
    else:
        print(bold + 'AccountInfo_SM_YouTube: ' + r_style + 'None')

    # Twitter
    if AccountInfo_SM_Twitter != 'None':
        print(bold + 'AccountInfo_SM_Twitter: ' + r_style +
              'https://twitter.com/' + AccountInfo_SM_Twitter)
    else:
        print(bold + 'Twitter: ' + r_style + 'None')

    # Twitch
    if AccountInfo_SM_Twitch != 'None':
        print(bold + 'AccountInfo_SM_Twitch: ' + r_style +
              'https://twitch.tv/' + AccountInfo_SM_Twitch)
    else:
        print(bold + 'AccountInfo_SM_Twitch: ' + r_style + 'None')
    print()


def DownloadIcon(Account, Type):
    AccountIconDL_Icon = Account.AccountIconDL(Account, Type)
    open(Account + '_' + Type + '.png', 'wb').write(AccountIconDL_Icon)
    print('Success!')

### FUNCTIONALITY END ###

### MENUs ###

def Menu_Level():
    print(yellow + bold + 'Select level operation:' + r_color + r_style)
    print(bold + '1. ' + r_style + 'Level information')
    print(bold + '2. ' + r_style + 'Level information ' + dim + '(debug mode)' + r_style)
    print(bold + '3. ' + r_style + 'Export level info to JSON')

def Menu_Account():
    print(yellow + bold + 'Select account operation:' + r_color + r_style)
    print(bold + '1. ' + r_style + 'Account information')
    print(bold + '2. ' + r_style + 'Account information ' + dim + '(debug mode)' + r_style)
    print(bold + '3. ' + r_style + 'Export account info to JSON')
    print(bold + '4. ' + r_style + 'Download icon')

def ShowGamemodes():
    print('1. Cube')
    print('2. Ship')
    print('3. Ball')
    print('4. UFO')
    print('5. Wave')
    print('6. Robot')
    print('7. Spider')

### MENUs END ###

### SELECTOR ###

while True:
    print(bold + yellow + 'Select operation type: ' + r_color + r_style)
    print(bold + '1. ' + r_style + 'Level')
    print(bold + '2. ' + r_style + 'Account')
    ChoiceInput_Main = input('> ')
    if ChoiceInput_Main == '1':
        Menu_Level()
        ChoiceInput_Level = input('Level operations > ')
        if ChoiceInput_Level == '1':
            LevelInfo_Input = input('Level name or ID: ')
            LevelInfo_Output(LevelInfo_Input)
        elif ChoiceInput_Level == '2':
            LevelInfo_Input = input('Level name or ID: ')
            LevelInfoDebug(LevelInfo_Input)
        elif ChoiceInput_Level == '3':
            LevelExportJson_Input = input ('Level name or ID: ')
            LevelExportJson_Output(LevelExportJson_Input)
        else:
            print('Uhm...')
    elif ChoiceInput_Main == '2':
        Menu_Account()
        ChoiceInput_Account = input('Account operations > ')
        if ChoiceInput_Account == '1':
            AccountInfo_Input = input('Account name or ID: ')
            AccountInfo_Output(AccountInfo_Input)
        elif ChoiceInput_Account == '2':
            AccountInfo_Input = input('Level name or ID: ')
            AccountInfoDebug(AccountInfo_Input)
        elif ChoiceInput_Account == '3':
            AccountExportJson_Input = input('Account name or ID: ')
            ExportAccountJson(AccountExportJson_Input)
        elif ChoiceInput_Account == '4':
            DownloadIcon_Input_Name = input('Account name or ID: ')
            ShowGamemodes()
            DownloadIcon_Input_Type = input('Icon type: ')
            DownloadIcon(DownloadIcon_Input_Name, DownloadIcon_Input_Type)
        else:
            print('Uhm...')
    else:
        print('Uhm...')

### SELECTOR END ###