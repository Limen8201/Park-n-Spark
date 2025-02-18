import sqlite3

conn = sqlite3.connect("Park-n-Spark\DataBase\Park-n-Spark.db")
cursor = conn.cursor()

class User:
    def __init__ (self, UID, first, last, carType, emailAddress):
        self.UID = UID
        self.first = first
        self.last = last
        self.carType = carType
        self.emailAddress = emailAddress

    def fullName(self):
        cursor.execute('SELECT firstName, lastName FROM userInfo WHERE userID = ?', (self.userID,))
        return '{} {}'.format(cursor.fetchone()[0], cursor.fetchone()[1])
    
    def firstName(self):
        cursor.execute('SELECT firstName FROM userInfo WHERE userID = ?', (self.userID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def lastName(self):
        cursor.execute('SELECT lastName FROM userInfo WHERE userID = ?', (self.userID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def carType(self):
        cursor.execute('SELECT vechicleType FROM userInfo WHERE userID = ?', (self.userID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def emailAddress(self):
        cursor.execute('SELECT emailAddress FROM userInfo WHERE userID = ?', (self.userID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def register(self):
        cursor.execute('INSERT OR REPLACE INTO userInfo (UID, firstName, lastName, carType, emailAddress) VALUES (?, ?, ?, ?, ?)', 
                       (self.UID, self.first, self.last, self.carType, self.emailAddress))
        conn.commit()
        return '{} {} {} {}'.format(self.first, self.last, self.carType, self.emailAddress)
        
    def userID(self):
        cursor.execute('SELECT userID FROM userInfo WHERE UID = ?', (self.emailAddress,))
        return '{}'.format(cursor.fetchone()[0])


# test case
p1 = User(100, 'John', 'Doe', 'SUV', '@ako')
p1.register()
print(p1.register)
print(p1.carType)
print(p1.emailAddress)
