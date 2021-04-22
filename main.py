import re

#Open txt file
with open("./test1.txt", "r") as f:
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

 #print(lambdaf(["q0"]))


def extendedTransition(qi,toProcess):

  result = []

  #BASE CASE: The String is empty
  if len(toProcess)==0:
    return lambdaf([qi])

  else:
    if len(toProcess)==1:
      
      for state in lambdaf([qi]):
        print("state",state)
        if transition(state,toProcess) != None:
          print("Appended")
          result.append(transition(state,toProcess))
        
      return result
      
    else:
       transition(extendedTransition(qi,toProcess[:-1]),toProcess[-1])


print(extendedTransition("q0", "a"))


  
# test = "hola"

# #Quitar primero
# print(test[1:])
# #Quitar ultimo
# print(test[:-1])
# #Último character
# print(test[-1])


#Extended transtion -> q0, lamba ->q0
# Extended transition(1st char)
  #transition normal(char que se agrego)
  #lambdaf(transition normal)
#le meto el segundo char a extended
#extended(1st char + 1)
  #solo uso el ultimo char que se agrego!!
  #transition normal(char que se agrego)
#se sigue hasta que extended transition complete el string 
