import sqlite3

# Initialize the Database and Add Sample Questions
def create_database():
    # Connect to SQLite database (creates the file if it doesn't exist)
    conn = sqlite3.connect('quiz_app.db')
    cursor = conn.cursor()

    # Create the questions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT,
            option4 TEXT,
            correct_option INTEGER
        )
    ''')

    # Insert sample questions
    sample_questions = [
        ("What is the capital of France?", "Paris", "Berlin", "Madrid", "Rome", 1),
        ("What is 2 + 2?", "3", "4", "5", "6", 2),
        ("What is the largest planet in our solar system?", "Earth", "Mars", "Jupiter", "Venus", 3),
        ("Which programming language is known as the backbone of web development?", "Python", "JavaScript", "C++", "Ruby", 2),
        ("Who developed the theory of relativity?", "Newton", "Einstein", "Galileo", "Tesla", 2)
    ]

    # Insert the sample questions into the table
    cursor.executemany('''
        INSERT INTO questions (question, option1, option2, option3, option4, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', sample_questions)

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("Database created and sample questions added successfully!")

if __name__ == "__main__":
    create_database()
