from survey import AnonymousSurvey

question="What language did you first learn to speak?"
my_survery=AnonymousSurvey(question)

my_survery.show_question()
print("Enter 'q' at any time to quit.\n")
while 1:
    response=input("Language: ")
    if response == 'q':
        break
    my_survery.store_response(response)

print("\nThank you to everyone who participated in the survery!")
my_survery.show_results()