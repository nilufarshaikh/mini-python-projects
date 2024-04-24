def run_quiz(questions):
    
    score = 0
    
    for question in questions:
        print(question["prompt"])
        
        for option in question["options"]:
            print(option)
        
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer is", question["answer"], "\n")
    
    print(f"Result: You got {score} out of {len(questions)} questions correct.")

# List of quiz questions. Each question is a dictionary.

questions = [
    {
        "prompt": "What is a variable in Python?",
        "options": ["A. Symbol", "B. Data", "C. Name", "D. Value"],
        "answer": "C"
    },
    {
        "prompt": "Which statement is used for decision making in Python?",
        "options": ["A. for", "B. if", "C. while", "D. do"],
        "answer": "B"
    },
    {
        "prompt": "What does the 'print()' function do in Python?",
        "options": ["A. Input", "B. Output", "C. Calculate", "D. Loop"],
        "answer": "B"
    },
    {
        "prompt": "How are lists and tuples different in Python",
        "options": ["A. Size", "B. Indexing", "C. Elements", "D. Mutability"],
        "answer": "D"
    }
]

run_quiz(questions)