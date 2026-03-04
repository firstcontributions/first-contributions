def check_my_word(word):
    # making it small letters first so it is easy
    word = word.lower()
    
    # reversing the word using a simple trick
    reverse_word = word[::-1]
    
    # checking if both are exactly same
    if word == reverse_word:
        print("Yay! The word", word, "is a palindrome!")
    else:
        print("Oh no! The word", word, "is not a palindrome.")

# testing my code below
check_my_word("radar")
check_my_word("hello")
