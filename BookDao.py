import mysql.connector
import dbconfig as cfg

class BookDAO:
   
    db=""
    
    def __init__(self):    # dbconfig allows us to access our SQL account with our details.
        self.db = mysql.connector.connect(   # mysql.connector establishes the connection. 
        host=       cfg.mysql['host'],
        user=       cfg.mysql['user'],
        password=   cfg.mysql['password'],
        database=   cfg.mysql['database'])
    
    def create(self, values):
        cursor = self.db.cursor()    # Cursor allows us to execute SQL commands. In this case , from the database 'db'.
        sql="insert into book (title,author, price) values (%s,%s,%s)"    # SQL statement.
        cursor.execute(sql, values)    # Execute method takes our SQL statement and values as parameters. 
        self.db.commit()    # commit() method makes pending statements permanent for our database in SQL.
        return cursor.lastrowid    # Returns ID of the last row in our table. 

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from book"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from book where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update book set title= %s,author=%s, price=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
    
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from book where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','Title','Author', "Price"]
        item = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item
