import random

def choose_word():
  """
  Picks a random word from a list of words.
  """
  words = ["apple", "banana", "orange", "computer", "python"]
  return random.choice(words)

def hangman():
  """
  Implements the hangman game logic.
  """
  word = choose_word()
  word_letters = set(word)  # Letters in the word as a set
  alphabet = set('abcdefghijklmnopqrstuvwxyz')
  guessed_letters = set()  # Letters guessed by the player
  attempts = 6

  while len(guessed_letters) < len(word_letters) and attempts > 0:
    print("You have", attempts, "attempts left.")
    # Show the word with placeholders for unguessed letters
    print(' '.join(letter if letter in guessed_letters else '_' for letter in word))

    # Get player input
    while True:
      guess = input("Guess a letter: ").lower()
      if len(guess) != 1 or guess not in alphabet:
        print("Invalid input. Please enter a single letter.")
      elif guess in guessed_letters:
        print("You already guessed that letter. Try again.")
      else:
        break

    guessed_letters.add(guess)

    if guess in word_letters:
      print("Good guess!")
    else:
      attempts -= 1
      print("Wrong guess.")

  if attempts == 0:
    print("You ran out of guesses. The word was:", word)
  else:
    print("Congratulations! You guessed the word:", word)

play_again = "yes"
while play_again.lower() in ("yes", "y"):
  hangman()
  print("Do you want to play again?")
  play_again = input()
