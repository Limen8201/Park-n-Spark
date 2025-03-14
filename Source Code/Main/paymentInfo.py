import sqlite3
import parkingInfo
import parkingSlot
import user
conn = sqlite3.connect("D:\JM\VS Code\Park-n-Spark\DataBase\Park-n-Spark.db")
cursor = conn.cursor()

class PaymentInfo:
    def __init__ (self, userID, parkingID, parkingName, paymentAmount, paymentDate):
        self.userID = userID
        self.parkingID = parkingID
        self.parkingName = parkingName
        self.paymentAmount = paymentAmount
        self.paymentDate = paymentDate

    def userID(self):
        cursor.execute('SELECT userID FROM paymentInfo WHERE paymentID = ?', (self.userID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def parkingID(self):
        cursor.execute('SELECT parkingID FROM paymentInfo WHERE paymentID = ?', (self.parkingID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def parkingName(self):
        cursor.execute('SELECT parkingName FROM paymentInfo WHERE paymentID = ?', (self.parkingID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def paymentAmount(self):
        cursor.execute('SELECT paymentAmount FROM paymentInfo WHERE paymentID = ?', (self.parkingID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def paymentDate(self):
        cursor.execute('SELECT paymentDate FROM paymentInfo WHERE paymentID = ?', (self.parkingID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def addPayment(self):
        cursor.execute('''
            INSERT INTO paymentInfo (userID, parkingID, parkingName, paymentAmount, paymentDate)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.userID, self.parkingID, self.parkingName, self.paymentAmount, self.paymentDate))
        conn.commit()

    def deletePayment(self, paymentID):
        cursor.execute('DELETE FROM paymentInfo WHERE paymentID = ?', (paymentID,))
        conn.commit()

    def updatePayment(self):
        cursor.execute('''
            UPDATE paymentInfo
            SET userID = ?, parkingID = ?, parkingName = ?, paymentAmount = ?, paymentDate = ?
            WHERE paymentID = ?
        ''', (self.userID, self.parkingID, self.parkingName, self.paymentAmount, self.paymentDate, self.parkingID))
        conn.commit()

# test case
