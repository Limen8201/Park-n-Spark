from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QLineEdit, QDialog, QInputDialog
import sqlite3
from user import User
from PyQt5.QtGui import QPixmap

conn = sqlite3.connect(r"C:/Users/ethan/Downloads/Park-n-Spark/DataBase/Park-n-Spark.db")
cursor = conn.cursor()

class ParkingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Park & Spark - Parking System")
        self.setGeometry(100, 100, 1000, 1000)  #
        self.layout = QVBoxLayout()
        self.user_data = {}
        self.total_hours = 0
        self.payment_mode = None
        self.__widgetInit__()

    def __widgetInit__(self):
        self.clear_layout()
        self.label = QLabel("Welcome to Park & Spark")
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(self.label)

        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.show_signup_page)
        self.layout.addWidget(self.signup_button)

        self.signin_button = QPushButton("Sign In")
        self.signin_button.clicked.connect(self.show_signin_page)
        self.layout.addWidget(self.signin_button)

        self.guest_button = QPushButton("Log in as Guest")
        self.layout.addWidget(self.guest_button)

        self.setLayout(self.layout)

    def show_signup_page(self):
        self.clear_layout()

        self.label = QLabel("Sign Up")
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(self.label)

        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText("First Name")
        self.layout.addWidget(self.first_name)

        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText("Last Name")
        self.layout.addWidget(self.last_name)

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email Address")
        self.layout.addWidget(self.email)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password)

        self.car_type = QLineEdit()
        self.car_type.setPlaceholderText("Car Type")
        self.layout.addWidget(self.car_type)

        self.car_model = QLineEdit()
        self.car_model.setPlaceholderText("Car Model")
        self.layout.addWidget(self.car_model)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.validate_registration)
        self.layout.addWidget(self.register_button)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.__widgetInit__)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def validate_registration(self):
        if not self.first_name.text() or not self.last_name.text() or not self.email.text() or not self.password.text() or not self.car_type.text() or not self.car_model.text():
            QMessageBox.warning(self, "Error", "All fields must be filled!")
        else:
            self.user_data = User(self.password.text(),
                                self.first_name.text(),
                                self.last_name.text(),
                                self.car_type.text(),
                                self.car_model.text(),
                                self.email.text())
            
            self.user_data.register()
            self.show_registration_success()

    def show_registration_success(self):
        QMessageBox.information(self, "Success", "You have been successfully registered!")
        self.show_signin_page()

    def show_signin_page(self):
        self.clear_layout()

        self.label = QLabel("Sign In")
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(self.label)

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email Address")
        self.layout.addWidget(self.email)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password)

        self.login_button = QPushButton("Log In")
        self.login_button.clicked.connect(self.validate_login)
        self.layout.addWidget(self.login_button)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.__widgetInit__)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def validate_login(self):
        cursor.execute('SELECT * FROM userInfo WHERE emailAddress = ? AND password = ?', (self.email.text(), self.password.text()))
        if not self.email.text() or not self.password.text():
            QMessageBox.warning(self, "Error", "All fields must be filled!")
            print("Login failed")
        elif not cursor.fetchone():  # An empty result evaluates to False.
            QMessageBox.information(self, "Login Failed", "Invalid email or password")
            print("Login failed")
        else:
            print("Login successful")
            self.show_parking_dashboard(self.email.text())
        

    def show_parking_dashboard(self, email):
        self.clear_layout()
        cursor.execute('SELECT * FROM userInfo WHERE emailAddress = ?', (email,))
        user = cursor.fetchone()
        first, last = user[2], user[3] # Get firstName and lastName; column in database
        self.label = QLabel(f"Welcome, {first} {last}!")
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(self.label)

        model, type = user[6], user[5] # Get Model and Type; column in database
        self.car_info = QLabel(f"Car Model: {model}\nCar Type: {type}")
        self.layout.addWidget(self.car_info)

        self.vacancy_button = QPushButton("View Number of Vacancy")
        self.layout.addWidget(self.vacancy_button)

        self.pay_button = QPushButton("Pay")
        self.pay_button.clicked.connect(self.show_payment_window)
        self.layout.addWidget(self.pay_button)

        self.find_parking_button = QPushButton("Find Parking Spot")
        self.find_parking_button.clicked.connect(self.find_parking_spot)
        self.layout.addWidget(self.find_parking_button)

        self.cancel_button = QPushButton("Cancellation")
        self.cancel_button.clicked.connect(self.cancel_parking)
        self.layout.addWidget(self.cancel_button)

        self.reserve_button = QPushButton("Reservation")
        self.layout.addWidget(self.reserve_button)

        self.bookmark_button = QPushButton("Bookmark")
        self.layout.addWidget(self.bookmark_button)

        self.history_button = QPushButton("View History")
        self.layout.addWidget(self.history_button)

        self.logout_button = QPushButton("Log Out")
        self.layout.addWidget(self.logout_button)
        self.logout_button.clicked.connect(self.logout)

        self.setLayout(self.layout)

    def cancel_parking(self):
        if self.total_hours == 0:
            QMessageBox.warning(self, "Error", "You should find a parking spot first!")
        else:
            self.total_hours = 0  
            self.payment_mode = None  
            QMessageBox.information(self, "Success", "Successfully cancelled parking!")

    def find_parking_spot(self):
        if self.total_hours > 0:
            reply = QMessageBox.question(self, "Add More Hours", "Do you want to add more parking hours?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                return
            
        hours, ok = QInputDialog.getInt(self, "Find Parking Spot", "Enter hours to park:")
        if ok and hours > 0:
            self.total_hours += hours
            QMessageBox.information(self, "Success", f"Successfully added {hours} hours to your current parking. Total hours: {self.total_hours}.")
        else:
            QMessageBox.warning(self, "Error", "Invalid number of hours!")


    def show_payment_window(self):
        if self.total_hours == 0:
            QMessageBox.warning(self, "Error", "Please find a parking spot first!")
            return
        
        self.payment_window = QWidget()
        self.payment_window.setWindowTitle("Payment")
        self.payment_layout = QVBoxLayout()

        rate = 20  # Pesos per hour
        self.total_amount = self.total_hours * rate

        self.payment_label = QLabel(f"Total Hours Parked: {self.total_hours} hours")
        self.rate_label = QLabel(f"Rate: {rate} pesos per hour")
        self.total_amount_label = QLabel(f"Total Amount: {self.total_amount} pesos")

        self.payment_layout.addWidget(self.payment_label)
        self.payment_layout.addWidget(self.rate_label)
        self.payment_layout.addWidget(self.total_amount_label)

        self.gcash_button = QPushButton("Pay with GCash")
        self.gcash_button.clicked.connect(lambda: self.select_payment_mode("GCash"))
        self.payment_layout.addWidget(self.gcash_button)

        self.cash_button = QPushButton("Pay with Cash")
        self.cash_button.clicked.connect(lambda: self.select_payment_mode("Cash"))
        self.payment_layout.addWidget(self.cash_button)

        self.payment_window.setLayout(self.payment_layout)
        self.payment_window.show()
    
    def select_payment_mode(self, mode):
        if self.payment_mode:
            QMessageBox.warning(self, "Error", "You can only choose one payment method!")
            return
        
        self.payment_mode = mode
        if mode == "GCash":
            self.show_gcash_payment()
        elif mode == "Cash":
            self.show_cash_payment()

    def show_gcash_payment(self):
        self.gcash_window = QWidget()
        self.gcash_window.setWindowTitle("GCash Payment")
        self.gcash_layout = QVBoxLayout()

        self.gcash_label = QLabel("Scan the QR code to pay via GCash")
        self.gcash_qr = QLabel()
        pixmap = QPixmap(r"C:\Users\ethan\Downloads\Park-n-Spark\GCASH\gcash.png")
        pixmap = pixmap.scaled(500, 800)
        self.gcash_qr.setPixmap(pixmap)

        self.gcash_layout.addWidget(self.gcash_label)
        self.gcash_layout.addWidget(self.gcash_qr)

        self.confirm_payment_button = QPushButton("Mark as Paid")
        self.confirm_payment_button.clicked.connect(self.confirm_payment)
        self.gcash_layout.addWidget(self.confirm_payment_button)

        self.gcash_window.setLayout(self.gcash_layout)
        self.gcash_window.show()
 
    def show_cash_payment(self):
        cash_given, ok = QInputDialog.getDouble(self, "Cash Payment", "Enter cash amount:")
        if not ok:
            return  # Cancelled input

        if cash_given >= self.total_amount:
            change = cash_given - self.total_amount
            QMessageBox.information(self, "Change", f"Your change: {change} pesos")
            self.confirm_payment()
        else:
            QMessageBox.warning(self, "Error", "Insufficient amount!")

    def confirm_payment(self):
        self.total_hours = 0  # Clear parking hours after successful payment
        self.payment_mode = None
        QMessageBox.information(self, "Success", "Payment successfully received!")
        self.payment_window.close()
        if hasattr(self, 'gcash_window'):
            self.gcash_window.close()
        if hasattr(self, 'cash_window'):
            self.payment_window.close()

    def logout(self):
        self.label = QLabel("Are you sure you want to log out?")
        self.layout.addWidget(self.label)

        self.yes_button = QPushButton("Yes")
        self.layout.addWidget(self.yes_button)
        self.yes_button.clicked.connect(self.__widgetInit__)

        self.no_button = QPushButton("No")
        self.layout.addWidget(self.no_button)
        self.no_button.clicked.connect(self.show_parking_dashboard)

    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

if __name__ == "__main__":
    app = QApplication([])
    window = ParkingApp()
    window.show()
    app.exec_()
