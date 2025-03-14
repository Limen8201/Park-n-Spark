import sqlite3

conn = sqlite3.connect("D:\JM\VS Code\Park-n-Spark\DataBase\Park-n-Spark.db")
cursor = conn.cursor()

class User:
    def __init__ (self, password, first, last, carType, carModel, emailAddress):
        self.password = password
        self.first = first
        self.last = last
        self.carType = carType
        self.carModel = carModel
        self.emailAddress = emailAddress

    def fullName(self):
        cursor.execute('SELECT firstName, lastName FROM userInfo WHERE userID = ?', (self.userID,))
        return '{} {}'.format(cursor.fetchone()[0], cursor.fetchone()[1])
    
    def password(self):
        cursor.execute('SELECT password FROM userInfo WHERE userID = ?', (self.userID,))
        return '{}'.format(cursor.fetchone()[0])

    def firstName(self):
        cursor.execute('SELECT firstName FROM userInfo WHERE userID = ?', (self.userID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def lastName(self):
        cursor.execute('SELECT lastName FROM userInfo WHERE userID = ?', (self.userID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def carType(self):
        cursor.execute('SELECT vechicleType FROM userInfo WHERE userID = ?', (self.userID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def carModel(self):
        cursor.execute('SELECT vehicleModel FROM userInfo WHERE userID = ?', (self.userID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def emailAddress(self):
        cursor.execute('SELECT emailAddress FROM userInfo WHERE userID = ?', (self.userID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def register(self):
        cursor.execute('''
            INSERT INTO userInfo (password, firstName, lastName, vehicleType, vehicleModel, emailAddress)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.password, self.first, self.last, self.carType, self.carModel, self.emailAddress))
        conn.commit()
        
    def userID(self):
        cursor.execute('SELECT userID FROM userInfo WHERE emailAddress = ?', (self.emailAddress,))
        return '{}'.format(cursor.fetchone()[0])

    def delete(self):
        cursor.execute('DELETE FROM userInfo WHERE userID = ?', (self.userID,))
        conn.commit()

# test case




