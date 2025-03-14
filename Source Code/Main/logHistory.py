import sqlite3
import parkingInfo
import parkingSlot
import user
conn = sqlite3.connect("D:\JM\VS Code\Park-n-Spark\DataBase\Park-n-Spark.db")
cursor = conn.cursor()

class LogHistory:
    def __init__ (self, userID, parkingID, parkingName, startTime, endTime):
        self.userID = userID
        self.parkingID = parkingID
        self.parkingName = parkingName
        self.startTime = startTime
        self.endTime = endTime

    def userID(self):
        cursor.execute('SELECT userID FROM logHistory WHERE logID = ?', (self.userID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def parkingID(self):
        cursor.execute('SELECT parkingID FROM logHistory WHERE logID = ?', (self.parkingID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def parkingName(self):
        cursor.execute('SELECT parkingName FROM logHistory WHERE logID = ?', (self.parkingID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def startTime(self):
        cursor.execute('SELECT parkingStartTime FROM logHistory WHERE logID = ?', (self.parkingID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def endTime(self):
        cursor.execute('SELECT parkingEndTime FROM logHistory WHERE logID = ?', (self.parkingID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def addLog(self):
        cursor.execute('''
            INSERT INTO logHistory (userID, parkingID, parkingName, parkingStartTime, parkingEndTime)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.userID, self.parkingID, self.parkingName, self.startTime, self.endTime))
        conn.commit()

    def deleteLog(self, logID):
        cursor.execute('DELETE FROM logHistory WHERE logID = ?', (logID,))
        conn.commit()

    def updateLog(self):
        cursor.execute('''
            UPDATE logHistory
            SET userID = ?, parkingID = ?, parkingName = ?, parkingStartTime = ?, parkingEndTime = ?
            WHERE logID = ?
        ''', (self.userID, self.parkingID, self.parkingName, self.startTime, self.endTime, self.parkingID))
        conn.commit()

# test case
