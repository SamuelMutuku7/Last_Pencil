import string

# put your code here
my_template = string.Template("Dear $username! It was really nice to meet you. Hopefully, you have a nice day! See you soon, $username!")
my_string = my_template.substitute(username=input())
print(my_string)