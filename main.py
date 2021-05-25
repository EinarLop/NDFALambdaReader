import re
"""Summary
Within this program, you will be able to process a string of n characters in order to know if it accepted in the Non Deterministic Automata with lambda (NDFA-lambda) of your text file. 
"""

dic = {}


def initialSetup(filename):
  """Sets up the name of the file in which the Automata is defined, and reads its content. 

  In the function with open, it saves the first 4 lines as variables, 1- states, 2- alphaber, 3- initial states, 4- final states in dictionaries.

  Parameters
  -------
  filename: The file where the Automata is defined.
  """
  
  with open("./" + filename , "r") as f:
    contents = f.read().splitlines()
    
  states = contents[0].split(",")
  alphabet=contents[1].split(",")
  alphabet.append("lambda")
  initialState = contents[2]
  global finalStates 
  finalStates= contents[3].split(",")
  
 
  def generateStates():
    """
    Generates the states for the Automata.
    """
    for state in states:
      dic[state]= {}
      
  generateStates()
  

  def generateTransitions():
    """
    Generates the transitions on the file, saving them on the dictionary.
    """
    for i in range(4, len(contents)):
      current = re.split(",|=>",contents[i])
      currentTransitions = current[2:]
      for character in alphabet:
        if character not in dic[current[0]]:
          dic[current[0]][character]= []
      dic[current[0]][current[1]] = currentTransitions
      
  generateTransitions()



###################################################
def transitionFunction(state, character):
  """
  Processes the string with the transition function and returns a dictionary with the transitions.

  Parameters
  -----
  state: the state of the Automata
  character: the character that has a transition with the state.
  """
  return dic[state][character]
###################################################


###################################################
def lambdaFunction(state):
  """
  Processes the states with the lambda function, returning a set of states.

  Parameters
  -----
  states: The states that are going to be processed with the lambda function.

  """
  visited = []
  result=[]
  result.append(state)
 
  for state in result:
    current= transitionFunction(state, "lambda")
    if current != None:
      for state in current:
        if state not in visited:
          visited.append(state)
          result.append(state)
  return result
###################################################


##################################################
def etf(state, string):
  """
  
  """
  if len(string) == 1:
    return lambdaFunction(state)
  else:
    firstPart = string[:-1]
    lastChar= string[-1]
    # print(firstPart, lastChar)
    
    etfRes = etf("q0", firstPart)
    
    print("Processing the transition function with:", lastChar)
    tfRes=[]
    
    for etfState in etfRes:
      print(f'Processing the transition function of: {etfState} with {lastChar}')
      current = transitionFunction(etfState, lastChar)
      for c in current:
       if c not in tfRes:
         tfRes.append(c)
      # print("The result of the extended transition function is:", tfRes)

    lfRes = []
   
    for tfState in tfRes:
      print("Processing the lambda funtion of:", tfState)
      curr = lambdaFunction(tfState)
      for cu in curr:
        if cu not in lfRes:
         lfRes.append(cu)

    return lfRes
###################################################


def isFinalState(finalStates, states):
  for state in states:
    if state in finalStates:
      return True
  else:
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
    
      filename= input("Please enter the name of the file (Ex: test1.txt): ")
      initialSetup(filename)
    
      
      # print("Note: If you want to load your own Automata please copy-paste it in test1.txt")
      print("---------------------------")
      #Ask user for string
      stri= input("Enter the String you want to evaluate: ")
      print("")
      #Evaluate string with User string
      extended = etf("q0","x"+stri)
      print("Final set of states", extended)
      print("")

      print("List of final states in the automata", finalStates)
      print("")
       #Evaluate states form evaluatedString() and run isFinalState()
      if isFinalState(finalStates ,extended):
        print("The string is accepted")
      else:
        print("The string is not accepted")
     
      print("")
    
      
    elif option == "2":
        exit = True
    else:
      print("Please enter a valid option :(")
      
menu()