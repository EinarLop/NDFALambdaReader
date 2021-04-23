import re

#Open txt file
with open("./test3.txt", "r") as f:
  contents = f.read().splitlines()
 
#Save first 4 lines as variables(states,alphabet, initialStates, finalStates)
states = contents[0].split(",")
alphabet=contents[1].split(",")
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

#Initialized array to save all completed dicronaries
completedDictionaries = []

#Create a dictonaries for every state with empty transition array
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
      #Add transitions to a temp array to then add them to the state's dictionary 
      #Comparing if current state has any transition in transitions array  
  for trans in transitions:
    if state == trans["state"]:
       tran.append({
         "character":trans["character"],
         "states": trans["result"]
   })
 
  #Assign the temp array to transitons dictonary of current state
  dictionary["transitions"] = tran
  #Assign other variables to dictionary attributes
  dictionary["state"]= state
  dictionary["initialState"]=initial
  dictionary["finalState"]=final
  
  #Add current dictonary to an array of completedDictionaries
  completedDictionaries.append(dictionary)



# Simple transition function
def transition(state, character):
  current = {}
  for dic in completedDictionaries:
    if dic["state"] == state:
      current=dic
      for trans in current["transitions"]:
        if trans["character"] == character:
          if len(trans["states"] )!= 0:
            return trans["states"]
          

#print(completedDictionaries)
# print("=============")
# print(transition("q3", "b"))

def lambdaf(lambdaStates):
  
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


 ##############################################

def xTest(qi, toProcess,results):
  
  states = lambdaf([qi])
  result = results

  if len(toProcess)==0:
    return qi
  
  if len(toProcess)==1:
    for res in states:
      transition(res, toProcess)
      if transition(res,toProcess) != None:
        if isinstance(lambdaf(res), str): 
          result = result + [transition(res,toProcess)]
        else:
          result = result + transition(res,toProcess)
    return result

  else:
    for state in states:
      if transition(state, toProcess[0]) != None:
        result=result + transition(state, toProcess[0])
     
        for res in result:
          if  lambdaf(res) != None:
            if isinstance(lambdaf(res), str): 
              result = result + [lambdaf(res)]
            else:
              result = result + lambdaf(res)
      
    result = list(set(result))

    for ans in result:
      return xTest(ans,toProcess[1:],result)
    

#print(xTest("q0", "ab", []))    



#itTrans(qi,string)
# 
# estadosLambda=lamdaf(qi)

# string.len = 0
#   estadosLambda

# while(sting.len != 1)

# evaluar primer char de strig en trans function normal
# usando estadosLambda como state

# evaluamos lambda de todos los estados antes mencionados = lambda states

# quitamos un char del string
# =================





def lastTry(qi, word):
  estadosLambda = lambdaf([qi])
  

  if len(word)==0:
    return estadosLambda
  
  while(len(word) != 0):
    temp =[]
    for state in estadosLambda:
     if transition(state,word[0]) != None:
      temp = temp + (transition(state,word[0])) #POSIBLE ERROR ARRAY DENTRO ARRAY
    estadosLambda = []
   
    for newLState in temp:
     if lambdaf(newLState) != None:
       estadosLambda.append(lambdaf(newLState))
    
    word=word[1:]
  return estadosLambda



print(lastTry("q0", "bbbb"))
    

#q1,q3,q4,q5,q6,q7

      
  
