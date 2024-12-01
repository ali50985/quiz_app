import sqlite3

# Initialize Database and Create Table for Questions
def initialize_db():
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

    # Add sample questions (Run this once)
    cursor.execute("SELECT COUNT(*) FROM questions")
    if cursor.fetchone()[0] == 0:  # If the table is empty
        sample_questions = [
            ("What is the capital of France?", "Paris", "Berlin", "Madrid", "Rome", 1),
            ("What is 2 + 2?", "3", "4", "5", "6", 2),
            ("What is the largest planet in our solar system?", "Earth", "Mars", "Jupiter", "Venus", 3),
            ("Which programming language is known as the backbone of web development?", "Python", "JavaScript", "C++", "Ruby", 2),
            ("Who developed the theory of relativity?", "Newton", "Einstein", "Galileo", "Tesla", 2)
        ]
        cursor.executemany('''
            INSERT INTO questions (question, option1, option2, option3, option4, correct_option)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', sample_questions)
    
    conn.commit()
    conn.close()

# Function to Conduct the Quiz
def start_quiz():
    conn = sqlite3.connect('quiz_app.db')
    cursor = conn.cursor()

    # Fetch all questions
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    conn.close()

    if not questions:
        print("No questions available in the database!")
        return

    score = 0
    total_questions = len(questions)

    for question in questions:
        print(f"\n{question[1]}")
        print(f"1. {question[2]}  2. {question[3]}  3. {question[4]}  4. {question[5]}")
        try:
            answer = int(input("Your answer (1-4): "))
            if answer == question[6]:
                score += 1
        except ValueError:
            print("Invalid input! Moving to the next question.")

    print(f"\nQuiz Completed! Your Score: {score}/{total_questions}")

# Main Function
def main():
    initialize_db()
    print("Welcome to the Quiz App!")
    start_quiz()

if __name__ == "__main__":
    main()
