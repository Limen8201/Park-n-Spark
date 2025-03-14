import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QLineEdit, QInputDialog
from PySide6.QtUiTools import QUiLoader
from ui_form_park import Ui_Widget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from user import User
from parkingSlot import ParkingSlot
from paymentInfo import PaymentInfo
from parkingInfo import ParkingInfo
from logHistory import LogHistory
import sqlite3
from functools import partial



conn = sqlite3.connect("D:\JM\VS Code\Park-n-Spark\DataBase\Park-n-Spark.db")
cursor = conn.cursor()

class Parking(QWidget):
    def __init__(self, app_instance, dashboard_window, parent=None):
        super().__init__(parent)
        self.layout = Ui_Widget()
        self.layout.setupUi(self)
        self.layout.Warning1.hide()
        self.layout.Warning2.hide()
        self.layout.reserveSpot.hide()
        self.user_data = {}
        self.selected_spot = None
        self.dashboard_window = dashboard_window
        self.app_instance = app_instance
        self.find_parking_spot()
        
        print("Icon exists:", os.path.exists("D:\JM\VS Code\Park-n-Spark\source code\car.png"))
        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "D:\JM\VS Code\Park-n-Spark\source code\car.png"))

        for i in range(1, 11):
            car_spot = self.findChild(QPushButton, f"carSpot_{i}")
            if car_spot:
                car_spot.setIcon(QIcon(icon_path))  # Set icon manually
                car_spot.setIconSize(QSize(100, 100))  

        print("Icon exists1:", os.path.exists("D:\JM\VS Code\Park-n-Spark\source code\Main\motorcycle.png"))
        icon_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "D:\JM\VS Code\Park-n-Spark\source code\Main\motorcycle.png"))

        for i in range(11, 21):
            car_spot = self.findChild(QPushButton, f"carSpot_{i}")
            if car_spot:
                car_spot.setIcon(QIcon(icon_path1))  # Set icon manually
                car_spot.setIconSize(QSize(80, 80))
        
    def find_parking_spot(self):
        self.car_spots = []
        confirm_spot = self.findChild(QPushButton, f"confirmSpot")

        for i in range(1, 21):
            car_spot = self.findChild(QPushButton, f"carSpot_{i}")
            if car_spot:
                car_spot.setCheckable(True)
                self.car_spots.append(car_spot)
                cursor.execute("SELECT isAvailable FROM parkingSlot WHERE parkingSlotName = ?", (car_spot.objectName(),))
                result = cursor.fetchone()
                if result and result[0] == 0:  # If spot is reserved
                    car_spot.setChecked(True)
                    car_spot.setEnabled(False)
                car_spot.clicked.connect(partial(self.validateSpot, car_spot))

        if confirm_spot:
            confirm_spot.clicked.connect(lambda: self.reserveSpot())

    def validateSpot(self, car_spot):
        for spot in self.car_spots:
            if spot != car_spot:
                spot.setChecked(False)
        self.selected_spot = car_spot

        warn_Okay = self.findChild(QPushButton, f"warning1Okay")
        if warn_Okay:
            warn_Okay.clicked.connect(lambda: self.layout.Warning1.hide())


    def reserveSpot(self):
        if not self.selected_spot:
            self.layout.Warning2.show()
            warn_Okay = self.findChild(QPushButton, "warning1Okay_2")
            if warn_Okay:
                warn_Okay.clicked.connect(lambda: self.layout.Warning2.hide())
            return

        self.layout.reserveSpot.show()

        cancel_button = self.findChild(QPushButton, f"cancelButton")
        if cancel_button:
            cancel_button.clicked.connect(self.cancelReserve)

        reserve_button = self.findChild(QPushButton, f"reserveButton")
        if reserve_button:
            print("✅ Reserve button clicked!") 
            reserve_button.clicked.connect(lambda: self.app_instance.reserved())
            reserve_button.clicked.connect(lambda: self.payment(self.selected_spot))

    def cancelReserve(self, car_spot):
        if self.selected_spot:
                self.selected_spot.setChecked(False)
        self.selected_spot = None
        self.layout.reserveSpot.hide()

    def payment(self, car_spot):
        self.layout.reserveSpot.hide()
        self.selected_spot.setChecked(True)

        cursor.execute("SELECT parkingSlotName FROM parkingSlot WHERE parkingSlotName = ?", (car_spot.objectName(),))
        result = cursor.fetchone()
        if result:  # If a slot with this name exists in the database
            slot_name_from_db = result[0]

        if self.selected_spot.objectName() == slot_name_from_db:
            # Update the parking slot availability
            cursor.execute("UPDATE parkingSlot SET isAvailable = 0 WHERE parkingSlotName = ?", (slot_name_from_db,))
            conn.commit()
            self.selected_spot.setEnabled(False)
            print(f"Spot {slot_name_from_db} reserved.")
        else:
            print("Spot not reserved")
    
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Parking()
    widget.show()
    sys.exit(app.exec())
