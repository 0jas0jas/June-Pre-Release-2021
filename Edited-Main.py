
#This is a list containing all the possible tutor groups there can be.
PossibleTutorGroups = [
  "7A", "7B", "7C", "7D", "7E", "7F",
  "8A", "8B", "8C", "8D", "8E", "8F",
  "9A", "9B", "9C", "9D", "9E", "9F",
  "10A", "10B", "10C", "10D", "10E", "10F",
  "11A", "11B", "11C", "11D", "11E", "11F",
]

# This is an example of a REPEAT [this]... UNTIL[this] loop. What it, basically does is that it makes the user keep entering the tutor group until they enter the right value.
#Validation for variable[tutorGroup]
while True:
  tutorGroup = str(input('Enter the name of the tutor group: '))
  if(tutorGroup in PossibleTutorGroups): #This checks if the input is in the list on line 2 or not
    break
  print("Please Enter A Valid Tutor Group. Retry.")

#This is again a REPEAT.. UNTIL loop and it checks if the number of students 
#Validation for variable[numStudents]
while True:
  numStudents = int(input('Enter the number of students in the tutor group: '))
  if(numStudents >= 28 or numStudents <= 35):
    break
  print("Error. Invalid amount of students. Please enter again.")

#REPEAT... UNTIL loop to check if numCanditates is between 1 and 4 or not
#Validation for variable[numCandidates]
while True:
  numCandidates = int(input('Enter the number of candidates in the election. [max of four]: '))
  if(numCandidates >= 1 and numCandidates <= 4):
    break
  print("Error. Invalid amount of candidates, only 1-4. Please enter again")

#Empty Array: namesCandidates
#initializing variable: abstain
namesCandidates = []
abstain = 0


#Input names of candidates and add them to the string array, namesCandidate
for count in range(0, numCandidates):
  Candidate = input('Enter the name of candidate ' + str(count + 1) + ': ')
  namesCandidates.append(Candidate)

#ID-ing students...
#Store VoterID in a list(array), voterID

#Some Variables
voterID_used = []
Votes = [0]*numCandidates
Abstain = 0
for id in voterID_used:
  print(id)
for count in range(0, numStudents):
  while True:
    voterID = input("Please enter your unique voter number: ")
    if (voterID in voterID_used):
      print('Error. This voter number has already been used once, you cannot vote again')
    else:
      voterID_used.append(voterID)
      break
  print("-------------------------------")
  print("These are your voting options:")
  print("0. Abstain from this election.")
  optionNumber = 1
  for candidate in namesCandidates:
    print(str(optionNumber) + ". " + candidate)
    optionNumber = optionNumber + 1
  for i in range(0, numCandidates):
    print("Type", i+1, " to vote for ", namesCandidates[i] )
  print("Press 0 to abstain.")
  
  while True:
    VoteInput = int(input())
    if (VoteInput >= 0 and VoteInput <= numCandidates):
      break
    print("Error. Type the candidate number or type 0.")

  if VoteInput == 0:
    abstain = abstain + 1
  elif VoteInput == 1: 
    Votes[0] = Votes[0] + 1
  elif VoteInput == 2:
    Votes[1] = Votes[1] + 1
  elif VoteInput == 3:
    Votes[2] = Votes[2] + 1
  else:
    Votes[3] = Votes[3] + 1


#DISPLAYING THE RESULTS
print("----------------------")
print("Tutor Group: ", tutorGroup)
for count in range(0, numCandidates):
  print("Candidate Name: ", namesCandidates[count])
  print("Number of Votes: ", Votes[count])
print("Abstained: ", abstain)

winner = []
most = Votes[0]
for count in range(0, numCandidates):
  if Votes[count]>most:
    most = Votes[count]

for count in range(0, numCandidates):
  if Votes[count] == most:
    winner.append(namesCandidates[count])
  if len(winner) == 1:
    print("The winner is " + winner[1])
  else:
    #IN CASES OF TIE ( as described in Task 3 )
    print("---------------------------------------------------")
    print("THERE HAS BEEN A TIE! There will be a re-election.")
    numCandidates = len(winner)
    namesCandidates.clear()
    for count in range(len(winner)):
      namesCandidates[count] = winner[count]
    voterID_used.clear()
    for count in range(0, numStudents):
      while True:
        voterID = input("Please enter your unique voter number: ")
        if (voterID in voterID_used):
          print('Error. This voter number has already been used once, you cannot vote again')
        else:
          voterID_used.append(voterID)
          break
      print("-------------------------------")
      print("These are your voting options:")
      print("0. Abstain from this election.")
      for candidate in namesCandidates:
        print(str(optionNumber) + ". " + candidate)
        optionNumber = optionNumber + 1
      for i in range(0, numCandidates):
        print("Type", i+1, " to vote for ", namesCandidates[i] )
      print("Press 0 to abstain.")
    
      while True:
        VoteInput = int(input())
        if (VoteInput >= 0 and VoteInput <= numCandidates):
          break
        print("Error. Type the candidate number or type 0.")
      if VoteInput == 0:
        abstain = abstain + 1
      elif VoteInput == 1: 
        Votes[0] = Votes[0] + 1
      elif VoteInput == 2:
        Votes[1] = Votes[1] + 1
      elif VoteInput == 3:
        Votes[2] = Votes[2] + 1
      else:
        Votes[3] = Votes[3] + 1
  print("----------------------")
  print("Tutor Group: ", tutorGroup)
  for count in range(0, numCandidates):
    print("Candidate Name: ", namesCandidates[count])
    print("Number of Votes: ", Votes[count])
  print("Abstained: ", abstain)

  winner = []
  most = Votes[0]
  for count in range(0, numCandidates):
    if Votes[count]>most:
      most = Votes[count]

  for count in range(0, numCandidates):
    if Votes[count] == most:
      winner.append(namesCandidates[count])
      if (len(winner) == 1):
        print(winner[0], " is the winner.")
    






       

