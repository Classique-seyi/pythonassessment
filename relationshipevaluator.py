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
  
  communication = get_valid_score("\nHow would you rate your communication skills? ")
  
  anger = get_valid_score("\nHow well do you handle your anger? ")
      
  
  jealousy = get_valid_score("\nHow well do you handle your jealousy? ")
        
 
  sense_humour = get_valid_score("\nHow would you rate your sense of humour and playfulness? ")
      
  generosity = get_valid_score("\nHow willing are you to share, give and reciprocate gestures? ")
      
  looks = get_valid_score("\nHow would you rate your physical appearance? and you better don't lie i can  clearly see it!!!: \n")
      

  scores = {
    "communication": communication,
    "anger_management": anger,
    "sense_of_humour": sense_humour,
    "generosity": generosity,
    "looks": looks
  }

  return scores

def calculate_total(scores):
    score_list = []
    for value in scores.values():
        score_list.append(value)

    total = sum(score_list)

    return total

def safety_check():
    red_flags = [
      "Manipulation or emotional abuse",
      "Controlling behaviour",
      "Threats, intimidation or physical aggression",
      "Harmful substance use that negatively affects behaviour(Excessive alcohol intake or smokes etc.)",
      "Cheating, repeated dishonesty or betrayal"
    ]

    identified_flags = []

    print("\nHave you engaged in any of the following behaviours?")
    print("Enter yes or no for each question.\n")
    
    
    for flag in red_flags:

        while True:
            answer = input(f"{flag}? \n").strip().lower()

            if answer == "yes":
                identified_flags.append(flag)
                break

            elif answer == "no":
                break

            else:
                print("Invalid response! Reply with Yes or No\n")

    return identified_flags

def evaluate_relationship(total, identified_flags):
    if identified_flags:
       return "NOT SAFE TO PROCEED"
    elif (total >= 40 and total <= 50):
        return "GREAT CHOICE"

    elif (total >= 25 and total < 40):
        return "PROCEED WITH CAUTION"

    else:
        return "NOT SAFE TO PROCEED"

def display_result(scores, total, verdict, identified_flags):

    print("=" * 55)
    print("              EVALUATION RESULTS")
    print("=" * 55)

    print(f"Communication skill: {scores['communication']}")
    print(f"Conflict Management: {scores['anger_management']}")
    print(f"Sense of humour: {scores['sense_of_humour']}")
    print(f"Generosity: {scores['generosity']}")
    print(f"Physical Appearance: {scores['looks']}")

    print(f"\nThe total rating is {total}")

    if identified_flags:
        print("\nRED FLAGS IDENTIFIED:")
        for flag in identified_flags:
            print(f" - {flag}")
    else:
        print("\nNO RED FLAGS REPORTED.")

    print(f"{verdict}")
  
def main():
    display_parameters()
    scores = collect_scores()
    total = calculate_total(scores)
    identified_flags = safety_check()
    verdict = evaluate_relationship(total, identified_flags)
    display_result(scores, total, verdict, identified_flags)
    

main()