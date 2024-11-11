Disease Recommendation System

This Disease Recommendation System is a machine learning-based tool designed to assist users in identifying potential diseases based on their symptoms. It uses a pre-trained Support Vector Classifier (SVC) model to provide disease recommendations. The system features a user-friendly GUI (Graphical User Interface) built with Tkinter where users can input their symptoms, and the model will predict a possible disease.

Features:
Symptom Input: Users can enter symptoms in a comma-separated format.
Disease Prediction: Based on the input symptoms, the system predicts the most likely disease using a pre-trained machine learning model.
User Interface: A simple and interactive interface built with Tkinter.

Requirements
To run this system, you need:

Python 3.6+
Required Libraries:
numpy: for numerical computations
scikit-learn: for machine learning model
pandas: for handling data (if used in the script)
tkinter: for creating the GUI
If you don’t have these libraries installed, you can install them using pip:

bash:
pip install numpy scikit-learn pandas
Running the Application
You have two options to run the system: either using the bundled executable or running the Python script directly.

Option 1: Using the Executable (PyInstaller Bundle)
If you prefer running the application as an executable, follow these steps:

Download the executable: After building the executable with PyInstaller, find it in the dist folder.
Ensure that the model file svc.pkl is located in the same folder as the executable.
Double-click on the executable to run the application. The GUI will appear where you can enter symptoms and get a disease prediction.
Note: If you want to build the executable yourself, follow the "PyInstaller Build Instructions" section below.

Option 2: Running the Python Script
If you prefer to run the Python script directly, follow these steps:

Download the script: Clone or download the project directory.
Navigate to the project directory: Open a terminal and change to the project folder where the script is located.
Run the script:
bash:
python recommendation_script.py
This will launch the application in the terminal. You can then interact with the GUI to enter symptoms and view the disease recommendation.

PyInstaller Build Instructions (Optional)
To bundle the script into a standalone executable, you can use PyInstaller. Here's how:

Install PyInstaller:

If you don't have PyInstaller installed, install it using pip:

bash:
pip install pyinstaller
Build the executable:

Run the following PyInstaller command to generate a bundled executable.

For Windows:

bash:
pyinstaller --onefile --add-data "path_to_svc.pkl;." --hidden-import=sklearn --hidden-import=pandas recommendation_script.py
For Linux/macOS:

bash:
pyinstaller --onefile --add-data "path_to_svc.pkl:." --hidden-import=sklearn --hidden-import=pandas recommendation_script.py
Replace path_to_svc.pkl with the actual path to the svc.pkl model file.

Test the executable:

Once the build process is complete, you will find the executable in the dist folder. You can run this executable directly.

How the System Works
Input Symptoms: The user types the symptoms in a comma-separated list in the input field.
Binary Vector Conversion: The entered symptoms are converted into a binary vector corresponding to the 132 symptoms used for training the model.
Model Prediction: The model (svc.pkl) uses the binary vector to predict the disease associated with the symptoms.
Display Recommendation: The system shows the predicted disease on the interface.
Troubleshooting
ModuleNotFoundError
If you encounter errors such as ModuleNotFoundError (e.g., for sklearn or pandas), ensure that you include these libraries during the PyInstaller build process using the --hidden-import flag:

bash:
--hidden-import=sklearn --hidden-import=pandas
This will include those modules in the final executable.

License
This project is licensed under the MIT License - see the LICENSE file for more details.

Customization
You can modify the system by:

Changing symptoms: Modify the symptom_list if you want to add or remove symptoms.
Updating the disease dictionary: The disease_dict can be customized with different diseases based on your requirements.
Feel free to modify the script or GUI according to your needs. If you have any questions or run into issues, please open an issue in the repository.