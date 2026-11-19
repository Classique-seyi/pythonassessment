def play_hangman(word, guesses, max_attempts) -> tuple[str, str, list[str]]:
    max_guesses = 5
    wrong_guesses = []
    status = "playing"
    display = ""

    for char in word:
        if char not in 






