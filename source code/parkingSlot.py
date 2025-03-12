import sqlite3
conn = sqlite3.connect("Park-n-Spark\DataBase\Park-n-Spark.db")
cursor = conn.cursor()

class ParkingSlot:
    def __init__ (self, slotID, slotName, isAvailable):
        self.slotID = slotID
        self.slotName = slotName
        self.isAvailable = isAvailable

    def slotID(self):
        cursor.execute('SELECT parkingSlotID FROM parkingSlot WHERE parkingSlotID = ?', (self.slotID,))
        return '{}'.format(cursor.fetchone()[0])

    def slotName(self):
        cursor.execute('SELECT parkingSlotName FROM parkingSlot WHERE parkingSlotID = ?', (self.slotName,))
        return '{}'.format(cursor.fetchone()[0])
    
    def isAvailable(self):
        cursor.execute('SELECT isAvailable FROM parkingSlot WHERE parkingSlotID = ?', (self.slotName,))
        return '{}'.format(cursor.fetchone()[0])
    
    def addSlot(self):
        cursor.execute('''
            INSERT INTO parkingSlot (parkingSlotName, isAvailable)
            VALUES (?, ?)
        ''', (self.slotName, self.isAvailable))
        conn.commit()

    def deleteSlot(self, parkingSlotID):
        cursor.execute('DELETE FROM parkingSlot WHERE parkingSlotID = ?', (parkingSlotID,))
        conn.commit()


    def updateSlot(self):
        cursor.execute('''
            UPDATE parkingSlot
            SET parkingSlotName = ?, isAvailable = ?
            WHERE parkingSlotID = ?
        ''', (self.slotName, self.isAvailable, self.slotID))
        conn.commit()

    def slotAvailable(self):
        cursor.execute('''
            UPDATE parkingSlot
            SET isAvailable = ?
            WHERE parkingSlotID = ?
        ''', ('True', self.slotID))
        conn.commit()

#test case
#for i in range(1, 21):  # Ensures all 20 slots are updated
 #   slot = ParkingSlot(i, f"carSpot_{i}", 1)
  #  slot.slotAvailable()


