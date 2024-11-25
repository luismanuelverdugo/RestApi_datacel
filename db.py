import pymysql

try:
    connexion=pymysql.connect(host="localhost",
                              user="root", password="",
                              database="datacel")
except:
    print("------ Error:{err}")
