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
        parkingSlotName TEXT NOT NULL,
        isAvailable BOOLEAN NOT NULL
    )
''')

cursor.execute('''
    create table if not exists parkingInfo(
        parkingID INTEGER PRIMARY KEY AUTOINCREMENT,
        parkingSlotID INTEGER NOT NULL,
        parkingSlotName TEXT NOT NULL,
        parkingStartTime TEXT NOT NULL,
        parkingEndTime TEXT NOT NULL,
        foreign key (parkingSlotID) references parkingSlot(parkingSlotID)
        foreign key (parkingSlotName) references parkingSlot(parkingSlotName)
    )
''')

cursor.execute('''
    create table if not exists logHistory(
        logID INTEGER PRIMARY KEY AUTOINCREMENT,
        userID INTEGER NOT NULL,
        parkingID INTEGER NOT NULL,
        parkingName TEXT NOT NULL,
        parkingStartTime TEXT NOT NULL,
        parkingEndTime TEXT NOT NULL,
        foreign key (userID) references userInfo(userID),
        foreign key (parkingID) references parkingInfo(parkingID)
    )
''')

cursor.execute('''
    create table if not exists paymentInfo(
        paymentID INTEGER PRIMARY KEY AUTOINCREMENT,
        userID INTEGER NOT NULL,
        parkingID INTEGER NOT NULL,
        parkingName TEXT NOT NULL,
        paymentAmount DECIMAL(5,2) NOT NULL,
        paymentDate TEXT NOT NULL,
        foreign key (userID) references userInfo(userID),
        foreign key (parkingID) references parkingInfo(parkingID),
        foreign key (parkingName) references parkingInfo(parkingName)
    )
''')