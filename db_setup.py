import sqlite3

def setup_database():
    conn = sqlite3.connect('tracker.db')
    cursor = conn.cursor()

    # Table 1: Weekly Templates
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS templates (
            day_of_week TEXT,
            goal_name TEXT,
            category TEXT
        )
    ''')

    # Table 2: Specific Day Overrides
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS overrides (
            specific_date TEXT,
            goal_name TEXT,
            category TEXT
        )
    ''')

    # Table 3: Daily Log
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_logs (
            date TEXT,
            goal_name TEXT,
            is_completed BOOLEAN
        )
    ''')

    conn.commit()
    conn.close()
    print("Database and tables created successfully")

if __name__ == "__main__":
    setup_database()