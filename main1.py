import random

print("--- WELCOME TO THE CRICKET SIMULATOR ---")
print("Rules: Numbers must be between 1 and 6 only.")

user_score = 0
user_wickets = 0
balls_bowled = 0

print("\n--- YOUR BATTING STARTS ---")
while user_wickets < 2 and balls_bowled < 12:
    print(f"\nBall: {balls_bowled + 1}")
    user_input = int(input("Enter your number (1-6): "))
    
    if user_input < 1 or user_input > 6:
        print("INVALID INPUT! Please enter a number between 1 and 6.")
        continue 
    
    comp_input = random.randint(1, 6)
    print(f"Computer chose: {comp_input}")
    
    if user_input == comp_input:
        user_wickets += 1
        print(f"OUT! Wickets: {user_wickets}")
    else:
        user_score += user_input
        print(f"Current Score: {user_score}")
    
    balls_bowled += 1

print(f"\nYour Innings Over! Final Score: {user_score}/{user_wickets}")

comp_score = 0
comp_wickets = 0
balls_bowled = 0 

print("\n--- COMPUTER BATTING STARTS ---")
while comp_wickets < 2 and balls_bowled < 12:
    print(f"\nBall: {balls_bowled + 1}")
    user_input = int(input("Bowl a number (1-6): "))
    
    if user_input < 1 or user_input > 6:
        print("INVALID BOWL! Please enter a number between 1 and 6.")
        continue
    
    comp_input = random.randint(1, 6)
    print(f"Computer chose: {comp_input}")
    
    if user_input == comp_input:
        comp_wickets += 1
        print(f"COMPUTER OUT! Wickets: {comp_wickets}")
    else:
        comp_score += comp_input
        print(f"Computer Score: {comp_score}")
        
    balls_bowled += 1

print(f"\nComputer Innings Over! Final Score: {comp_score}/{comp_wickets}")

print("\n" + "="*30)
if user_score > comp_score:
    print(f"RESULT: You win! ({user_score} vs {comp_score})")
elif comp_score > user_score:
    print(f"RESULT: Computer wins! ({comp_score} vs {user_score})")
else:
    print("RESULT: It is a Draw!")
print("="*30)