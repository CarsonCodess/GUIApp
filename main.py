import sys
import random
import time
import psutil
from PyQt6.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QTextCursor
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QGridLayout, QFrame

# Load Cascadia Code font
FONT = "Cascadia Code"

# Fake hacking-style commands
HACK_COMMANDS = [
    "Initializing boot sequence...",
    "Loading kernel modules...",
    "Establishing encrypted connection...",
    "Decrypting payload...",
    "Fetching system configuration...",
    "Injecting runtime variables...",
    "Accessing root privileges...",
    "Compiling modules...",
    "Initiating stealth protocols...",
    "System breach detected...",
    "Loading UI components..."
]

# Thread for startup animation
class StartupAnimationThread(QThread):
    finished_signal = pyqtSignal()
    command_signal = pyqtSignal(str)
    
    def run(self):
        for command in HACK_COMMANDS:
            self.command_signal.emit(command)
            time.sleep(random.uniform(0.2, 0.5))
        time.sleep(1)
        self.finished_signal.emit()

# Main UI Window
class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.start_cpu_monitor()

    def init_ui(self):
        self.setWindowTitle("Cyber Console UI")
        self.setStyleSheet("background-color: black; color: white;")
        layout = QGridLayout()

        # CPU Usage Section
        self.cpu_label = QLabel("CPU Usage: 0%")
        self.cpu_label.setFont(QFont(FONT, 14))
        self.cpu_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cpu_bar = QFrame()
        self.cpu_bar.setStyleSheet("background-color: white;")
        self.cpu_bar.setFixedWidth(30)
        self.cpu_bar.setFixedHeight(100)
        
        cpu_layout = QVBoxLayout()
        cpu_layout.addWidget(self.cpu_bar, alignment=Qt.AlignmentFlag.AlignCenter)
        cpu_layout.addWidget(self.cpu_label)
        
        cpu_container = QWidget()
        cpu_container.setLayout(cpu_layout)
        layout.addWidget(cpu_container, 0, 0)
        
        # Clock Section
        self.clock_label = QLabel("00:00:00")
        self.clock_label.setFont(QFont(FONT, 18, QFont.Weight.Bold))
        self.clock_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.clock_label, 0, 1, alignment=Qt.AlignmentFlag.AlignRight)

        # Console Section
        self.console_output = QTextEdit()
        self.console_output.setFont(QFont(FONT, 12))
        self.console_output.setReadOnly(True)
        self.console_output.setStyleSheet("border: 1px solid white;")
        self.console_output.setFixedHeight(200)

        self.console_input = QLineEdit()
        self.console_input.setFont(QFont(FONT, 12))
        self.console_input.setStyleSheet("border: 1px solid white;")
        self.console_input.returnPressed.connect(self.execute_command)
        
        layout.addWidget(self.console_output, 1, 0, 1, 2)
        layout.addWidget(self.console_input, 2, 0, 1, 2)
        self.setLayout(layout)

        # Clock Timer
        self.clock_timer = QTimer()
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.start(1000)
    
    def update_clock(self):
        self.clock_label.setText(time.strftime("%H:%M:%S"))

    def start_cpu_monitor(self):
        self.cpu_timer = QTimer()
        self.cpu_timer.timeout.connect(self.update_cpu_usage)
        self.cpu_timer.start(1000)
    
    def update_cpu_usage(self):
        usage = psutil.cpu_percent()
        self.cpu_label.setText(f"CPU Usage: {usage}%")
        self.cpu_bar.setFixedHeight(int(usage))
    
    def execute_command(self):
        command = self.console_input.text()
        self.console_output.append(f"> {command}")
        self.console_input.clear()
        if command.lower() == "clear":
            self.console_output.clear()
        else:
            self.console_output.append("Command not recognized.")
        self.console_output.moveCursor(QTextCursor.MoveOperation.End)

# Splash Screen
class StartupScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # Start the animation thread
        self.startup_thread = StartupAnimationThread()
        self.startup_thread.command_signal.connect(self.update_console)
        self.startup_thread.finished_signal.connect(self.start_logo_animation)
        self.startup_thread.start()
    
    def init_ui(self):
        self.setWindowTitle("Booting...")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()
        self.setStyleSheet("background-color: black; color: white;")
        
        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(10)
        
        self.console_output = QTextEdit()
        self.console_output.setFont(QFont(FONT, 14))
        self.console_output.setReadOnly(True)
        self.console_output.setStyleSheet("border: none;")
        
        self.logo = QLabel("CYBER SYSTEM")
        self.logo.setFont(QFont(FONT, 20, QFont.Weight.Bold))
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo.setVisible(False)
        
        # Adjust layout to center the logo
        self.layout.addWidget(self.console_output, 0, 0, 1, 3)
        self.layout.addWidget(self.logo, 1, 1, 1, 1, Qt.AlignmentFlag.AlignCenter)  # Ensure centering
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 2)
        self.layout.setRowStretch(2, 1)
        
        self.setLayout(self.layout)


    
    def update_console(self, command):
        self.console_output.append(command)
        self.console_output.moveCursor(QTextCursor.MoveOperation.End)
    
    def start_logo_animation(self):
        self.console_output.clear()
        self.logo.setVisible(True)
        self.flash_timer = QTimer()
        self.flash_interval = 100  # Start fast
        self.flash_count = 0
        self.flash_timer.timeout.connect(self.flash_logo)
        self.flash_timer.start(self.flash_interval)
    
    def flash_logo(self):
        if self.flash_count < 10:
            self.logo.setVisible(not self.logo.isVisible())
            self.flash_interval += 50  # Gradually slow down
            self.flash_timer.setInterval(self.flash_interval)
            self.flash_count += 1
        else:
            self.flash_timer.stop()
            self.logo.setVisible(True)
            QTimer.singleShot(2000, self.launch_main_app)
    
    def launch_main_app(self):
        self.main_app = MainApp()
        self.main_app.show()
        self.close()
    
    def closeEvent(self, event):
        if self.startup_thread.isRunning():
            self.startup_thread.quit()
            self.startup_thread.wait()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = StartupScreen()
    splash.show()
    sys.exit(app.exec())
