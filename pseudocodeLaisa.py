name=input("Hey you! What's your name? ")
print("hello, it's really nice to meet you", name.title())

game=input("would you like to play a quiz of 5 questions?")

if game=="yes" or game=="Yes" or game=="YES" or game=="sure" or game=="Sure" or game=="SURE" or game=="ok" or game=="OK" or game=="Ok" or game=="OKAY" or game=="Okay" or game=="okay" or game== "yeah" or game=="Yeah" or game=="YEAH" or game=="yep" or game=="Yep" or game=="YEP" or game=="yup" or game=="Yup" or game=="YUP" or game=="ya" or game=="Ya" or game=="YA":
  print("okay, let's get started!")

else:
  print("okay, maybe next time! Bye!")
  exit()
  
question_number1=input("what is the capital of Brazil? ")
if question_number1 == "Brasilia" or question_number1 == "brasilia":
  print("yes!you're correct!")

else:
  print("sorry, wrong answer! try one more time!")

question_number2=input("what language do brazilians speak? ")
if question_number2 == "portuguese" or question_number2 == "Portuguese":
  print("yes!you're correct!")

else:
  print("sorry, wrong answer! try one more time!")

question_number3=input("what is the name of the current president of Brazil? ")
if question_number3=="Lula" or question_number3 == "lula":
  print("yes! you're correct!")
elif question_number3=="Bolsonaro" or question_number3=="bolsonaro":
  print("thank god you're wrong!")
else:
  print("sorry, wrong answer! try one more time!")

question_number4=input("when did Brazil gain independence? ")
if question_number4=="1822":
  print("yes! you're correct!")

else:
  print("sorry, wrong answer! try one more time!")

question_number5=input("How many times Brazil has won the world cup? ")
if question_number5=="5":
  print("yes! you're correct!")
else:
  print("sorry, wrong answer! try one more time!")

if question_number1 == "Brasilia" or question_number1 == "brasilia" and \
 question_number2 == "portuguese" or question_number2 == "Portuguese" and \
 question_number3 == "Lula" or question_number3 == "lula" and \
 question_number4 == "1822" and \
 question_number5 == "5":
 print("congratulations! you got all the questions right!!")

else:
  print("sorry! you almost got all the questions right. Try it again!")

