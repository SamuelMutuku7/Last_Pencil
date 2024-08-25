# We need to create a function that accepts a string as argument
def process_string(s):
    s = input()
    words = s.split()
    word_count = len(words)
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    print(word_count)
    print(reversed_string)


# The next line is for invoking the function, and you can replace 'your_string_here' with your actual string
process_string("Let's see how this works")