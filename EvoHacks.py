def Home():
  print("Welcome to EVO Jobs!!")
  question= input ("Do You Have an Account?: ")
  if question.lower()== 'yes':
    Username= input("Enter Username: ")
    password= input("Enter Paswword: ")
    next = input("Type 'next' to enter personal info: ")
    if next == "next":
      print("----------")
      Personal()
    else:
      print("Incorrect entry! We'll take that as a next!")
      Personal()
        
  else :
    print("Welcome! Create an account ")
    Username= input("Enter Username: ")
    password= input("Enter Paswword: ")
    next1 = input("Type 'next' to enter personal info: ")
    if next1 == "next":
      print("----------") 
      Personal()
    else:
      print("Incorrect entry!  We'll take that as a next!")
      Personal()
      
def Personal():
  name = input("Enter your name: ")
  print("Hello " + name + " ,Thanks for joining Evo")
  print("----------")
  ed= input("Enter your highest education level \n A: Highschool diploma or GED \n B: Some highschool \n C: College diploma  \n D: Some college \n E: Graduate degree \n : ")
  if ed.lower() == "c":
    major = input("Enter your major:")
  if ed.lower() == "d":
    major = input("Enter your major:")
  if ed.lower() == "e":
    major = input("Enter your major:")
  else:
    print("Thats awesome!")
  age = input("Are you 18+ ? (yes/no): ")
  skills= input("Enter 3 your best hard and soft skills: ")
  print("Personal info updated!!")
  print("----------")
def Quest():
  print("Welcome to the Questionaire, Where we will find what work environment is best for you! ")
  dn = input("Do you prefer to work day or night?: ")
  pr = input("Do you prefer to work in A: person or B: remote?: ")
  travel = input("How far are you willing to travel? \n A: Under 5miles \n B: 5-25miles \n C: 25+miles \n  : ")  
  sal = input("What is your minimum salary expectation? ")
  fp = input("Do you prefer to work full or part time?: ")
  print("Here's Your report =)")
  x =""
  y =""
  z =""
  v =""
  if dn == "night":
    x = "night owl"
  else:
    x = "early bird"
  if pr == "a":
    y = "In person"
  else:
    y ="Remote"
  if travel == "a":
    z = "homelanding"
  if travel == "b":
    z = "traveling"
  else:
    z  ="voyaging"
  if fp == "full time":
    v = "full time"
  else:
    v = "part time"
 
  report= print("You are a " + v + " , " + y + " , " + z  + " , " + x +" looking to earn a minimum of " + sal)
  print("----------")
  print(report)
  print("searching for matches... ")
  print("----------")
  print("Congratulations! We've matched you with the Lincoln Financial Group as a Senior Engineer in Washington,DC")
  
  
Home()
Quest()
# def Gtky():
#   print("Lets get to know you!") 
# def key
'''
if "voyaging" in report:

    print("Congratulatons!! We've matched you with the   Lincoln Financial group

as an Engineer in Washington,DC")

  if SeniorEngineer in report:

    print("Congratulations!! We've matched you with the   Lincoln Financial group as a Senior Engineer in Washington,DC")

  if JuniorDeveloper in report:

    print("Congratulations!! We've matched you with the   Lincoln Financial group as a Junior developer in Washington,DC")

  if Deveoper in report:

    print("Congratulations!! We've matched you with the   Lincoln Financial group as a developer in Washington,DC")

  else:

    print("Unfortunately we have no matches for you")

    re = print("Would you like to reassess (Y/N)? ")

    if re == "Y":
'''
