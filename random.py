import getpass
import os

def display_parameters():
    while True:
        status = input("Would you like to be my partner?(Yes/No) ").strip().lower()

        if status == "yes":
            print("\n" + "=" * 60)
            print('''\nWelcome to Oluwaseyi's Relationship Evaluator
\nKindly evaluate yourself on a scale of 1 to 10.
 \nYour responses will be used to determine your relationship eligibility.
''')
            print("=" * 60)
            return True
        
        elif status == "no":
            print("This relationship is a do or die affair!!! Go back and type yes")

        else:
            print("Option can either be Yes or No.")

def get_valid_score(prompt: str):
  while True:
    try:
      user_input = int(input(prompt))
      if user_input < 1 or user_input > 10:
        print("Invalid score, Kindly rate on a scale of 1 to 10!!")
        continue
    except ValueError:
      print("Invalid score, Input a valid number")
      continue

    return user_input
  
def collect_scores():
    
    communication = get_valid_score("\nHow would you rate your communication skills?\n")
    
    anger = get_valid_score("\nHow well do you handle your anger?\n")
            
    jealousy = get_valid_score("\nHow well do you handle your jealousy?\n")
           
    accountability = get_valid_score("\nHow would you rate your level of accountability?\n(particularly your ability to admit when you're wrong, apologize sincerely and make efforts to improve):\n")
    
    sense_humour = get_valid_score("\nHow would you rate your sense of humour and playfulness?\n")
            
    generosity = get_valid_score("\nHow willing are you to share, give and reciprocate gestures?\n")
          
    looks = get_valid_score("\nHow would you rate your physical appearance?\n and you better don't lie i can  clearly see it!!!:\n")

    honesty = get_valid_score("\nHow would you rate your level of honesty?\n(ability to tell the truth and keep your promises):\n")
            
    commitment = get_valid_score("\nHow would you rate your level of commitment and faithfulness?\n(particularly your ability to remain loyal, respect relationship boundaries and stay commited to your partner):\n")

    financial = get_valid_score("\nHow would you rate your level of financial stability and responsibility?\n(particularly your ability to afford basic necessities, manage your finances, meet financial obligations and make thoughtful decisions):\n")

    scores = {
        "communication": communication,
        "anger_management": anger,
        "jealousy_management": jealousy,
        "accountability": accountability,
        "sense_of_humour": sense_humour,
        "generosity": generosity,
        "looks": looks,
        "honesty": honesty,
        "commitment": commitment,
        "financial_stability": financial
    }

    return scores

def calculate_total(scores):
    score_list = []
    for value in scores.values():
        score_list.append(value)

    total = sum(score_list)
    return total

def evaluate_relationship(total):

    if (total >= 70 and total <= 100):
        return "GREAT CHOICE"

    elif (total >= 50 and total < 70):
        return "SAFE TO PROCEED"

    else:
        return "PROCEED WITH CAUTION"

def admin_access():
    
    stored_password = os.getenv("RELATIONSHIP_ADMIN_PASSWORD")

    if not stored_password:
        print("No admin password configured.")
        stored_password = getpass.getpass("Create an admin password: ")

    if not stored_password:
        print("Password cannot be empty.")
        return False
    
    trial = 0

    while trial < 3:
        password = getpass.getpass("Enter the admin password: ")

        if password == stored_password:
            print("\nAccess granted. Welcome, Admin!")
            return True
        else:
            trial += 1
            print("\nAccess denied. Incorrect password.")

    print("Too many attempts!")
    return False

    
def display_result(scores, total, verdict):

    print("=" * 55)
    print("              EVALUATION RESULTS")
    print("=" * 55)

    print(f"Communication skill: {scores['communication']}")
    print(f"Anger Management: {scores['anger_management']}")
    print(f"Jealousy Management: {scores['jealousy_management']}")
    print(f"Accountability: {scores['accountability']}")
    print(f"Sense of humour: {scores['sense_of_humour']}")
    print(f"Generosity: {scores['generosity']}")
    print(f"Physical Appearance: {scores['looks']}")
    print(f"Honesty: {scores['honesty']}")
    print(f"Commitment: {scores['commitment']}")
    print(f"Financial Stability: {scores['financial_stability']}")

    print(f"\nThe total rating is {total}")

    print(f"{verdict}")
  
def main():
    status = display_parameters()
    if status:
        scores = collect_scores()
        total = calculate_total(scores)
        verdict = evaluate_relationship(total)
        print("\n" + "=" * 60)
        print("Thank you for taking the evaluation.")
        print("=" * 60)

       
        if admin_access():
            display_result(scores, total, verdict)
        else:
            print("\nWrong password. Access denied.")
            
    else:
        print("\nYou chose not to proceed with the evaluation. Goodbye!")

if __name__ == "__main__":
    main()



# read -s -p "Set admin password: " RELATIONSHIP_ADMIN_PASSWORD
# echo
# export RELATIONSHIP_ADMIN_PASSWORD