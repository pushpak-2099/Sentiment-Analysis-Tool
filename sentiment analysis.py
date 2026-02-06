from textblob import TextBlob

print("welcome to sentiment analysing tool")

print("Enter the 'stop' to stop the program")

user_input=(input("enter your text: "))
while user_input.lower() !="stop":
  sentence=TextBlob(user_input) 
  if sentence.sentiment.polarity >=0.1 :
       print("the sentence is positive. ")
  elif -0.1 <= sentence.sentiment.polarity <= 0.1:
       print("the sentence is neutral.") 
  else  print (" the sentence is negative.")
     
  user_input=input("enter another statement: ")

print("thanks for using the tool.")




    


