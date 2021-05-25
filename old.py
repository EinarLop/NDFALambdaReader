import re

#{"q0": {"a": ["q0", "q1"], "b": ["q3"]}}
#

"""Summary
Within this program, you will be able to process a string of n characters in order to know if it accepted in the Non Deterministic Automata with lambda (NDFA-lambda) of the text File 1, found as test1.txt. 

If you want to try another Automata you should change the input from the method with open.
"""

with open("./test2.txt", "r") as f:
  """Opens the text file where the Automata is defined.
  
  Saves the first 4 lines as variables, 1- states, 2- alphaber, 3- initial states, 4- final states in dictionaries.

  Parameters
  ------
  file: the file where the Automata is defined.
  r: the mode in which we want to open the file, read.
  """
  contents = f.read().splitlines()
 
states = contents[0].split(",")
alphabet=contents[1].split(",")
alphabet.append("lambda")
initialState = contents[2]
finalStates = contents[3].split(",")

#Create array with transitions read from line 5 to end of the file
transitions =[]
for i in range(4, len(contents)):
  transition = {
  "state": "",
  "character":"",
  "result": []
}
  current = re.split(",|=>",contents[i])
 
  transition["state"] = current[0]
  transition["character"] = current[1]

  for j in range(2, len(current)):
    transition["result"].append(current[j])
  transitions.append(transition)

#Initialized array to save all completed dictionaries
completedDictionaries = []

#q0: dictonary 


#Create dictonaries for every state with empty transition array
for state in states:
  dictionary = {
    "state": "",
    "initialState": "",
    "finalState": "",
    "transitions": []    
}
  initial = False
  final = False
  tran = []
  if state == initialState:
    initial= True
  for finalstate in finalStates:
    if state == finalstate:
      final = True
      #Adds transitions to a temp array to then add them to the state's dictionary 
      #Comparing if current state has any transition in transitions array  
  for trans in transitions:
    if state == trans["state"]:
       tran.append({
         "character":trans["character"],
         "states": trans["result"]
   })

   ########################################################
#{"q0": {"a": ["q0", "q1"], "b": ["q3"]}}


dic = {}


def generateStates():
 
  for state in states:
    dic[state]= {}

  print(dic)
    
    
generateStates()
#   dictionary = {
#     "state": {""},
#     "initialState": "",
#     "finalState": "",
#     "transitions": []    
# }

  
  
      #Adds transitions to a temp array to then add them to the state's dictionary 
      #Comparing if current state has any transition in transitions array  
  # for trans in transitions:
  #   if state == trans["state"]:
  #      tran.append({
  #        "character":trans["character"],
  #        "states": trans["result"]
  #  })

   ########################################################
def generateTransitions():

  transitions =[]
  for i in range(4, len(contents)):
   
   

    print(contents[i])

  
    
   
    current = re.split(",|=>",contents[i])
    print(current)

    currentTransitions = current[2:]
    #print("Current transitions", currentTransitions)

    for character in alphabet:
      if character not in dic[current[0]]:
        dic[current[0]][character]= []

    #dic[current[0]] = {current[1]:"hpla"}
    
    
    dic[current[0]][current[1]] = currentTransitions

    
      
    

  print("dic",dic)
  
  #   transition["state"] = current[0]
  #   transition["character"] = current[1]

  #   for j in range(2, len(current)):
  #     transition["result"].append(current[j])
  #   transitions.append(transition)

  #Initialized array to save all completed dictionaries
  # completedDictionaries = []
generateTransitions()

   ########################################################


  #Assign the temp array to transitons dictonary of current state
  # dictionary["transitions"] = tran
  # #Assign other variables to dictionary attributes
  # dictionary["state"]= state
  # dictionary["initialState"]=initial
  # dictionary["finalState"]=final
  
  # #Add current dictonary to an array of completedDictionaries
  # completedDictionaries.append(dictionary)



# Simple transition function
def transition(state, character):
  """
  Processes the string with the transition function and returns a set of transitions.

  Parameters
  -------
  state: the state of the Automata
  character: the character that creates a transition with the state
  """
  current = {}
  for dic in completedDictionaries:
    if dic["state"] == state:
      current=dic
      for trans in current["transitions"]:
        if trans["character"] == character:
          if len(trans["states"] )!= 0:
            return trans["states"]
        #dict[state][character]



def transitionFunction(state, character):
  return dic[state][character]


print("Transitions",transitionFunction("q0", "lambda"))

def lambdaf(lambdaStates):
  """
  Processes states with the lambda function, returning a list of results.

  Parameters
  ------
  lambdaStates: the states which are going to be processed with the lambda function
  """
  visitados = []
  result = lambdaStates
 
  for state in result:
    current = transition(state,"lambda")
    if current != None:
      for tran in current:
        
        if tran not in visitados:
         
          visitados.append(tran)
          result.append(tran)
       
  return result

print("Old lamnda ", lambdaf(["q0"]))


def lambdaFunction(state):
  visited = []
  result=[]
  result.append(state)

  current= dic[state]["lambda"]
  if current != None:
    for state in current:
       if state not in visited:
        visited.append(state)
        result.append(state)
  return result

print("Lambda Fun", lambdaFunction("q0"))


    #if current != None:



  

def evaluateString(qi, word):
  """The state evaluates the string, processing the string with the extended transition function, using the formula.
  
  Parameters
  ----
  qi: The states that were processed previously with the lambdaf.

  word: The string that is being evaluated.
  """
  estadosLambda = lambdaf([qi])
  
  print("Lambda closure of q0: ", estadosLambda )
  print("")
  

  if len(word)==0:
    return estadosLambda
  
  while(len(word) != 0):
    print("Currently processing char: ",word[0] )
    print("")
    temp =[]
    #Normal transition function for each state in q0
    for state in estadosLambda:
     if transition(state,word[0]) != None:
      print("Normal transition:", state,",",word[0], "=>", transition(state,word[0]))
      temp = temp + (transition(state,word[0])) 
    estadosLambda = []
    print("Set of states obtained from the normal transition",temp)
    print("")
    #Lambda clousure  for each state in the array formed by the normal transition functions
    for newLState in temp:
     if lambdaf(newLState) != None:
       print("Lambda clousure:", newLState, "=>", lambdaf(newLState))
       estadosLambda.append(lambdaf(newLState))
    print("Set of states obtained from the lambda clousure",estadosLambda)
    print("")
    
    word=word[1:]
  
  tempEL = []
  print("Last lambda closures to get the final states")
  #One last lambda clousure for the final set of states obtained after the while
  for lState in estadosLambda:
      print("Lambda clousure:", lState, "=>", lambdaf(lambdaf(lState)))
      tempEL.append(lambdaf(lState))

  print("")
    
  return tempEL


def isFinalState(states):
  """Checks if the state is a final state
  Parameter
  ------
  states: the states of the Automata we want to check

  """
  for state in states:
    for finalState in finalStates:
       if state == finalState:
         return True
  return False
  

def menu():
  """Allows the user to choose an option for using the program.

  Parameters
  -------
  None
  
  """
  exit = False

  while not exit:
    #Ask user for option
    print("==========================================")
    print("Welcome to the NDFA-Lambda string evaluator! ")
    print("1. Evaluate a String")
    print("2. Exit")
    
    option= input("Please enter an option: ")
    print("")
    if option == "1":
      stri = ""
      
      print("Note: If you want to load your own Automata please copy-paste it in test1.txt")
      print("---------------------------")
      #Ask user for string
      stri= input("Enter the String you want to evaluate: ")
      print("")
      #Evaluate string with User string
      evaluatedString = evaluateString("q0",stri)
      print("Final set of states", evaluatedString)
      print("")

      print("List of final states in the automata", finalStates)
      print("")
       #Evaluate states form evaluatedString() and run isFinalState()
      if isFinalState(evaluatedString):
        print("The string is accepted")
      else:
        print("The string is not accepted")
     
      print("")
    
      
    elif option == "2":
        exit = True
    else:
      print("Please enter a valid option :(")
      
#menu()



      
  
