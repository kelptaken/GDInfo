from os import stat_result
import requests as r
import json

def AccountInfo(Account):
    AccountInfo_jsonResponse = r.get('https://gdbrowser.com/api/profile/' + Account)
    AccountInfo_dict = json.loads(AccountInfo_jsonResponse.text)

    AccountInfo_Name = AccountInfo_dict['username']
    AccountInfo_AccountID = str(AccountInfo_dict['accountID'])
    AccountInfo_PlayerID = str(AccountInfo_dict['playerID'])
    AccountInfo_Stars = str(AccountInfo_dict['stars'])
    AccountInfo_Diamonds = str(AccountInfo_dict['diamonds'])
    AccountInfo_OffCoins = str(AccountInfo_dict['coins'])
    AccountInfo_UserCoins = str(AccountInfo_dict['userCoins'])
    AccountInfo_Demons = str(AccountInfo_dict['demons'])
    AccountInfo_CP = str(AccountInfo_dict['cp'])
    AccountInfo_IsModerator = AccountInfo_dict['moderator']

    AccountInfo_Privacy_FriendRequests = AccountInfo_dict['friendRequests']
    AccountInfo_Privacy_Messages = AccountInfo_dict['messages']
    AccountInfo_Privacy_CommentHistory = AccountInfo_dict['commentHistory']

    AccountInfo_SM_YouTube = str(AccountInfo_dict['youtube'])
    AccountInfo_SM_Twitter = str(AccountInfo_dict['twitter'])
    AccountInfo_SM_Twitch = str(AccountInfo_dict['twitch'])

    print(AccountInfo_Privacy_FriendRequests)

    return AccountInfo_jsonResponse, AccountInfo_dict, AccountInfo_Name, AccountInfo_AccountID, AccountInfo_PlayerID, AccountInfo_Stars, AccountInfo_Diamonds, AccountInfo_OffCoins, AccountInfo_UserCoins, AccountInfo_Demons, AccountInfo_CP, AccountInfo_IsModerator, AccountInfo_Privacy_FriendRequests, AccountInfo_Privacy_Messages, AccountInfo_Privacy_CommentHistory, AccountInfo_SM_YouTube, AccountInfo_SM_Twitter, AccountInfo_SM_Twitch