from PySide6.QtWidgets import QApplication, QMessageBox, QStackedWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QInputDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap
from widget import Parking
from user import User
from parkingSlot import ParkingSlot
from paymentInfo import PaymentInfo
from parkingInfo import ParkingInfo
from logHistory import LogHistory
import sqlite3
import sys
import os

conn = sqlite3.connect("D:\JM\VS Code\Park-n-Spark\DataBase\Park-n-Spark.db")
cursor = conn.cursor()

class ParkingApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.loader = QUiLoader()
        

        # Load all the UI files
        current_dir = os.path.dirname(os.path.realpath(__file__))

# Set the path to your UI files
        self.form_file = os.path.join(current_dir, "form.ui")
        self.login_file = os.path.join(current_dir, "login.ui")
        self.dashboard_file = os.path.join(current_dir, "ParkingDashboard.ui")
        self.signup_file = os.path.join(current_dir, "signup.ui")

        # Load windows
        self.form_window = self.loader.load(self.form_file)
        self.login_window = self.loader.load(self.login_file)
        self.dashboard_window = self.loader.load(self.dashboard_file)
        self.signup_window = self.loader.load(self.signup_file)

        self.parking_widget = Parking(self, self.dashboard_window)

        self.dashboard_window.setFixedSize(800, 600)
        self.form_window.setFixedSize(800, 600)
        self.login_window.setFixedSize(800, 600)
        self.signup_window.setFixedSize(800, 600)

        # Initialize parking data
        self.total_hours = 0
        self.payment_mode = None
        self.total_amount = 0
        self.receipt_window = None

        # Connect form buttons
        self.dashboard_window.findParkingButton.clicked.connect(self.show_parking)
        self.form_window.signin_button.clicked.connect(self.show_login)
        self.form_window.signup_button.clicked.connect(self.show_signup)
        self.form_window.guest_button.clicked.connect(self.show_guest_dashboard)


        # Connect signup buttons
        self.signup_window.backButton.clicked.connect(self.show_form)
        self.signup_window.registerButton.clicked.connect(self.register_user)

        # Connect login buttons
        self.login_window.backButton.clicked.connect(self.show_form)
        self.login_window.loginButton.clicked.connect(self.validate_login)

        # Connect dashboard buttons
        self.dashboard_window.logoutButton.clicked.connect(self.show_form)
        self.dashboard_window.cancelButton.clicked.connect(self.cancel_parking)
        self.dashboard_window.payButton.clicked.connect(self.show_payment_window)

        # Setup stacked widget
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.form_window)
        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.dashboard_window)
        self.stacked_widget.addWidget(self.signup_window)

        self.stacked_widget.setCurrentWidget(self.form_window)
        self.stacked_widget.show()

        # Create database if not exists
        self.create_table()

    def show_parking(self):
        self.parking_widget.show()

    def show_login(self):
        self.stacked_widget.setCurrentWidget(self.login_window)

    def show_signup(self):
        self.stacked_widget.setCurrentWidget(self.signup_window)

    def show_form(self):
        self.stacked_widget.setCurrentWidget(self.form_window)

    def show_guest_dashboard(self):
        self.stacked_widget.setCurrentWidget(self.dashboard_window)

    def show_dashboard(self, user_data):
        first_name = user_data[1]
        last_name = user_data[2]
        car_type = user_data[5]
        car_model = user_data[6]
        self.dashboard_window.welcomeLabel.setText(
            f"<p style='font-size:22px; font-weight:bold; margin-bottom: 20px;'>Welcome, {first_name} {last_name}!</p>"
            f"<p style='margin-top: 40px;'>Car Model: {car_model}</p>"
            f"<p>Car Type: {car_type}</p>"
        )
        self.stacked_widget.setCurrentWidget(self.dashboard_window)

    def register_user(self):
        first_name = self.signup_window.firstNameInput.text()
        last_name = self.signup_window.lastNameInput.text()
        email = self.signup_window.emailInput.text()
        password = self.signup_window.passwordInput.text()
        car_type = self.signup_window.carTypeInput.text()
        car_model = self.signup_window.carModelInput.text()

        if not all([first_name, last_name, email, password, car_type, car_model]):
            QMessageBox.warning(self.signup_window, "Warning", "Please fill out all fields.")
            return

        conn = sqlite3.connect("Park-n-Spark.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (first_name, last_name, email, password, car_type, car_model)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, email, password, car_type, car_model))
        conn.commit()
        conn.close()

        QMessageBox.information(self.signup_window, "Success", "Account created successfully!")
        self.show_login()

    def validate_login(self):
        email = self.login_window.findChild(QLineEdit, 'emailInput').text()
        password = self.login_window.findChild(QLineEdit, 'passwordInput').text()

        conn = sqlite3.connect("Park-n-Spark.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, first_name, last_name, email, password, car_type, car_model
            FROM users
            WHERE email = ? AND password = ?
        """, (email, password))
        user = cursor.fetchone()

        if user:
            self.show_dashboard(user)
        else:
            QMessageBox.warning(None, "Login Failed", "Invalid email or password.")

    def reserved(self):
        print("Reserved function triggered!")
        if self.total_hours > 0:
            reply = QMessageBox.question(self.dashboard_window, "Add More Hours",
                                         "Do you want to add more parking hours?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                return

        hours, ok = QInputDialog.getInt(self.dashboard_window, "Find Parking Spot", "Enter hours to park:")
        if ok and hours > 0:
            self.total_hours += hours
            QMessageBox.information(self.dashboard_window, "Success",
                                    f"Successfully added {hours} hours. Total hours: {self.total_hours}.")
        else:
            QMessageBox.warning(self.dashboard_window, "Error", "Invalid number of hours!")

    def cancel_parking(self):
        if self.total_hours == 0:
            QMessageBox.warning(self.dashboard_window, "Error", "You should find a parking spot first!")
        else:
            self.total_hours = 0
            self.payment_mode = None
            for i in range(1, 21):
                slot = ParkingSlot(i, f"carSpot_{i}", 1)
                slot.slotAvailable()
            QMessageBox.information(self.dashboard_window, "Success", "Successfully cancelled parking!")

    def show_payment_window(self):
        if self.total_hours == 0:
            QMessageBox.warning(self.dashboard_window, "Error", "Please find a parking spot first!")
            return

        self.payment_window = QWidget()
        self.payment_window.setWindowTitle("Payment")
        layout = QVBoxLayout()

        rate = 20
        self.total_amount = self.total_hours * rate

        layout.addWidget(QLabel(f"Total Hours Parked: {self.total_hours} hours"))
        layout.addWidget(QLabel(f"Rate: {rate} pesos per hour"))
        layout.addWidget(QLabel(f"Total Amount: {self.total_amount} pesos"))

        gcash_button = QPushButton("Pay with GCash")
        gcash_button.clicked.connect(lambda: self.select_payment_mode("GCash"))
        layout.addWidget(gcash_button)

        cash_button = QPushButton("Pay with Cash")
        cash_button.clicked.connect(lambda: self.select_payment_mode("Cash"))
        layout.addWidget(cash_button)

        self.payment_window.setLayout(layout)
        self.payment_window.show()

    def select_payment_mode(self, mode):
        if self.payment_mode:
            QMessageBox.warning(self.dashboard_window, "Error", "You can only choose one payment method!")
            return

        self.payment_mode = mode
        if mode == "GCash":
            self.show_gcash_payment()
        else:
            self.show_cash_payment()

    def show_gcash_payment(self):
        QMessageBox.information(self.dashboard_window, "GCash Payment",
                                "Payment successfully received via GCash!")
        self.close_receipt_window()
        self.reset_parking_data()

    def show_cash_payment(self):
        cash_given, ok = QInputDialog.getDouble(self.dashboard_window, "Cash Payment", "Enter cash amount:")
        if ok and cash_given >= self.total_amount:
            change = cash_given - self.total_amount
            QMessageBox.information(self.dashboard_window, "Change", f"Your change: {change} pesos")
            self.close_receipt_window()
            self.reset_parking_data()
        else:
            QMessageBox.warning(self.dashboard_window, "Error", "Insufficient amount!")

    def close_receipt_window(self):
        if self.receipt_window:
            self.receipt_window.close()
            self.receipt_window = None

    def handle_logout(self):
        self.close_receipt_window()
        self.show_form()

    def reset_parking_data(self):
        self.total_hours = 0
        self.payment_mode = None

    def create_table(self):
        conn = sqlite3.connect("Park-n-Spark.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                password TEXT,
                car_type TEXT,
                car_model TEXT
            )
        """)
        conn.commit()
        conn.close()


if __name__ == "__main__":
    window = ParkingApp()
    sys.exit(window.app.exec())
