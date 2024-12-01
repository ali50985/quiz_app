def ask_question(question,option,correct_answer):
    print(f'{question}')
    
    for i,option in enumerate(option ,start = 1):
        print(f'{i}. {option}')
        
    choice = int(input("enter the no. of your answer: "))
        
    if choice == correct_answer:
            print("your answer is correct!")
            return True
    else:
        print(f"your answer is wrong , the correct answer is {correct_answer}")
        return False
def quiz():
    questions = [{'question' : "Which of the following is a mutable data type in Python?",
                 'option':['tuple','list','integer','string'],
                  'correct_answer':2},
                 {'question':'Which data type is used to store True or False values?',
                  'option':['bool','float','string','integer'],
                  'correct_answer':1},
                 {'question':'what operator is used to find remainder?',
                  'option':['+','/','%','-'],
                  'correct_answer':3},
                 {'question':'What keyword is used to exit a loop prematurely in Python?',
                  'option':['def','break','continue','pass'],
                  'correct_answer':2},
                 {'question':'What symbol is used to make comments in Python?',
                  'option':['$','*','//','#'],
                  'correct_answer':4}
                ]
    
    score = 0
    incorrect = 0
    correct = 0
    
    for j in questions:
        is_correct = ask_question(j['question'],j['option'],j['correct_answer'])
        if is_correct:
            score = score + 1
            correct += score 
        else:
            incorrect = incorrect + 1
            
    print(f'your final score is {score}')
    print(f'correct: {correct}')
    
    print(f'incorrect: {incorrect}')
    
    
    
if __name__ == "__main__":
    print("Welcome to the Quiz App!")
    quiz()
                  