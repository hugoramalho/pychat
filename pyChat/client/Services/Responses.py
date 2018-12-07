from . import DTP
from pyChat.client.Models import Models

class ResponseLogin(DTP.DataTransfer):
    def __init__(self, login:Models.Login = Models.Login()):
        super().__init__()
        self.login = login

    def toJson(self):
        dictJson = super().toJson()
        dictJson['user'] = self.user.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.user = Models.user().fromJson(dictObj['user'])
        return self


class ResponseRetrieveChat(DTP.DataTransfer):
    def __init__(self, friendship: Models.Friendship, lstMessages: Models.LstMessages):
        super().__init__()
        self.friendship = friendship
        self.lstMessages = Models.LstMessages()

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['friendship'] = self.friendship.toJson()
        dictJson['lstMessages'] = self.lstMessages.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.friendship = Models.LstMessages().fromJson(dictObj['friendship'])
        self.lstMessages = Models.LstMessages().fromJson(dictObj['lstMessages'])
        return self


class ResponseRetrieveFriends(DTP.DataTransfer):
    def __init__(self, user: Models.user = Models.user()):
        super().__init__()
        self.user = user
        self.lstUsers = Models.LstUsers()

    def toJson(self):
        dictJson = super().toJson()
        dictJson['user'] = self.user.toJson()
        dictJson['lstUsers'] = self.lstUsers.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.lstUsers = Models.LstUsers().fromJson(dictObj['lstUsers'])
        return self


class ResponseSendMessage(DTP.DataTransfer):
    def __init__(self, message: Models.Message = Models.Message()):
        super().__init__()
        self.message = message

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['message'] = self.message.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.message = Models.Message().fromJson(dictObj)
        return self


class ResponseStatusMessage(DTP.DataTransfer):
    def __init__(self, message: Models.Message = Models.Message()):
        super().__init__()
        self.message = message

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['message'] = self.message.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.message = Models.Message().fromJson(dictObj)
        return self


class ResponseNewUser(DTP.DataTransfer):
    def __init__(self, user:Models.user = Models.user()):
        super().__init__()
        self.user = user
    def toJson(self):
        dictJson = super().toJson()
        dictJson['user'] = self.user.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.user = Models.user().fromJson(dictObj['user'])
        return self


class ResponseAddFriend(DTP.DataTransfer):
    def __init__(self, senderUser:Models.user = Models.user(), recipUser:Models.user = Models.user()):
        super().__init__()
        self.senderUser = senderUser
        self.recipUser = recipUser
        self.statusAcept = 0

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['senderUser'] = self.senderUser.toJson()
        dictJson['recipUser'] = self.recipUser.toJson()
        dictJson['statusAcept'] = self.statusAcept
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.recipUser = Models.user().fromJson(dictObj['recipUser'])
        self.senderUser = Models.user().fromJson(dictObj['senderUser'])
        self.statusAcept = dictObj['statusAcept']
        return self


class ResponseNamesLike(DTP.DataTransfer):
    def __init__(self, namesLike:str=''):
        super().__init__()
        self.namesLike = namesLike

    def toJson(self):
        dictJson = super().toJson()
        dictJson['namesLike'] = self.namesLike
        return dictJson

    def fromJson(self, dictObj: dict or list):
        super().fromJson(dictObj)
        self.namesLike = Models.LstUsers().fromJson(dictObj)
        return self


class ResponseDeleteChat(DTP.DataTransfer):
    def __init__(self, friendship: Models.Friendship):
        super().__init__()
        self.friendship = friendship

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['friendship'] = self.friendship.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.friendship = Models.Friendship().fromJson(dictObj['friendship'])
        return self


class ResponseDeleteMessage(DTP.DataTransfer):
    def __init__(self, message:Models.Message = Models.Message()):
        super().__init__()
        self.message = message
        self.info = ''

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['message'] = self.message.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.info = dictObj['info']
        return self

class ResponseBlockUser(DTP.DataTransfer):
    def __init__(self, senderUser: Models.user = Models.user(), recipUser: Models.user = Models.user()):
        """
        :param senderUser:  Models.user()
        :param recipUser:  Models.user()
        :rtype: ResponseBlockUser
        """
        super().__init__()
        self.senderUser = senderUser
        self.recipUser = recipUser

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['senderUser'] = self.senderUser.toJson()
        dictJson['recipUser'] = self.recipUser.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.recipUser = Models.user().fromJson(dictObj['recipUser'])
        self.senderUser = Models.user().fromJson(dictObj['senderUser'])
        return self


class ResponseUnblockUser(DTP.DataTransfer):
    def __init__(self, senderUser:Models.user = Models.user(), recipUser:Models.user = Models.user()):
        """
        :param senderUser:  Models.user()
        :param recipUser:  Models.user()
        :rtype: ResponseUnblockUser
        """
        super().__init__()
        self.senderUser = senderUser
        self.recipUser = recipUser

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['senderUser'] = self.senderUser.toJson()
        dictJson['recipUser'] = self.recipUser.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.recipUser = Models.user().fromJson(dictObj['recipUser'])
        self.senderUser = Models.user().fromJson(dictObj['senderUser'])
        return self