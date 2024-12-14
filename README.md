Name Group Randomizer 

Overview

        The Group Randomizer GUI is a Python application designed to help users randomly assign names to groups or pick random names from a 
        provided list. This tool is particularly useful for team assignments, classroom activities, or any scenario requiring randomization 
        of names. With a user-friendly graphical interface built using Tkinter, this application simplifies the process of randomizing 
        group assignments or selecting names with minimal effort.

        Key Features:
        - Input names separated by commas into a text box.
        - Specify the number of groups for random assignment.
        - Pick a random name from the provided list.
        - Clear the last entered name or clear all fields.
        - Results displayed in an intuitive and visually appealing format.



Installation and Usage Instructions

        Prerequisites
                - Python 3.8+
                The following Python packages are required:
                - tkinter (built-in with most Python installations)
                - random

        Clone or Download the Repository
	        Option 1: Clone the repository
                        git clone https://github.com/carnaje-s/NameGroupRandomizer_Group2.git
                        cd NameGroupRandomizer_Group2

	        Option 2: Download as ZIP
                        Go to your repository page.
                        Click on the Code button beside the Add file, then select Download ZIP.

   	Run the Application
    		Navigate to the project directory in the terminal.
      		Run the main script (app.py) to start the GUI application



Examples of Functionalities

        1. Group Randomization:
                Input a list of names separated by commas in the provided text box. Specify the desired number of groups in the "Number of Groups"
                input field. Click the "Generate Groups" button to randomize and display group assignments.
                	Example Input:
               		John, Sarah, Emily, Michael, Anna, David
                	Number of Groups: 3
                	Output:
                	Group 1: John, Emily
                	Group 2: Sarah, Anna
                	Group 3: Michael, David

        2. Pick Random Name:
                Input a list of names separated by commas in the text box. Click the "Pick Random Name" button to randomly select one 
                name from the list.
                	Example Output:
                	Picked Name: Emily

        3. Clear Last Name and Clear All:
                Use the "Clear Last Name" button to remove the last entered name in the text box.
  			Example: 
			Input: John, Sarah, Emily
			Click "Clear Last Name".
			Result: John, Sarah
   
                Use the "Clear All" button to reset all inputs and results.
			Example:
			Input: John, Sarah, Emily
			Click "Clear All".
			Result: (Text box is empty)
