import sqlite3

class Habit:
    def __init__(self, name, periodicity, duration):
        """Initialize a Habit instance.
        :param name: Name of the habit.
        :param periodicity: How often the habit should be performed (Daily or Weekly).
        :param duration: The total duration for maintaining the habit (up to 30 days)."""
        self.name = name
        self.periodicity = periodicity
        self.duration = duration
    def save(self, keep_conn=False):
        """Save the habit to the SQLite database.
        :param keep_conn: Boolean flag to keep the connection open if set to True."""
        # Connect to the SQLite database 'habits.db'. If it does not exist, it will be created.
        conn = sqlite3.connect('habits.db')
        c = conn.cursor()

        # Create the 'habits' table if it does not already exist.
        c.execute('''CREATE TABLE IF NOT EXISTS habits
                     (name text, periodicity text, duration text)''')

        # Insert the habit instance's details into the 'habits' table.
        c.execute("INSERT INTO habits (name, periodicity, duration) VALUES (?, ?, ?)",
                  (self.name, self.periodicity, self.duration))

        # Commit the transaction to save changes to the database.
        conn.commit()

        # Close the database connection unless keep_conn is True.
        if not keep_conn:
            conn.close()

    @staticmethod
    def get_all():
        """Retrieve all habits from the SQLite database.
        :return: A list of tuples containing habit details (name, periodicity, duration)."""
        # Connect to the SQLite database 'habits.db'.
        conn = sqlite3.connect('habits.db')
        c = conn.cursor()

        # Execute a query to select all records from the 'habits' table.
        c.execute("SELECT * FROM habits")

        # Fetch all rows from the executed query.
        habits = c.fetchall()

        # Close the database connection.
        conn.close()

        # Return the list of all habits.
        return habits

def seed():
    """Seed the database with predefined habits."""
    # List of predefined Habit instances.
    predefined_habits = [
        Habit("Stretching Session per day", "Daily", "30 days"),
        Habit("Drinking 2 liters of water per day", "Daily", "30 days"),
        Habit("Taking 10,000 steps per day", "Daily", "30 days"),
        Habit("Engaging in 1 hour physical activity per day", "Daily", "30 days"),
        Habit("Spending 15 minutes in meditation per day", "Daily", "30 days")
    ]

    # Save each predefined habit to the database.
    for habit in predefined_habits:
        habit.save()
