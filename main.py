import csv
import pandas
import os
import argparse



class Team:
    def __init__(self,name,score):
        self._name = name
        self._score = score
    
    # Using @property decorator
    
    # Getter method
    @property
    def name(self):         
        return self._name
    
    @property
    def score(self):    
        return self._score
    
    # Setter method
    @name.setter
    def name(self, a):        
         self._name = a

     # Setter method
    @score.setter
    def score(self, a):        
         self._score = a


def GetTeamOrCreate(teams,name):
    for team in teams:
        if team.name == name:
            t = team
            teams.remove(team)
            return t
    return Team(name,0)


def main():
    with open('input_data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', lineterminator='\n')       
        teams = [] 
        for row in spamreader:      

            t1name = row[0][0:-2]
            t1score =  row[0][-1:]

            t2name = row[1][1:-2]
            t2score =  row[1][-1:]

            T1 = GetTeamOrCreate(teams,t1name)                
            T2 = GetTeamOrCreate(teams,t2name)  
           # print("MATCH:")          
           # print("Match results T1: ",T1.name)
           # print("Match results T1: ",T1.score)
           # print("Match results T2: ",T2.name)
           # print("Match results T2: ",T2.score)
            
            # Check who won and return score
            if t1score > t2score:
                # T1 won 
                T1.score = T1.score + 3
            elif t1score < t2score:
                # T2 won 
                T2.score = T2.score + 3
            else:
                # Draw
                T1.score = T1.score + 1
                T2.score = T2.score + 1

            teams.append(T1)
            teams.append(T2)
       
        def myFunc(e):
            return e.name
        def myFunc2(e):
            return e.score
        # Arrange in decending order (score) + alphabetically
        teams.sort(key=myFunc,reverse=False)
        teams.sort(key=myFunc2,reverse=True)
        
        #Add index
        count = 0 
        
        for team in teams:
            
           # Add ranking with conditions
           count = count +1 
           
           # Check if points are equal
           if team.score == 1:
               team.score = team.score,'pt'
           elif team.score > 1:
               team.score = team.score,'pts'   
           else:
               team.score = team.score,'pts'    
               
           #string and split
           x = str(team.score)
           x = x.replace("(","")
           x = x.replace(")","")
           x = x.replace("'","")
           x = x.replace(",","")
           
           
           
           # {} tell format how to order the data eg. where data needs to go. (count into {})
           print("{}. {}, {}".format(count,team.name,x)) 
           

if __name__ == "__main__":
    main()

