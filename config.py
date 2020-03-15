# coding:utf-8
# DIALECT+DRIVER://USERNAME:PASSWORD@HOST:PORT/DATABSE
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = '1234'
HOST = '122.51.189.232'
PORT = '3306'
DATABASE = 'baobab'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
