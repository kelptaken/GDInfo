# GDInfo by @kelptaken
# This script is using GNU General Public License v3.0; see the LICENSE
# file for details.

# <!--- IMPORTS AND DEFINES ---------

__VERSION__ = 'v2.1'

import platform
import sys
from colorama import init, Fore, Style
from halo import Halo
import AccountModule
import LevelModule

if platform.system() == 'Windows':
    init(convert=True)
else:
    init()

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
info_true = green + '☑ ' + r_color
info_false = red + '✕ ' + r_color

print(bold + 'Detected system: ' + r_style + platform.system())


# IMPORTS AND DEFINES --------->


# <!--- FUNCTIONALITY ---------


@Halo(text='Loading', spinner='dots')
def LevelInfo_Output(Level):
    LevelInfo = LevelModule.RetrieveLevelInfo(Level)

    # Show the info ----------
    print()
    print(bold + 'Name: ' + r_style + LevelInfo.name)
    print(bold + 'ID: ' + r_style + str(LevelInfo.id))
    print()
    print(bold + 'You will get...' + r_style)
    print('· ' + str(LevelInfo.stars) + ' stars (' +
          str(LevelInfo.starsRequested) + ' requested by creator)...')
    print('· ' + str(LevelInfo.orbs) + ' orbs...')
    print('· ...and ' + str(LevelInfo.diamonds) +
          ' diamonds for beating this level.')
    print()
    print(bold + 'Description: ' + r_style + LevelInfo.description)
    print(bold + 'Creator: ' + r_style + LevelInfo.author)
    print(bold + 'Game version: ' + r_style + LevelInfo.gameVersion)
    print(bold + 'Level version: ' + r_style + str(LevelInfo.version))
    print(bold + 'Difficulty: ' + r_style + LevelInfo.difficulty)

    if LevelInfo.difficulty != 'Extreme Demon':
        LevelInfo.demonList = 'N/A'
    else:
        pass

    print(bold + 'Position in PointerCrate Demonlist: ' +
          r_style + str(LevelInfo.demonList))
    if LevelInfo.featured == True:
        print(info_true + bold + 'Featured: ' + r_style + 'true')
    elif LevelInfo.featured == False:
        print(info_false + bold + 'Featured: ' + r_style + 'false')
    else:
        print(bold + 'Featured: ' + r_style +
              'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')

    if LevelInfo.epic == True:
        print(info_true + bold + 'Epic: ' + r_style + 'true')
    elif LevelInfo.epic == False:
        print(info_false + bold + 'Epic: ' + r_style + 'false')
    else:
        print(bold + 'Epic: ' + r_style +
              'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')

    print(bold + 'Downloads: ' + r_style + str(LevelInfo.downloads))
    print(bold + 'Likes: ' + r_style + str(LevelInfo.likes))
    print(bold + 'Coins: ' + r_style + str(LevelInfo.coins))

    if LevelInfo.verifiedCoins == True:
        print(info_true + bold + 'Coins' + r_style + ' are verified.')
    elif LevelInfo.verifiedCoins == False:
        print(info_false + bold + 'Coins' + r_style + ' are NOT verified.')
    else:
        print(bold + 'Coins' + r_style +
              ' are, uhm... else statement just happened in the code. Report this to @kelptaken.')

    print(bold + 'Length: ' + r_style + LevelInfo.length)

    print()
    print(bold + 'Song: ' + r_style + LevelInfo.songAuthor + ' - ' + LevelInfo.songName)
    try:
        print(bold + 'Song ID:  ' + r_style + str(LevelInfo.songID))
        print(bold + 'Song on Newgrounds: ' +
              r_style + 'https://newgrounds.com/audio/listen/' + str(LevelInfo.songID))
        print(bold + 'Song size: ' + r_style + LevelInfo.songSize)
        print(bold + 'Raw link to song MP3: ' + r_style + LevelInfo.songLink)
    except BaseException:
        print(bold + 'Song ID: N/A' + r_style)
        print(bold + 'Song on Newgrounds: N/A' + r_style)
        print(bold + 'Song size: N/A' + r_style)
        print(bold + 'Raw link to song MP3: N/A')
    print()

    if LevelInfo.objects == '0':
        print(bold + 'Objects: ' + r_style +
              'unknown, level copying may be locked')
    else:
        print(bold + 'Objects: ' + r_style + str(LevelInfo.objects))

    if LevelInfo.large == True:
        print(info_true + bold + 'Large (>40k objects): ' + r_style + 'true')
    elif LevelInfo.large == False:
        print(info_false + bold + 'Large (>40k objects): ' + r_style + 'false')
    print()


@Halo(text='Loading', spinner='dots')
def AccountInfo_Output(Account):
    # Take vars from AccountInfo ----------
    AccountInfo = AccountModule.RetrieveAccountInfo(Account)

    # Show info ----------
    print()
    print(bold + 'Name: ' + r_style + AccountInfo.username)
    print(bold + 'Account ID: ' + r_style + str(AccountInfo.accountID))
    print(bold + 'Player ID: ' + r_style + str(AccountInfo.playerID))
    print(bold + 'Stars: ' + r_style + str(AccountInfo.stars))
    print(bold + 'Diamonds: ' + r_style + str(AccountInfo.diamonds))
    print(bold + 'Coins: ' + r_style + str(AccountInfo.coins))
    print(bold + 'User coins: ' + r_style + str(AccountInfo.userCoins))
    print(bold + 'Demons: ' + r_style + str(AccountInfo.demons))
    print(bold + 'Creator points: ' + r_style + str(AccountInfo.cp))
    if AccountInfo.moderator == 0:
        print(info_false + bold + 'Moderator: ' + r_style + 'false')
    elif AccountInfo.moderator == 1:
        print(info_true + bold +
              ' Moderator: ' + r_style + 'true, regular mod')
    elif AccountInfo.moderator == 2:
        print(info_true + bold +
              ' Moderator: ' + r_style + 'true, elder mod')
    else:
        print(bold + ' Moderator: ' + r_style +
              'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')

    print()

    # Privacy block ----------
    print('Privacy: ')

    # Friend requests ----------
    if AccountInfo.friendRequests == True:
        print(info_true + bold +
              ' Friend requests: ' + r_style + 'allowed')
    else:
        print(info_false + bold +
              ' Friend requests: ' + r_style + 'not allowed')

    # Messages ----------
    if AccountInfo.messages == 'all':
        print(info_true + bold +
              ' Messages: ' + r_style + 'anyone')
    elif AccountInfo.messages == 'friends':
        print(yellow + '□ ' + r_color + bold +
              ' Messages: ' + r_style + 'only friends')
    elif AccountInfo.messages == 'off':
        print(info_false + bold + 'Messages: ' + r_style + 'off')
    else:
        print(bold + ' Messages: ' + r_style +
              'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')

    # Comment history ----------
    if AccountInfo.commentHistory == 'all':
        print(info_true + bold +
              ' Comment history: ' + r_style + 'anyone')
    elif AccountInfo.commentHistory == 'friends':
        print(yellow + '□ ' + r_color + bold +
              ' Comment history: ' + r_style + 'only friends')
    elif AccountInfo.commentHistory == 'off':
        print(info_false + bold +
              ' Comment history: ' + r_style + 'off')
    else:
        print(bold + ' Comment history: ' + r_style +
              'unknown: "else" state in the code happened. It may be a server error, or another bug in my dirty code ¯\_(ツ)_/¯')

    print()

    # Social media ----------
    print('Social media:')

    # YouTube ----------
    if str(AccountInfo.youtube) != 'None':
        print(bold + 'YouTube: ' + r_style +
              'https://youtube.com/channel/' + AccountInfo.youtube)
    else:
        print(bold + 'YouTube: ' + r_style + 'not linked.')

    # Twitter ----------
    if str(AccountInfo.twitter) != 'None':
        print(bold + 'Twitter: ' + r_style +
              'https://twitter.com/' + AccountInfo.twitter)
    else:
        print(bold + 'Twitter: ' + r_style + 'not linked.')

    # Twitch ----------
    if str(AccountInfo.twitch) != 'None':
        print(bold + 'Twitch: ' + r_style +
              'https://twitch.tv/' + AccountInfo.twitch)
    else:
        print(bold + 'Twitch: ' + r_style + 'not linked. ')
    print()


@Halo(text='Loading', spinner='dots')
def LevelExportJson_Output(Level):
    LevelExportJson_Content = LevelModule.LevelExportJson(Level)
    LevelExportJson_File = open(Level + '.json', 'w')
    LevelExportJson_File.write(LevelExportJson_Content)
    LevelExportJson_File.close()


@Halo(text='Loading', spinner='dots')
def ExportAccountJson(Account):
    AccountExportJson_Content = AccountModule.AccountExportJson(Account)
    AccountExportJson_File = open(Account + '.json', 'w')
    AccountExportJson_File.write(AccountExportJson_Content)
    AccountExportJson_File.close()


@Halo(text='Loading', spinner='dots')
def DownloadIcon(Account, Type):
    AccountIconDL_Icon = AccountModule.AccountIconDL(Account, Type)
    open(Account + '_' + Type + '.png', 'wb').write(AccountIconDL_Icon)


# FUNCTIONALITY --------->


# <!--- MENUs ---------


def Menu_Level():
    print(yellow + bold + 'Select level operation:' + r_color + r_style)
    print(bold + '1. ' + r_style + 'Level information')
    print(bold + '2. ' + r_style + 'Export level info to JSON')


def Menu_Account():
    print(yellow + bold + 'Select account operation:' + r_color + r_style)
    print(bold + '1. ' + r_style + 'Account information')
    print(bold + '2. ' + r_style + 'Export account info to JSON')
    print(bold + '3. ' + r_style + 'Download icon')


def ShowGamemodes():
    print('1. Cube')
    print('2. Ship')
    print('3. Ball')
    print('4. UFO')
    print('5. Wave')
    print('6. Robot')
    print('7. Spider')


# MENUs --------->


# <?--- SELECTOR ---------


def returnToMonke():
    print(bold + yellow + f'GDInfo {__VERSION__}' + r_color +
          r_style + dim + ' by @kelptaken' + r_style)
    print(bold + yellow + 'Select operation type: ' + r_color + r_style)
    print(bold + '1. ' + r_style + 'Level')
    print(bold + '2. ' + r_style + 'Account')
    ChoiceInput_Main = input('> ')

    # LEVEL block
    if ChoiceInput_Main == '1':
        Menu_Level()
        ChoiceInput_Level = input('Level operations > ')
        if ChoiceInput_Level == '1':
            LevelInfo_Input = input('Level name or ID: ')
            LevelInfo_Output(LevelInfo_Input)  # Level info
        elif ChoiceInput_Level == '2':
            LevelExportJson_Input = input('Level name or ID: ')
            # Level info export to JSON
            LevelExportJson_Output(LevelExportJson_Input)
        else:
            print('Uhm...')

    # ACCOUNT block
    elif ChoiceInput_Main == '2':
        Menu_Account()
        ChoiceInput_Account = input('Account operations > ')
        if ChoiceInput_Account == '1':
            AccountInfo_Input = input('Account name or ID: ')
            AccountInfo_Output(AccountInfo_Input)  # Account info
        elif ChoiceInput_Account == '2':
            AccountExportJson_Input = input('Account name or ID: ')
            # Export account info to JSON
            ExportAccountJson(AccountExportJson_Input)
        elif ChoiceInput_Account == '3':
            DownloadIcon_Input_Name = input('Account name or ID: ')
            ShowGamemodes()
            DownloadIcon_Input_Type = input('Icon type: ')
            DownloadIcon(DownloadIcon_Input_Name,
                         DownloadIcon_Input_Type)  # Download icon
        else:
            print('Uhm...')
    else:
        print('Uhm...')


# SELECTOR --------->

global climode

try:
    if sys.argv[1] == 'cli':
        climode = True
        print(bold + 'Entering CLI mode.' + r_style)
    else:
        climode = False
except IndexError:
    climode = False

if climode == False:
    try:
        while True:
            returnToMonke()
    except KeyboardInterrupt:
        exit('\nBye!')
else:

    # CLI mode. ----------

    try:
        if sys.argv[2] == 'level':

            if sys.argv[3] == 'info':
                LevelInfo_Output(sys.argv[4])

            elif sys.argv[3] == 'json':
                LevelExportJson_Output(sys.argv[4])

            else:
                print('Uhm...')  # ERROR4

        elif sys.argv[2] == 'account':

            if sys.argv[3] == 'info':
                AccountInfo_Output(sys.argv[4])

            elif sys.argv[3] == 'json':
                ExportAccountJson(sys.argv[4])

            elif sys.argv[3] == 'icon':
                DownloadIcon(sys.argv[5], sys.argv[4])
            else:
                print('Uhm...')  # ERROR5

        else:
            print('Uhm...')

    except IndexError:
        print('Uhm...')  # ERROR6
