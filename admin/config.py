#-*- coding:utf-8 -*- 



#-- db config --
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWD = "123456"
DB_NAME = "admindb"




#-- app config --
DEBUG = True
SECRET_KEY = "dev_key_of_admin"
SESSION_COOKIE_NAME = "pastme"
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30

SITE_COOKIE = "adminck"