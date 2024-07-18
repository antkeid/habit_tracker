import os
import questionary
from habit import Habit, seed
from analytics import Analytics


def main_menu():
    """Display the main menu and handle user choice."""
    choice = questionary.select(
        "Welcome to the Habit Tracker. What would you like to do?",
        choices=[
            "Define Habit",
            "Check Progress",
            "Habit Analytics",
            "Exit"
        ]).ask()

    # Route the user to the appropriate function based on their choice.
    if choice == "Define Habit":
        define_habit()
    elif choice == "Check Progress":
        check_progress()
    elif choice == "Habit Analytics":
        habit_analytics()
    elif choice == "Exit":
        exit()


def define_habit():
    """Define a new habit and save it to the database."""
    habit_type = questionary.select(
        "Choose a habit type:",
        choices=[
            "Stretching Session per day",
            "Drinking 2 liters of water per day",
            "Taking 10,000 steps per day",
            "Engaging in 1 hour physical activity per day",
            "Spending 15 minutes in meditation per day",
            "Create your own habit"
        ]).ask()

    # If the user chooses to create their own habit, prompt for the habit name.
    if habit_type == "Create your own habit":
        habit_name = questionary.text("Enter the name of your habit:").ask()
    else:
        habit_name = habit_type

    # Default periodicity is 'Daily'. Allow the user to choose if creating their own habit.
    periodicity = questionary.select(
        "How often would you like to track this habit?",
        choices=["Daily", "Weekly"]
    ).ask()

    # Prompt the user to enter the duration for tracking the habit.
    duration = questionary.text("For how many days or weeks do you want to track this habit?").ask()

    # Create a new Habit instance and save it to the database.
    habit = Habit(name=habit_name, periodicity=periodicity, duration=duration)
    habit.save()

    # Return to the main menu after defining the habit.
    main_menu()


def check_progress():
    """Display the progress of all habits."""
    # Retrieve all habits from the database.
    habits = Habit.get_all()

    # Print each habit's details.
    for habit in habits:
        print(habit)

    # Return to the main menu after displaying progress.
    main_menu()


def habit_analytics():
    """Display habit analytics options and handle user choice."""
    choice = questionary.select(
        "Choose an analytics option:",
        choices=[
            "List all currently tracked habits",
            "List all habits with the same periodicity",
            "Longest run streak of all defined habits",
            "Longest streak for a given habit",
            "Back to Main Menu"
        ]).ask()

    # Route the user to the appropriate analytics function based on their choice.
    if choice == "List all currently tracked habits":
        print(Analytics.list_all_habits())
    elif choice == "List all habits with the same periodicity":
        periodicity = questionary.select(
            "Choose the periodicity:",
            choices=["Daily", "Weekly"]
        ).ask()
        print(Analytics.list_habits_by_periodicity(periodicity))
    elif choice == "Longest run streak of all defined habits":
        print(Analytics.longest_run_streak())
    elif choice == "Longest streak for a given habit":
        habit_name = questionary.text("Enter the name of the habit:").ask()
        print(Analytics.longest_streak_for_habit(habit_name))
    elif choice == "Back to Main Menu":
        main_menu()

    # Return to the main menu after displaying analytics.
    main_menu()


if __name__ == "__main__":
    # Seed the database with predefined habits before starting the main menu.
    if not os.path.exists('./habits.db'):
        seed()
    main_menu()
