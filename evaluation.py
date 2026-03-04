def evaluate(actual_ai_label):
    guess = input("\nWho do you think is the AI? (A/B): ").strip().upper()
    
    if guess == actual_ai_label:
        print("Correct! You identified the AI.")
        return True
    else:
        print("Wrong! You failed to identify the AI.")
        return False