# coding:utf-8
import MySQLdb


class MySQL(object):
    def __init__(self):
        self.db = None
        self.cursor = None

    def connect(self, ip, username, password, database, charset='utf8'):
        self.db = MySQLdb.connect(ip, username, password, database, charset=charset)
        self.cursor = self.db.cursor()

    def execute(self, sqlcmd):
        self.cursor.execute(sqlcmd)
        data = self.cursor.fetchall()
        return data

    def execute_no_result(self, sqlcmd):
        self.cursor.execute(sqlcmd)

    def close(self):
        self.db.close()
