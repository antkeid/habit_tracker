# Habit Tracker

Welcome to the Habit Tracker! This tracker helps you monitor your habits on a daily or weekly basis. You can choose from 5 predefined habits or create your own custom habit.

### Features

- **Predefined Habits**: Choose from a selection of 5 common habits.
- **Custom Habits**: Create and track your own habits.
- **Daily and Weekly Tracking**: Select the tracking frequency that suits your needs.
- **Habit Analysis**: Analyze your habit data to see trends and improvements.

### Installation

After installing Python,  proceed to the following steps to install the habit tracker

1. Copy the repository.
2. Navigate to the project directory.
3. Install the required dependencies using pip:
   ``` 
   pip install questionary
   ```
   ```
   pip install pytest 
   ```

4. Run the application.


### Project Structure

- `main.py`: The main script containing the CLI and core implementation of the Habit Tracker.
- `habit.py`: Defines the `Habit` class and handles predefined and user created habits.
- `analytics.py`: Handles the analysis of the habits.
- `README.md`: Provides installation and project description. 
- `test.py`: Directory containing test files to ensure the application works as expected.
- `requirements.txt`: Lists all the dependencies needed to run the application.

### Usage
#### Starting the Application
To start tracking your habits, run the application by executing the following command in your terminal:

```
python main.py
```

### Defining a Habit
When prompted by the application, you will need to provide the following details for each habit:

- Habit Name: Select from predefined habits or enter a custom name.
- Periodicity: Choose whether you want to track the habit daily or weekly.
- Duration: Specify the number of days or weeks you plan to track the habit.

### Tracking Your Habits
Once your habits are defined, you can start tracking them daily or weekly based on your chosen periodicity. The application will prompt you to update the status of your habits regularly.

### Analyzing Your Habits
Use the analysis features to review your habit data. The analytics.py module provides insights into your progress, helping you understand trends and areas for improvement.

### Testing
To run tests and ensure the application is functioning correctly, execute the following command:

```
pytest
```



Happy habit tracking!

