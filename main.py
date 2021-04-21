import re
with open("./test1.txt", "r") as f:
  contents = f.read().splitlines()
 
 

states = contents[0].split(",")
alphabet=contents[1].split(",")
initialState = contents[2]
finalStates = contents[3].split(",")


transitions =[]

completedDictionaries = []

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

#print(transitions)

# print(states)
# print(alphabet)
# print(initialState)
# print(finalStates)
# print(contents)


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
  for trans in transitions:
    if state == trans["state"]:
       tran.append({
         "character":trans["character"],
         "states": trans["result"]
   })

  dictionary["transitions"] = tran

  dictionary["state"]= state
  dictionary["initialState"]=initial
  dictionary["finalState"]=final
  print("==============")
  # print(dictionary)
  completedDictionaries.append(dictionary)



#print(completedDictionaries)


# {
#   {
#     "state": "q0",
#     "initialState": True,
#     "finalState": False,
#     "transitions": [
#       {
#         "alphabet": "a",
#       "states": ["q0","q1"]
#       },
#       {
#       "alphabet": "b",
#       "states": ["q2","q3"]
#       }
#       ]
#   }
# } 






# function (){
#   #Base case
#   if string.length = 0
#     return initialState

#   else
#   extendedTransitionFunction(transitionfunction(char))


# }



def transition(state, character):
  current = {}
  for dic in completedDictionaries:
    if dic["state"] == state:
      current=dic
      #print(current)
      for trans in current["transitions"]:
        if trans["character"] == character:
          return trans["states"]


#def extendedTransition():

  #xtendedTransitionFunction(transition())

def findLambdaStates(lambdaStates):
  s = []
  for j in lambdaStates:
    for i in completedDictionaries:
      if lambdaStates[j] == completedDictionaries["state"]:
        s.append(lambdaStates[j])

  


print(completedDictionaries)
def lambdaf(self,lambdaStates):
  
 
  
  if s == lambdaStates:
    return lambdaStates

  elif transition(s,"lambda") not in lambdaStates:
    lambdaf(transition(s, "lambda"))
    
  
  


      
 
  


#transition("q6", "b")


