"""
app_starter.py
by HundredVisionsGuy
A bare bones starter code to begin with.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Simple Calculator App: Tells you information about Math.")

        # TODO: add a text input for an equation
        self.num_input = QLineEdit(placeholderText="Add Equation")

        # TODO: add a push button to give the sum
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.get_input)

        # TODO: add instructions for the user
        self.instructions = "Enter an equation, then click the button."
        self.output_label = QLabel(self.instructions)
        self.output_label.setWordWrap(True)

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.num_input)
        layout.addWidget(submit_button)
        layout.addWidget(self.output_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def get_input(self):
        """grab input, process input, display output"""
        output = ""
        num = self.num_input.text()

        if not num:
            output = "WARNING: you did not enter an equation. Please enter "
            output += "an equation."
        else:
            output = f"Your answer is {num}."
        self.output_label.setText(output)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()