# coding=utf-8
from operation import *
from faker import Faker

f = Faker(locale='zh_CN')


class CreatFakeData:
    def InsertUserData(self, n):
        for i in range(n):
            passwd = ""
            like = []
            for i in range(8): passwd += f.random_element()
            for x in range(6): like.append(round(0.1 * f.random_digit(), 2))
            A = UserDBoperate()
            A.Insert(f.name(), passwd, like)
        Infor = Show()
        Infor.AllUser()

    def InsertInforData(self, n):
        for i in range(n):
            like = []
            for x in range(6): like.append(round(0.1 * f.random_digit(), 2))
            A = InforDBoperate()
            A.Insert(f.province()+f.city_suffix()+f.district()+f.street_name()+f.street_suffix(),like)
        Infor = Show()
        Infor.AllInfor()


C = CreatFakeData()
C.InsertInforData(20)
