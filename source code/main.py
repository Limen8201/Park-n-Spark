from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QLineEdit
import sqlite3
from user import User

conn = sqlite3.connect("Park-n-Spark\DataBase\Park-n-Spark.db")
cursor = conn.cursor()

class ParkingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Park & Spark - Parking System")
        self.setGeometry(100, 100, 1000, 1000)  # Increased window size further
        self.layout = QVBoxLayout()
        self.user_data = {}  # Dictionary to store user info
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
        self.label = QLabel(f"Welcome {first} {last}")
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(self.label)

        model, type = user[6], user[5] # Get Model and Type; column in database
        self.car_info = QLabel(f"Car Model: {model}, Car Type: {type}")
        self.layout.addWidget(self.car_info)

        self.vacancy_button = QPushButton("View Number of Vacancy")
        self.layout.addWidget(self.vacancy_button)

        self.pay_button = QPushButton("Pay")
        self.layout.addWidget(self.pay_button)

        self.print_receipt_button = QPushButton("Print Receipt")
        self.layout.addWidget(self.print_receipt_button)

        self.find_parking_spot_button = QPushButton("Find Parking Spot")
        self.layout.addWidget(self.find_parking_spot_button)

        self.cancel_button = QPushButton("Cancellation")
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
