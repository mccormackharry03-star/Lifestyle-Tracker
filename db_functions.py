import sqlite3
import datetime

def get_connection():
    return sqlite3.connect('tracker.db')

def add_weekly_goal(day_of_week, goal_name, category):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO templates (day_of_week, goal_name, category) VALUES (?, ?, ?)",
        (day_of_week, goal_name, category)
    )
    conn.commit()
    conn.close()

def get_todays_goals():
    conn = get_connection()
    cursor = conn.cursor()
    today_date = datetime.date.today().isoformat()
    today_name = datetime.date.today().strftime("%A")
    
    # Check for Overrides
    cursor.execute("SELECT goal_name FROM overrides WHERE specific_date = ?", (today_date,))
    override_goals = cursor.fetchall()
    if len(override_goals) > 0:
        conn.close()
        return [goal[0] for goal in override_goals]
    
    # Weekly Templates
    cursor.execute("SELECT goal_name FROM templates WHERE day_of_week = ?", (today_name,))
    template_goals = cursor.fetchall()
    conn.close()
    if len(template_goals) > 0:
        return [goal[0] for goal in template_goals]
    else:
        return[]

# Testing stuff
if __name__ == "__main__":
    today_name = datetime.date.today().strftime("%A")
    
    # Let's inject a dummy goal into the database for whatever day today is
    add_weekly_goal(today_name, "Drink 2L Water", "Diet")
    add_weekly_goal(today_name, "Do 50 Pushups", "Gym")
    
    # Now let's test the brain to see if it can read what we just wrote
    print(f"--- Brain Test for {today_name} ---")
    goals = get_todays_goals()
    print("Your goals for today are:")
    for g in goals:
        print(f"- {g}")