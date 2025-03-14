import sqlite3
import parkingInfo
conn = sqlite3.connect("D:\JM\VS Code\Park-n-Spark\DataBase\Park-n-Spark.db")
cursor = conn.cursor()

class ParkingInfo:
    def __init__ (self, slotID, slotName, startTime, endTime):
        self.slotID = slotID
        self.slotName = slotName
        self.startTime = startTime
        self.endTime = endTime

    def slotID(self):
        cursor.execute('SELECT parkingSlotID FROM parkingInfo WHERE parkingID = ?', (self.slotID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def slotName(self):
        cursor.execute('SELECT parkingSlotName FROM parkingInfo WHERE parkingID = ?', (self.slotID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def startTime(self):
        cursor.execute('SELECT parkingStartTime FROM parkingInfo WHERE parkingID = ?', (self.slotID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def endTime(self):
        cursor.execute('SELECT parkingEndTime FROM parkingInfo WHERE parkingID = ?', (self.slotID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def addParking(self):
        cursor.execute('''
            INSERT INTO parkingInfo (parkingSlotID, parkingSlotName, parkingStartTime, parkingEndTime)
            VALUES (?, ?, ?, ?)
        ''', (self.slotID, self.slotName, self.startTime, self.endTime))
        conn.commit()

    def deleteParking(self, parkingID):
        cursor.execute('DELETE FROM parkingInfo WHERE parkingID = ?', (parkingID,))
        conn.commit()

    def updateParking(self):
        cursor.execute('''
            UPDATE parkingInfo
            SET parkingSlotID = ?, parkingSlotName = ?, parkingStartTime = ?, parkingEndTime = ?
            WHERE parkingID = ?
        ''', (self.slotID, self.slotName, self.startTime, self.endTime, self.slotID))
        conn.commit()

# test case

    
    
