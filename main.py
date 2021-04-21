import re

#Open txt file
with open("./test2.txt", "r") as f:
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
          return trans["states"]

# print(completedDictionaries)
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

print(lambdaf(["q0"]))



