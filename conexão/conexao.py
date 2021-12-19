#conexão

import mysql.connector
cnxn = mysql.connector.connect(host="sql10.freemysqlhosting.net", user="sql10459891", passwd="ZEVEuMyb52", db="sql10459891")
cursor = cnxn.cursor()