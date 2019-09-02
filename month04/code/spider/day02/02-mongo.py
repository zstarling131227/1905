import pymongo
database='maoyandb'
table='filmset'
conn=pymongo.MongoClient('localhost',27017)
# db=conn['maoyandb']
db=conn[database]
# myset=db['filmset']
myset=db[table]
myset.insert_one({'name':'Tiechui'})
myset.insert_many({'name':'wangba'},{'name':'ret'})
