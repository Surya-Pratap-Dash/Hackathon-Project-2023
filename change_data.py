import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QLabel,QComboBox
import pandas as pd
from PyQt5.QtCore import QTimer,Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the CSV file into a pandas DataFrame
        self.df = pd.read_csv('F:/Hackathon Project 2023/worldcities.csv')

        # Set the title and dimensions of the replace window
        self.setWindowTitle('Changing_Data')
        self.setGeometry(100, 100, 800, 600)

        # Store the DataFrame as an instance variable
        self.df = df

        # Create a central widget and a layout for it
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Create a drop-down menu with all the column names of the DataFrame
        self.column_name_menu = QComboBox()
        self.column_name_menu.addItems(self.df.columns.tolist())
        layout.addWidget(self.column_name_menu)

        # Increase the minimum width of the menu view
        self.column_name_menu.view().setMinimumWidth(200)

        layout.addWidget(self.column_name_menu)

        # Set the focus policy of the menu view to Qt.NoFocus
        self.column_name_menu.view().setFocusPolicy(Qt.NoFocus)

        layout.addWidget(self.column_name_menu)
        # Create a layout and add the widgets to it
        layout = QVBoxLayout()
        layout.addWidget(self.column_name_menu)
        # ... add more widgets to the layout as needed

        # Create a main widget to hold the layout and set it as the central widget
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        # Create a label and a text input field for the old value
        old_value_label = QLabel('Old Value')
        self.old_value_input = QLineEdit()
        layout.addWidget(old_value_label)
        layout.addWidget(self.old_value_input)

        # Create a label and a text input field for the new value
        new_value_label = QLabel('New Value')
        self.new_value_input = QLineEdit()
        layout.addWidget(new_value_label)
        layout.addWidget(self.new_value_input)

        # Create a button to replace the values
        replace_button = QPushButton('Replace')
        replace_button.clicked.connect(self.replace_values)
        layout.addWidget(replace_button)

        # Set the layout of the central widget
        central_widget.setLayout(layout)

        # Set the central widget of the replace window
        self.setCentralWidget(central_widget)

        # Create a button to insert the values
        insert_button = QPushButton('Insert')
        insert_button.clicked.connect(self.insert_values)
        layout.addWidget(insert_button)

        # Create a button to delete the values
        delete_button = QPushButton('Delete')
        delete_button.clicked.connect(self.delete_values)
        layout.addWidget(delete_button)

        # Set the layout of the central widget
        central_widget.setLayout(layout)

        # Set the central widget of the main window
        self.setCentralWidget(central_widget)



    def insert_values(self):

        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv('F:/Hackathon Project 2023/worldcities.csv')

        # Get the values from the input fields
        city = self.city_input.text()
        country = self.country_input.text()
        region = self.region_input.text()
        population = self.population_input.text()

        # Insert the values into the database
        # (you would need to implement this part yourself)
        # For example:
        # cursor.execute("INSERT INTO cities (city, country, region, population) VALUES (?, ?, ?, ?)", (city, country, region, population))
        # connection.commit()

        # Clear the input fields
        self.city_input.clear()
        self.country_input.clear()
        self.region_input.clear()
        self.population_input.clear()

        # Save the modified DataFrame back to a CSV file
        df.to_csv('F:/Hackathon Project 2023/worldcities.csv', index=False)

        # Show a message box to confirm the insertion
        msg = QMessageBox()
        msg.setWindowTitle("Data Modified")
        msg.setText(f"A new row has been inserted with values: {new_row}")
        msg.exec_()

    def delete_values(self):
            # Load the CSV file into a pandas DataFrame
            df = pd.read_csv('F:/Hackathon Project 2023/worldcities.csv')

            # Get the value to delete from the text input field
            delete_value = self.old_value_input.text()

            # Get the name of the column to delete from
            column_name = self.column_name_input.currentText()

            # Delete all rows that match the delete value in the specified column
            df = df[df[column_name] != delete_value]

            # Save the modified DataFrame back to a CSV file
            df.to_csv('F:/Hackathon Project 2023/worldcities.csv', index=False)

            # Show a message box to confirm the deletion
            msg = QMessageBox()
            msg.setWindowTitle("Data Modified")
            msg.setText(f"All rows with {delete_value} in {column_name} column have been deleted.")
            msg.exec_()

    def replace_values(self):
        column_name = self.column_name_input.text()
        old_value = self.old_value_input.text()
        new_value = self.new_value_input.text()
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv('F:/Hackathon Project 2023/worldcities.csv')

        # Replace all occurrences of 'old_value' in the 'column_name' column with 'new_value'
        df.loc[df[column_name] == old_value, column_name] = new_value

        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv('F:/Hackathon Project 2023/worldcities.csv')

        # Save the modified DataFrame back to a CSV file
        df.to_csv('F:/Hackathon Project 2023/worldcities.csv', index=False)

        # Show a message box to confirm the replacement
        msg = QMessageBox()
        msg.setWindowTitle("Data Modified")
        msg.setText(f"All occurrences of '{old_value}' in column '{column_name}' have been replaced with '{new_value}'.")
        msg.exec_()


if __name__ == '__main__':
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv('F:/Hackathon Project 2023/worldcities.csv')
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
