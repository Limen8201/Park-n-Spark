import sqlite3

conn = sqlite3.connect("Park-n-Spark\DataBase\Park-n-Spark.db")
cursor = conn.cursor()

class parkingLocationInfo:
    def __init__ (self,locationName, latitude, longitude):
        self.locationName = locationName
        self.latitude = latitude
        self.longitude = longitude

    def locationName(self):
        cursor.execute('SELECT locationName FROM parkingLocationInfo WHERE locID = ?', (self.locID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def latitude(self):
        cursor.execute('SELECT latitude FROM parkingLocationInfo WHERE locID = ?', (self.locID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def longitude(self):
        cursor.execute('SELECT longitude FROM parkingLocationInfo WHERE locID = ?', (self.locID,))
        return '{}'.format(cursor.fetchone()[0])
    
    def addLoc(self):
        cursor.execute('''
            INSERT INTO parkingLocationInfo (locationName, latitude, longitude)
            VALUES (?, ?, ?)
        ''', (self.locationName, self.latitude, self.longitude))
        conn.commit()

    def locID(self):
        cursor.execute('SELECT locID FROM parkingLocationInfo WHERE locationName = ?', (self.locationName,))
        return '{}'.format(cursor.fetchone()[0])
    
    def delete(self):
        cursor.execute('DELETE FROM parkingLocationInfo WHERE locID = ?', (self.locID,))
        conn.commit()

# test case
p1 = parkingLocationInfo('locationName', 'latitude', 'longitude')
p1.addLoc()