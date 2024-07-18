import sqlite3
from habit import Habit

class Analytics:
    @staticmethod
    def list_all_habits():
        """ List all habits from the SQLite database.
        :return: A list of habit names.
        """
        # Connect to the SQLite database 'habits.db'.
        conn = sqlite3.connect('habits.db')
        c = conn.cursor()

        # Execute a query to select the name of all habits from the 'habits' table.
        c.execute("SELECT DISTINCT name FROM habits")

        # Fetch all rows from the executed query.
        habits = c.fetchall()

        # Close the database connection.
        conn.close()

        # Return a list of habit names.
        return [habit[0] for habit in habits]

    @staticmethod
    def list_habits_by_periodicity(periodicity):
        """List habits by their periodicity from the SQLite database.
        :param periodicity: The periodicity to filter habits (Daily or Weekly).
        :return: A list of habit names with the specified periodicity."""
        # Connect to the SQLite database 'habits.db'.
        conn = sqlite3.connect('habits.db')
        c = conn.cursor()

        # Execute a query to select the name of habits where the periodicity matches the given value.
        c.execute("SELECT DISTINCT name FROM habits WHERE periodicity = ?", (periodicity,))

        # Fetch all rows from the executed query.
        habits = c.fetchall()

        # Close the database connection.
        conn.close()

        # Return a list of habit names.
        return [habit[0] for habit in habits]

    @staticmethod
    def longest_run_streak():
        """Calculate the habit with the longest run streak.
        :return: A string describing the habit with the longest run streak.
        """
        # Retrieve all habits from the database.
        habits = Habit.get_all()

        longest_run_streak = 0
        longest_run_habit = None
        habits_group = {}

        # Iterate over all habits to calculate the longest run streak.
        for habit in habits:
            if habit[0] not in habits_group:
                habits_group[habit[0]] = 0

            # Extract the duration period (number and type, e.g., "30 days").
            habits_group[habit[0]] += 1

            # Update the longest run streak and corresponding habit details.
            if habits_group[habit[0]] > longest_run_streak:
                longest_run_habit = habit
                longest_run_streak = habits_group[habit[0]]

        return f"Longest run streak is {longest_run_streak} for '{longest_run_habit[0]}'"

    @staticmethod
    def longest_streak_for_habit(habit_name):
        """ Calculate the longest run streak for a specific habit.
        :param habit_name: The name of the habit to calculate the streak for.
        :return: A string describing the longest streak for the specified habit."""
        # Retrieve all habits from the database.
        habits = Habit.get_all()

        longest_run_streak = 0
        habits_group = {}

        # Iterate over all habits to calculate the longest run streak for the specified habit.
        for habit in habits:
            if habit[0] not in habits_group:
                habits_group[habit[0]] = 0

            # Extract the duration period (number and type, e.g., "30 days").
            habits_group[habit[0]] += 1

            # Update the longest run streak for the specified habit.
            if habits_group[habit[0]] > longest_run_streak and habit_name == habit[0]:
                longest_run_streak = habits_group[habit[0]]

        return f"Longest streak for {habit_name} is {longest_run_streak}"
