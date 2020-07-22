# coding=utf-8
from tinydb import TinyDB
from tinydb.queries import Query, where


class ConfigDBoperate:  # Data for json's
    def __init__(self):
        self.data = TinyDB('config/config.json')
        self.table = self.data.table('config')

    def GetAllUserID(self):
        Q = Query()
        return self.table.search(Q.Name == 'UserID')[0]['Config']

    def GetAllInforID(self):
        Q = Query()
        return self.table.search(Q.Name == 'InforID')[0]['Config']

    def CreateTable(self):
        self.table.insert({"Name": "UserID", "Config": 0})
        self.table.insert({"Name": "InforID", "Config": 0})

    def UserIDPlus(self):
        self.table.update({"Config": self.GetAllUserID() + 1}, where('Name') == "UserID")

    def InforIDPlus(self):
        self.table.update({"Config": self.GetAllInforID() + 1}, where('Name') == "InforID")


class InfroDBoperate:  # Scenic spot Information
    def __init__(self):
        self.data = TinyDB('config/beijing.json')
        self.table = self.data.table('config')

    def Insert(self, name, tag):
        D = ConfigDBoperate()
        D.InforIDPlus()
        self.table.insert({'id': D.GetAllInforID(), 'name': name, 'tag': tag})

    def Search(self, id):
        Q = Query()
        return self.table.search(Q.id == int(id))[0]


class UserDBoperate:  # User Database Operations
    def __init__(self):
        self.data = TinyDB('config/user.json')
        self.table = self.data.table('user')

    def Insert(self, user, pw, like):
        D = ConfigDBoperate()
        D.UserIDPlus()
        self.table.insert({"id": D.GetAllUserID(), "user": user, 'pw': pw, 'like': like})

    def Search(self, id):
        Q = Query()
        return self.table.search(Q.id == int(id))[0]


class Show:  # To Show all information
    def __init__(self):
        self.Infor = InfroDBoperate()
        self.User = UserDBoperate()
        self.Config = ConfigDBoperate()
        self.UserID = self.Config.GetAllUserID()
        self.InforID = self.Config.GetAllInforID()

    def GetIDs(self):  # Size of the data
        print(self.UserID, self.InforID)

    def AllUser(self):  # Show every User
        for i in range(1, self.UserID + 1):
            print(self.User.Search(i))

    def AllInfor(self):  # Show every Information
        for i in range(1, self.InforID + 1):
            print(self.Infor.Search(i))


A = Show()
A.GetIDs()
A.AllUser()
A.AllInfor()
