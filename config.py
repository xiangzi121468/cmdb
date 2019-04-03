DEBUG = True
#MySQL Database
HOST = '192.168.141.10'
PORT = '3306'
USERNAME = 'root'
PASSWORD = '121468wang'
DATABASE = 'cmdb'

DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset-utf8'.format(username=USERNAME,
                                                                                        password=PASSWORD,
                                                                                        host=HOST,
                                                                                        port=PORT,
                                                                                        db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False