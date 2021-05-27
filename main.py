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

  def generateStates():
    """
    Generates the states for the Automata.
    """
    for state in states:
      dic[state]= {}
   
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


  
  try:
    with open("./" + filename , "r") as f:
      """
        Generates the states and characters according to the file selected.
      """
      contents = f.read().splitlines()
      states = contents[0].split(",")
      global alphabet
      alphabet=contents[1].split(",")
      alphabet.append("lambda")
      initialState = contents[2]
      global finalStates 
      finalStates= contents[3].split(",")

      generateStates()
      generateTransitions()

    return True
  except (FileNotFoundError, IsADirectoryError):
    print("Oops! That was no valid filename. Please try again ")
    return False
 
def transitionFunction(state, character):
  """
  Processes the string with the transition function and returns a dictionary with the transitions.

  Parameters
  -----
  state: the state of the Automata
  character: the character that has a transition with the state.
  """
  return dic[state][character]





def lambdaFunction(states):
  """
  Processes the states with the lambda function, returning a set of states.

  Parameters
  -----
  states: The states that are going to be processed with the lambda function.

  """

  visited = []
  result=[]
  for lstate in states:    
    if lstate not in result:
      result.append(lstate)
  for state in result:
    current= transitionFunction(state, "lambda")
    if current != None:
      for state in current:
        if state not in visited and state not in result:
          
          visited.append(state)
          result.append(state)
          print("===>", state, result )
  return result



def etf(state, string):
  """
  Processes the states with the extended transition function and a string. 

  Parameters
  ----------
  State: the states i

  """
  if len(string) == 1:
    return lambdaFunction(state)
  else:
    firstPart = string[:-1]
    lastChar= string[-1]
    
    etfRes = etf("q0", firstPart)
    
    print("Processing the character:", lastChar)
    tfRes=[]
    
    for etfState in etfRes:
      print(f'Processing the transition function of: {etfState} with {lastChar}')
      current = transitionFunction(etfState, lastChar)
      for c in current:
       if c not in tfRes:
         tfRes.append(c)
  

    lfRes = []
   
    print("Processing the lambda funtion of:", tfRes)
    curr = lambdaFunction(tfRes)
    for cu in curr:
      if cu not in lfRes:
        lfRes.append(cu)

    return lfRes

def isFinalState(finalStates, states):
  """
  Checks if the states given are final States in the Automata.

  Parameters
  -----
  finalStates: The list of states that are final in the automata
  stateS: The states that are going to be checked.
  """
  for state in states:
    if state in finalStates:
      return True
  else:
    return False


def menu():
  """Allows the user to choose an option for using the program.
  """
  exit = False

  while not exit:
    print("==========================================")
    print("Welcome to the NDFA-Lambda string evaluator! ")
    print("1. Evaluate a String")
    print("2. Exit")
    
    option= input("Please enter an option: ")
    print("")
    if option == "1":
      stri = ""
    
     
      filename= input("Please enter the name of the file (Ex: test1.txt): ")
      while not initialSetup(filename):
        filename= input("Please enter the name of the file (Ex: test1.txt): ")
        

      print("---------------------------")
      stri= input("Enter the String you want to evaluate: ")
      for s in stri:
        if s not in alphabet:
          print("The string contains charachters that are not available in the current language")
          return
          
    
      extended = etf("q0","x"+stri)
      print("")
      print("Final set of states", extended)
      print("")

      print("List of final states in the automata", finalStates)
      print("")
     
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
