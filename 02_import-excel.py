import pandas as pd
import sqlite3

db = sqlite3.connect('example.db')

#DataForm Object
#"small countries are beautiful"
# dfs = pd.read_excel('WDVP-Datasets.xlsx', sheet_name=None)
# print(dfs)
# for table, df in dfs.items():
#   if table == "small countries are beautiful":
#     df.to_sql(table, db)




# deleteSQLStatememnt = "DELETE from 'small countries are beautiful' where population=2018"




cursor = db.cursor()
# cursor.execute(deleteSQLStatememnt)
# for a in cursor:
#   print(a)

#List all the tables
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cursor.fetchall())

# db.commit()
df = pd.read_sql_query("select indicator, population from 'small countries are beautiful';", db)
print(df)
db.close()
