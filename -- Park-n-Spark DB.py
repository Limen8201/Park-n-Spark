import sqlite3

conn = sqlite3.connect("D:\JM\VS Code\Park-n-Spark-main\Park-n-Spark.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS userInfo(
        userID INTEGER PRIMARY KEY AUTOINCREMENT,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        emailAddress TEXT NOT NULL,
        carType TEXT NOT NULL
    )
''')

cursor.execute('''
    create table if not exists parkingInfo(
        parkingID INTEGER PRIMARY KEY AUTOINCREMENT,
        userID INTEGER NOT NULL,
        parkingLocation TEXT NOT NULL,
        parkingStartTime TEXT NOT NULL,
        parkingEndTime TEXT NOT NULL,
        isAvailable BOOLEAN NOT NULL,
        FOREIGN KEY (userID) REFERENCES userInfo(userID)
    )
''')

cursor.execute('''
    create table if not exists locationInfo(
        locationID INTEGER PRIMARY KEY AUTOINCREMENT,
        parkingID INTEGER NOT NULL,
        userID INTEGER NOT NULL,
        locationName TEXT NOT NULL,
        latitude DECIMAL(8,6) NOT NULL,
        longitude DECIMAL(9,6) NOT NULL,
        foreign key (parkingID) references parkingInfo(parkingID),
        foreign key (userID) references userInfo(userID)
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
