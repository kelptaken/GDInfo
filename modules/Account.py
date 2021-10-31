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

def AccountIconDL(Account, Type):
    url = 'https://gdbrowser.com/icon/' + Account

    if Type == '1':
        AccountIconDL_Response = r.get(url + '?form=cube')
        AccountIconDL_Icon = AccountIconDL_Response.content
        return AccountIconDL_Icon
    
    elif Type == '2':
        AccountIconDL_Response = r.get(url + '?form=ship')
        AccountIconDL_Icon = AccountIconDL_Response.content
        return AccountIconDL_Icon
    
    elif Type == '3':
        AccountIconDL_Response = r.get(url + '?form=ball')
        AccountIconDL_Icon = AccountIconDL_Response.content
        return AccountIconDL_Icon
    
    elif Type == '4':
        AccountIconDL_Response = r.get(url + '?form=ufo')
        AccountIconDL_Icon = AccountIconDL_Response.content
        return AccountIconDL_Icon
    
    elif Type == '5':
        AccountIconDL_Response = r.get(url + '?form=wave')
        AccountIconDL_Icon = AccountIconDL_Response.content
        return AccountIconDL_Icon
    
    elif Type == '6':
        AccountIconDL_Response = r.get(url + '?form=robot')
        AccountIconDL_Icon = AccountIconDL_Response.content
        return AccountIconDL_Icon

    elif Type == '7':
        AccountIconDL_Response = r.get(url + '?form=spider')
        AccountIconDL_Icon = AccountIconDL_Response.content
        return AccountIconDL_Icon

def AccountExportJson(Account):
    AccountExportJson_Response = r.get('https://gdbrowser.com/api/profile/' + Account)
    AccountExportJson_ResponseContent = AccountExportJson_Response.text

    return AccountExportJson_ResponseContent

def AccountPosts(Account):
    pass


def AccountPost_LikePost(Account, Post):
    pass


def AccountPost_DislikePost(Account, Post):
    pass

def AccountLevels(Account):
    pass