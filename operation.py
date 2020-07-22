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

    def GetAllPassID(self):
        Q = Query()
        return self.table.search(Q.Name == 'PassID')[0]['Config']

    def CreateTable(self):
        self.table.insert({"Name": "UserID", "Config": 0})
        self.table.insert({"Name": "InforID", "Config": 0})
        self.table.insert({"Name": "PassID", "Config": 0})

    def UserIDPlus(self):
        self.table.update({"Config": self.GetAllUserID() + 1}, where('Name') == "UserID")

    def InforIDPlus(self):
        self.table.update({"Config": self.GetAllInforID() + 1}, where('Name') == "InforID")

    def PassIDPlus(self):
        self.table.update({"Config": self.GetAllPassID() + 1}, where('Name') == "PassID")


class InfroDBoperate:  # Scenic spot Information
    def __init__(self):
        self.data = TinyDB('config/beijing.json')
        self.table = self.data.table('config')

    def Insert(self, name: str, tag: []):
        D = ConfigDBoperate()
        D.InforIDPlus()
        self.table.insert({'id': D.GetAllInforID(), 'name': name, 'tag': tag})

    def Search(self, id: int):
        Q = Query()
        return self.table.search(Q.id == int(id))[0]


class UserDBoperate:  # User Database Operations
    def __init__(self):
        self.data = TinyDB('config/user.json')
        self.table = self.data.table('user')

    def Insert(self, user: str, pw: str, like: []):  # Sign Up
        D = ConfigDBoperate()
        D.UserIDPlus()
        self.table.insert({"id": D.GetAllUserID(), "user": user, 'pw': pw, 'like': like})

    def Search(self, id: int):  # Get information
        Q = Query()
        return self.table.search(Q.id == int(id))[0]


class PassageDBoperate: # Passages Database Operations
    def __init__(self):
        self.data = TinyDB('config/passage.json')
        self.table = self.data.table('user')

    def Insert(self, passage: str, AuthorID: int, time: str, PlaceID: []):
        D = ConfigDBoperate()
        D.PassIDPlus()
        self.table.insert(
            {"PassageID": D.GetAllPassID(), "AuthorID": AuthorID, "Time": time, "PlaceID": PlaceID, "Passage": passage})

    def Search(self, id: int):
        Q = Query()
        return self.table.search(Q.AuthorID == int(id))[0]


class Show:  # To Show all information
    def __init__(self):
        self.Infor = InfroDBoperate()
        self.User = UserDBoperate()
        self.Config = ConfigDBoperate()
        self.UserID = self.Config.GetAllUserID()
        self.InforID = self.Config.GetAllInforID()

    def GetIDs(self):  # Size of the data
        print("User ID: " + str(self.UserID) + "\nInforID: " + str(self.InforID) + "\nPassID: " + str(
            self.Config.GetAllPassID()))

    def AllUser(self):  # Show every User
        for i in range(1, self.UserID + 1):
            print(self.User.Search(i))

    def AllInfor(self):  # Show every Information
        for i in range(1, self.InforID + 1):
            print(self.Infor.Search(i))


P = PassageDBoperate()
print(P.Search(1)['AuthorID'])
A = Show()
A.GetIDs()
A.AllUser()
A.AllInfor()
