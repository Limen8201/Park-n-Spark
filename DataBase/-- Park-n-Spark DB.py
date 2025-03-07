import sqlite3

conn = sqlite3.connect("Park-n-Spark\DataBase\Park-n-Spark.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS userInfo(
        userID INTEGER PRIMARY KEY,
        password TEXT NOT NULL,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        emailAddress TEXT NOT NULL,
        vehicleType TEXT NOT NULL,
        vehicleModel TEXT NOT NULL
    )
''')

cursor.execute('''
    create table if not exists parkingSlot(
        parkingSLotID INTEGER PRIMARY KEY AUTOINCREMENT,
        parkingLocation TEXT NOT NULL,
        isAvailable BOOLEAN NOT NULL
    )
''')

cursor.execute('''
    create table if not exists parkingInfo(
        parkingID INTEGER PRIMARY KEY AUTOINCREMENT,
        parkingSlotID INTEGER N  OT NULL,
        parkingStartTime TEXT NOT NULL,
        parkingEndTime TEXT NOT NULL,
        foreign key (parkingSlotID) references parkingSlot(parkingSlotID)
    )
''')

cursor.execute('''
    create table if not exists userLocationInfo(
        userLocationInfoID INTEGER PRIMARY KEY AUTOINCREMENT,
        userID INTEGER NOT NULL,
        locationName TEXT NOT NULL,
        latitude DECIMAL(8,6) NOT NULL,
        longitude DECIMAL(9,6) NOT NULL,
        foreign key (userID) references userInfo(userID)
)
''')

cursor.execute('''
    create table if not exists parkingLocationInfo(
        parkingLocationID INTEGER PRIMARY KEY AUTOINCREMENT,
        parkingID INTEGER NOT NULL,
        locationName TEXT NOT NULL,
        latitude DECIMAL(8,6) NOT NULL,
        longitude DECIMAL(9,6) NOT NULL,
        foreign key (parkingID) references parkingInfo(parkingID)
    )
''')

cursor.execute('''
    create table if not exists paymentInfo(
        paymentID INTEGER PRIMARY KEY AUTOINCREMENT,
        userID INTEGER NOT NULL,
        parkingID INTEGER NOT NULL,
        paymentAmount DECIMAL(5,2) NOT NULL,
        paymentDate TEXT NOT NULL,
        foreign key (userID) references userInfo(userID),
        foreign key (parkingID) references parkingInfo(parkingID)
    )
''')

