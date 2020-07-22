# coding=utf-8
from tinydb import TinyDB
from tinydb.queries import Query, where


class ConfigDBoperate:
    def OpenInfroDB(self):
        self.data = TinyDB('config/config.json')
        self.table = self.data.table('config')

    def GetAllUserID(self):
        Q = Query()
        return self.table.search(Q.name == 'UserID')

    def GetAllInforID(self):
        Q = Query()
        return self.table.search(Q.name == 'InforID')

    def CreateTable(self):
        

class InfroDBoperate:
    def OpenInfroDB(self):
        self.data = TinyDB('config/beijing.json')
        self.table = self.data.table('config')

    def Insert(self, id, name, tag):
        self.table.insert({'id': id, 'name': name, 'tag': tag})

    def Search(self, id):
        Q = Query()
        return self.table.search(Q.id == int(id))


class UserDBoperate:
    def OpenUserDB(self):
        self.data = TinyDB('config/user.json')
        self.table = self.data.table('user')
        print("OpenDB")

    def Insert(self, user, pw, like):
        self.table.insert({"user": user, 'pw': pw, 'like': like})

    def Search(self, id):
        Q = Query()
        return self.table.search(Q.user == int(id))


class Learn:
    def Train(self, id):
        Infor = InfroDBoperate()
        Infor.OpenInfroDB()
        Config=ConfigDBoperate()
        Config.OpenInfroDB()
        UserID=Config.GetAllUserID()[0][]
        InforID=Config.GetAllInforID()
        Config = .Search(id)
        print(Config[0]['tag'])
        print(Config[0]['name'])


A = InfroDBoperate()
A.OpenInfroDB()
A.Insert(1, u"故宫博物院", [1, 0, 1, 0, 1, 1])
B = Learn()
B.Train(1)
