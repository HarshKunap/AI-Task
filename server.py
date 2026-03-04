import random
from ai_agent import ai_response
from human import human_response
from evaluation import evaluate
from logger import initialize_log, log_message

def run_turing_test():
    initialize_log()
    
    print("===== TURING TEST STARTED =====")
    print("You are the Interrogator.")
    print("Ask questions to Entity A and Entity B.")
    print("Type 'exit' to end questioning.\n")
    
    # Randomly assign AI to A or B
    ai_label = random.choice(["A", "B"])
    
    score = 0
    rounds = 1  # you can increase for multiple sessions
    
    for r in range(rounds):
        print(f"\n--- Round {r+1} ---")
        log_message(f"\n--- Round {r+1} ---")
        
        while True:
            question = input("\nInterrogator: ")
            if question.lower() == "exit":
                break
            
            if ai_label == "A":
                response_A = ai_response(question)
                response_B = human_response(question)
            else:
                response_A = human_response(question)
                response_B = ai_response(question)
            
            print("\nEntity A:", response_A)
            print("Entity B:", response_B)
            
            log_message(f"Q: {question}")
            log_message(f"A: {response_A}")
            log_message(f"B: {response_B}")
        
        correct = evaluate(ai_label)
        log_message(f"Judge guessed correctly: {correct}")
        
        if correct:
            score += 1
    
    print(f"\nFinal Score: {score}/{rounds}")
    log_message(f"Final Score: {score}/{rounds}")
    print("===== TEST ENDED =====")

if __name__ == "__main__":
    run_turing_test()