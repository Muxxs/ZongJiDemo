# coding=utf-8
from tinydb import TinyDB
from tinydb.queries import Query, where
import pymysql

Host = "140.143.3.101"
UserName = 'Zongji'
Passwd = "DwybnAKDSwhk6NWc"
DB = 'Zongji'
conn = pymysql.connect(host=Host, user=UserName, passwd=Passwd, db=DB, charset='utf8')


class ConfigDBoperate:  # Data for json's
    def __init__(self):
        self.data = TinyDB('config/config.json')
        self.table = self.data.table('config')
        self.cursor = conn.cursor()

    def GetAllUserID(self):
        SQL = 'SELECT * FROM Config where Name = "UserID"'
        self.cursor.execute(SQL)
        return self.cursor.fetchall()[0][1]

    def GetAllInforID(self):
        SQL = 'SELECT * FROM Config where Name = "InforID"'
        self.cursor.execute(SQL)
        return self.cursor.fetchall()[0][1]

    def GetAllPassID(self):
        SQL = 'SELECT * FROM Config where Name = "PassID"'
        self.cursor.execute(SQL)
        return self.cursor.fetchall()[0][1]

    def CreateTable(self):
        SQL = 'INSERT INTO Config (Name , Content) VALUES ("UserID", 0 )'
        self.cursor.execute(SQL)
        SQL = 'INSERT INTO Config (Name , Content) VALUES ("PassID", 0 )'
        self.cursor.execute(SQL)
        SQL = 'INSERT INTO Config (Name , Content) VALUES ("InforID", 0 )'
        self.cursor.execute(SQL)

    def UserIDPlus(self):
        Now = self.GetAllUserID()
        SQL = 'UPDATE Config SET Content = %d WHERE Name="UserID"' % (Now + 1)
        self.cursor.execute(SQL)
        conn.commit()

    def InforIDPlus(self):
        Now = self.GetAllInforID()
        SQL = 'UPDATE Config SET Content = %d WHERE Name="InforID"' % (Now + 1)
        self.cursor.execute(SQL)
        conn.commit()

    def PassIDPlus(self):
        Now = self.GetAllUserID()
        SQL = 'UPDATE Config SET Content = %d WHERE Name="PassID"' % (Now + 1)
        self.cursor.execute(SQL)
        conn.commit()


class InfroDBoperate:  # Scenic spot Information
    def __init__(self):
        self.cursor = conn.cursor()

    def Insert(self, name: str, tag: []):
        list = ''
        for i in tag: list += str(i) + "-"
        list = list[:-1]
        A = ConfigDBoperate()
        SQL = 'INSERT INTO Beijing (ID,name, tag) VALUES (%d, "%s","%s")' % (
            A.GetAllInforID() + 1, name, list)
        self.cursor.execute(SQL)
        conn.commit()
        D = ConfigDBoperate()
        D.InforIDPlus()

    def Search(self, id: int):
        SQL = 'SELECT * FROM Beijing where ID = %d' % id
        self.cursor.execute(SQL)
        return self.cursor.fetchall()[0]


class UserDBoperate:  # User Database Operations
    def __init__(self):
        self.cursor = conn.cursor()

    def Insert(self, user: str, pw: str, like: []):  # Sign Up
        list = ''
        for i in like: list += str(i) + "-"
        list = list[:-1]
        A = ConfigDBoperate()
        SQL = 'INSERT INTO Beijing (ID,User, pw,like) VALUES (%d, "%s","%s","%s")' % (
            A.GetAllUserID() + 1, user, pw, list)
        self.cursor.execute(SQL)
        conn.commit()
        D = ConfigDBoperate()
        D.UserIDPlus()

    def Search(self, id: int):  # Get information
        SQL = 'SELECT * FROM User where ID = %d' % id
        self.cursor.execute(SQL)
        return self.cursor.fetchall()[0]


class PassageDBoperate:  # Passages Database Operations
    def __init__(self):
        self.cursor = conn.cursor()

    def Insert(self, passage: str, AuthorID: int, time: str, PlaceID: []):
        list = ''
        for i in PlaceID: list += str(i) + "-"
        list = list[:-1]
        SQL = 'INSERT INTO Passage (PassageID,AuthorID, Time,PlaceID,Passage) VALUES (%d, %d,"%s","%s","%s")' % (
            A.GetAllPassID() + 1, AuthorID, time, list, passage)
        self.cursor.execute(SQL)
        conn.commit()
        D = ConfigDBoperate()
        D.PassIDPlus()

    def Search(self, id: int):
        SQL = 'SELECT * FROM Passage where PassageID = %d' % id
        self.cursor.execute(SQL)
        return self.cursor.fetchall()[0]


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