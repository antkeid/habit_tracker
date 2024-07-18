import sqlite3
import pytest
from unittest.mock import patch
from analytics import Analytics
from habit import Habit


@pytest.fixture
def setup_database():
    """Setup an in-memory SQLite database for testing purposes."""
    # Create an in-memory SQLite database connection.
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()

    # Create the 'habits' table.
    c.execute('''
        CREATE TABLE habits (
            name TEXT NOT NULL,
            periodicity TEXT NOT NULL,
            duration TEXT NOT NULL
        )
    ''')

    # Insert test data into the 'habits' table.
    c.executemany('''
        INSERT INTO habits (name, periodicity, duration)
        VALUES (?, ?, ?)
    ''', [
        ('Stretching Session per day', 'Daily', '30 days'),
        ('Drinking 2 liters of water per day', 'Daily', '30 days'),
        ('Taking 10,000 steps per day', 'Daily', '30 days'),
        ('Engaging in 1 hour physical activity per day', 'Daily', '30 days'),
        ('Spending 15 minutes in meditation per day', 'Daily', '30 days')
    ])

    # Commit the transaction.
    conn.commit()

    # Provide the database connection to the tests.
    yield conn

    # Close the database connection after tests are done.
    conn.close()


@patch('sqlite3.connect')
def test_list_all_habits(mock_connect, setup_database):
    """Test listing all habits from the database."""
    mock_connect.return_value = setup_database

    # Call the method to list all habits.
    habits = Analytics.list_all_habits()

    # Verify the expected result.
    assert habits == [
        'Stretching Session per day',
        'Drinking 2 liters of water per day',
        'Taking 10,000 steps per day',
        'Engaging in 1 hour physical activity per day',
        'Spending 15 minutes in meditation per day'
    ]


@patch('sqlite3.connect')
def test_list_habits_by_periodicity(mock_connect, setup_database):
    """Test listing habits by their periodicity from the database.
    """
    mock_connect.return_value = setup_database

    # Call the method to list habits with 'Daily' periodicity.
    daily_habits = Analytics.list_habits_by_periodicity('Daily')

    # Verify the expected result.
    assert daily_habits == [
        'Stretching Session per day',
        'Drinking 2 liters of water per day',
        'Taking 10,000 steps per day',
        'Engaging in 1 hour physical activity per day',
        'Spending 15 minutes in meditation per day'
    ]


@patch('habit.Habit.get_all')
def test_longest_run_streak(mock_get_all):
    """Test finding the habit with the longest run streak. """
    mock_get_all.return_value = [
        ('Stretching Session per day', 'Daily', '30 days'),
        ('Drinking 2 liters of water per day', 'Daily', '30 days'),
        ('Taking 10,000 steps per day', 'Daily', '30 days'),
        ('Engaging in 1 hour physical activity per day', 'Daily', '30 days'),
        ('Spending 15 minutes in meditation per day', 'Daily', '30 days')
    ]

    # Call the method to find the longest run streak.
    result = Analytics.longest_run_streak()

    # Verify the expected result.
    assert result == "Longest run streak is 1 for 'Stretching Session per day'"


@patch('habit.Habit.get_all')
def test_longest_streak_for_habit(mock_get_all):
    """Test finding the longest streak for specific habits."""
    mock_get_all.return_value = [
        ('Stretching Session per day', 'Daily', '30 days'),
        ('Drinking 2 liters of water per day', 'Daily', '30 days'),
        ('Taking 10,000 steps per day', 'Daily', '30 days'),
        ('Engaging in 1 hour physical activity per day', 'Daily', '30 days'),
        ('Spending 15 minutes in meditation per day', 'Daily', '30 days')
    ]

    # Verify the longest streak for each specific habit.
    result = Analytics.longest_streak_for_habit('Stretching Session per day')
    assert result == "Longest streak for Stretching Session per day is 1"

    result = Analytics.longest_streak_for_habit('Drinking 2 liters of water per day')
    assert result == "Longest streak for Drinking 2 liters of water per day is 1"

    result = Analytics.longest_streak_for_habit('Taking 10,000 steps per day')
    assert result == "Longest streak for Taking 10,000 steps per day is 1"

    result = Analytics.longest_streak_for_habit('Engaging in 1 hour physical activity per day')
    assert result == "Longest streak for Engaging in 1 hour physical activity per day is 1"

    result = Analytics.longest_streak_for_habit('Spending 15 minutes in meditation per day')
    assert result == "Longest streak for Spending 15 minutes in meditation per day is 1"


@patch('sqlite3.connect')
def test_add_habit(mock_connect, setup_database):
    """Test adding a new habit to the database."""
    mock_connect.return_value = setup_database

    # Create and save a new habit.
    new_habit = Habit('Reading a book', 'Daily', '15 days')
    new_habit.save(True)

    # Verify the new habit is correctly added to the database.
    conn = setup_database
    c = conn.cursor()
    c.execute("SELECT name, periodicity, duration FROM habits WHERE name = ?", ('Reading a book',))
    habit = c.fetchone()
    assert habit == ('Reading a book', 'Daily', '15 days')
