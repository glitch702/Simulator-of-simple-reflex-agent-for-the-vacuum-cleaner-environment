
# A and 0 -- leftcell
# B and 1 -- rightcell
# 1 means cell is dirty
# 0 means cell is clean

import random

def statespace(leftcell,rightcell,startpos): 
    p=""
    if startpos == 0:
        p="A"
    else: 
        p="B"
    s=" --> A"+str(leftcell)+"B"+str(rightcell)+"Pos"+p

    return s



def runSimulation(startpos,leftcell,rightcell,scen):
    score=0 # score for performance
    action=1 # 1000 actions required
    a=list()
    
    
    print("\nSCENARIO NO - ",scen)
    print("\nSimulating . . . \n")
    s=statespace(leftcell,rightcell,startpos)
    a.append(s)
    
    while action <= 1000 :
        
        if startpos==0: # if we are in leftcell
            print("Current state - ",leftcell,rightcell)
           
            print("Position : left")
            if leftcell==1:
                print("Action : Suck")
                #suck
                score+=1
                leftcell=0
                action+=1
                print("Score : ",score,"\n")
                s=statespace(leftcell,rightcell,startpos)
                a.append(s)
            else:
                
                newpos = random.randint(0,1)
                if newpos == 0:
                    print("Action = Stay (Can't go left. Bot is already here in leftcell).")
                    action+=1
                    print("Score : ",score,"\n")
                    s=statespace(leftcell,rightcell,startpos)
                    a.append(s)
                else:
                    print("Action : Move Right")
                    startpos=1
                    action+=1
                    print("Score : ",score,"\n")
                    s=statespace(leftcell,rightcell,startpos)
                    a.append(s)
        else:
            print("Current state - ",leftcell,rightcell)
            
            print("Position : Right")
            if rightcell==1:
                print("Action : Suck")
                #suck
                score+=1
                rightcell=0
                action+=1
                print("Score : ",score,"\n")
                s=statespace(leftcell,rightcell,startpos)
                a.append(s)
            else:
                
                newpos = random.randint(0,1)
                if newpos == 1:
                    print("Action = Stay (Can't go right. Bot is already here in rightcell).")
                    action+=1
                    print("Score : ",score,"\n")
                    s=statespace(leftcell,rightcell,startpos)
                    a.append(s)
                else:

                    print("Action : Move Left")
                    startpos=0
                    action+=1
                    print("Score : ",score,"\n")
                    s=statespace(leftcell,rightcell,startpos)
                    a.append(s)
    print("State space graph - ")
    for i in a:
        print(i,end="")
    print()    

def main() :
    print("\nVACUUM CLEANER ENVIRONMENT\n")

    print("CURRENT STATE IS 0 0 IMPLIES A IS CLEAN & B IS CLEAN")
    print("CURRENT STATE IS 1 1 IMPLIES A IS DIRTY & B IS DIRTY")
    print("CURRENT STATE IS 1 0 IMPLIES A IS DIRTY & B IS CLEAN")
    print("CURRENT STATE IS 0 1 IMPLIES A IS CLEAN & B IS DIRTY\n")

    print("STATE SPACE GRAPH CONVENTION")
    print("A0B0PosB means A IS CLEAN B IS CLEAN AND CURRENT POSITION IS B")
    print("A1B0PosA means A IS DIRTY B IS CLEAN AND CURRENT POSITION IS A")

    scen=1 # scenario number

    # to create the 8 different starting scenarios
    for startpos in range(2):
        for A in range(2):
            for B in range(2):
                runSimulation(startpos,A,B,scen)
                scen+=1
                
if __name__ == "__main__" :
    main()