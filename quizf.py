login_status = False
login_user = ''


def registration():
    name = input("Enter name: ")
    city = input("Enter City: ")
    enroll = input("Enter enroll: ")
    pwd = input("Enter password: ")

    with open('registration.txt', 'a') as file:
        file.write(f"{name},{city},{enroll},{pwd}\n")
        
    with open('login_details.txt', 'a') as file:
        file.write(f"{enroll},{pwd}\n")
    print("Registration successful!")


def login():
    global login_status
    global login_user
    en = input("Enter Enroll: ")
    users = {}
    
    # Read login details
    try:
        with open('login_details.txt', 'r') as file:
            for line in file:
                u, p = line.strip().split(',')
                users[u] = p
    except FileNotFoundError:
        print("Error: login_details.txt file not found!")
        return

    if en in users:
        pw = input("Enter Password: ")
        if pw == users[en]:
            print(f"Welcome {en}!")
            login_status = True
            login_user = en
        else:
            print("Wrong password!")
    else:
        print("User not registered!")
        if input("Do you want to register? (y/n): ").lower() == 'y':
            registration()


def attemptQuiz():
    if not login_status:
        print("Please log in first!")
        return

    try:
        with open('questions.txt', 'r') as file:
            questions = [line.strip().split(',') for line in file]
    except FileNotFoundError:
        print("Error: questions.txt file not found!")
        return

    score = 0
    for i, q in enumerate(questions):
        print(f"\nQ{i+1}: {q[0]}")
        print(f"1. {q[1]}  2. {q[2]}  3. {q[3]}  4. {q[4]}")
        try:
            answer = int(input("Your answer (1-4): "))
            if answer == int(q[5]):
                score += 1
        except ValueError:
            print("Invalid input! Moving to the next question.")

    print(f"\nYour score: {score}/{len(questions)}")
    
    # Save the result
    with open('results.txt', 'a') as file:
        file.write(f"{login_user},{score},{len(questions)}\n")


def showResult():
    if not login_status:
        print("Please log in first!")
        return

    try:
        with open('results.txt', 'r') as file:
            results = [line.strip().split(',') for line in file]
            for result in results:
                if result[0] == login_user:
                    print(f"\nYour Results: Score: {result[1]}/{result[2]}")
                    return
            print("No results found for your account.")
    except FileNotFoundError:
        print("Error: results.txt file not found!")


def showProfile():
    if not login_status:
        print("Please log in first!")
        return

    try:
        with open('registration.txt', 'r') as file:
            profiles = [line.strip().split(',') for line in file]
            for profile in profiles:
                if profile[2] == login_user:
                    print("\nYour Profile:")
                    print(f"Name: {profile[0]}")
                    print(f"City: {profile[1]}")
                    print(f"Enroll: {profile[2]}")
                    return
            print("Profile not found!")
    except FileNotFoundError:
        print("Error: registration.txt file not found!")


def main():
    while True:
        print("""
        1. Registration
        2. Login
        3. Attempt Quiz
        4. Show Profile
        5. Show Result
        6. EXIT
        """)
        choice = input("Enter your choice: ")

        if choice == "1":
            registration()
        elif choice == "2":
            login()
        elif choice == "3":
            attemptQuiz()
        elif choice == "4":
            showProfile()
        elif choice == "5":
            showResult()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
