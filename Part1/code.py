import sys

report = False
if (len(sys.argv)>1) and (sys.argv[1]=="REPORT"):
    report = True



roll_num_1 = 2019101004 # Ayush Sharma
roll_num_2 = 2019101024 # Nitin Chandak

last_4_digit_of_roll_no = 1004 # using roll_num_1
last_2_digit_of_roll_no = 4    # using roll_num_1

x = 1-(((last_4_digit_of_roll_no)%30 + 1)/100)
y = (last_2_digit_of_roll_no)%4 + 1

if report:
    print("First Roll Number =",roll_num_1)
    print("Second Roll Number =",roll_num_2)
    print("Used Roll Number =",roll_num_1)
    print("Value of x =",x)
    print("Value of y =",y)
else:
    print(roll_num_1,roll_num_2)
    print(x,y)




p_red = 0.0 
p_green = 0.0

if y==1:
    p_red = 0.95
    p_green = 0.8

if y==2:
    p_red = 0.9
    p_green = 0.85

if y==3:
    p_red = 0.85
    p_green = 0.9

if y==4:
    p_red = 0.8
    p_green = 0.95

belief = [1/3,0.0,1/3,0.0,0.0,1/3]

if report:
    print("P(Observation = Red|State = Red) = ",p_red)
    print("P(Observation = Green|State = Green) = ",p_green)
    print("Initial Beliefs <S1 - S6> = ",belief)


def print_computation(i,pes,old_belief,coef,final_belief_i):
    if (len(coef)!=6) or (len(old_belief)!=6):
        print("Problem")
    
    print(f"b'(S[{i}]) = ",end="")
    print("{:.4f}".format(pes), end="")
    print(f" × ( ",end="")
    for k in range(6):
        print("{:.4f}".format(coef[k]),end="")
        print(f" × ",end="")
        print("{:.4f}".format(old_belief[k]),end="")
        print(" ",end="")
        if k!=5:
            print("+ ",end="")
    
    print(f") = ",end ="")
    print("{:.4f}".format(final_belief_i))


for action in range(0,3):
    belief_upd = [0.0,0.0,0.0,0.0,0.0,0.0]
    if action == 0:
        for i in range(0,6):
            if i==0:
                belief_upd[i] = (1.00-p_red)*((1-x)*belief[0] + (1-x)*(belief[1]))
                if report:
                    coef = [ 1-x, 1-x, 0, 0, 0, 0 ]
                    print_computation(i,1.00-p_red,belief,coef,belief_upd[i])
            if i==1:
                belief_upd[i] = (p_green)*(x*belief[0] + (1-x)*belief[2])
                if report:
                    coef = [ x, 0, 1-x, 0, 0, 0 ]
                    print_computation(i,p_green,belief,coef,belief_upd[i])
            if i==2:
                belief_upd[i] = (1.00-p_red)*(x*belief[1] + (1-x)*belief[3])
                if report:
                    coef = [ 0, x, 0, 1-x, 0, 0 ]
                    print_computation(i,1.00-p_red,belief,coef,belief_upd[i])
            if i==3:
                belief_upd[i] = (p_green)*(x*belief[2] + (1-x)*belief[4])
                if report:
                    coef = [ 0, 0, x, 0, 1-x, 0 ]
                    print_computation(i,p_green,belief,coef,belief_upd[i])
            if i==4:
                belief_upd[i] = (p_green)*(x*belief[3] + (1-x)*belief[5])
                if report:
                    coef = [ 0, 0, 0, x, 0, 1-x ]
                    print_computation(i,p_green,belief,coef,belief_upd[i])
            if i==5:
                belief_upd[i] = (1.00- p_red)*(x*belief[4] + x*belief[5])
                if report:
                    coef = [ 0,0,0,0,x,x ]
                    print_computation(i,1.00 - p_red,belief,coef,belief_upd[i])

    if action == 1:
        for i in range(0,6):
            if i==0:
                belief_upd[i] = (p_red)*(x*belief[0] + x*belief[1])
                if report:
                    coef = [ x,x,0,0,0,0 ]
                    print_computation(i,p_red,belief,coef,belief_upd[i])
            if i==1:
                belief_upd[i] = (1.00-p_green)*((1-x)*belief[0] + (x)*belief[2])
                if report:
                    coef = [ 1-x,0,x,0,0,0 ]
                    print_computation(i,1.00-p_green,belief,coef,belief_upd[i])
            if i==2:
                belief_upd[i] = (p_red)*((1-x)*belief[1] + (x)*belief[3])
                if report:
                    coef = [ 0,1-x,0,x,0,0 ]
                    print_computation(i,p_red,belief,coef,belief_upd[i])
            if i==3:
                belief_upd[i] = (1.00-p_green)*((1-x)*belief[2] + (x)*belief[4])
                if report:
                    coef = [ 0,0,1-x,0,x,0 ]
                    print_computation(i,1.00-p_green,belief,coef,belief_upd[i])
            if i==4:
                belief_upd[i] = (1.00-p_green)*((1-x)*belief[3] + (x)*belief[5])
                if report:
                    coef = [ 0,0,0,1-x,0,x ]
                    print_computation(i,1.00-p_green,belief,coef,belief_upd[i])
            if i==5:
                belief_upd[i] = (p_red)*((1-x)*belief[4] + (1-x)*belief[5])
                if report:
                    coef = [ 0,0,0,0,1-x,1-x ]
                    print_computation(i,p_red,belief,coef,belief_upd[i])

    if action == 2:
        for i in range(0,6):
            if i==0:
                belief_upd[i] = (1.00-p_red)*((x)*belief[0] + (x)*(belief[1]))
                if report:
                    coef = [ x,x,0,0,0,0 ]
                    print_computation(i,1.00-p_red,belief,coef,belief_upd[i])
            if i==1:
                belief_upd[i] = (p_green)*((1-x)*belief[0] + (x)*belief[2])
                if report:
                    coef = [ 1-x,0,x,0,0,0 ]
                    print_computation(i,p_green,belief,coef,belief_upd[i])
            if i==2:
                belief_upd[i] = (1.00-p_red)*((1-x)*belief[1] + (x)*belief[3])
                if report:
                    coef = [ 0,1-x,0,x,0,0 ]
                    print_computation(i,1-p_red,belief,coef,belief_upd[i])
            if i==3:
                belief_upd[i] = (p_green)*((1-x)*belief[2] + (x)*belief[4])
                if report:
                    coef = [ 0,0,1-x,0,x,0 ]
                    print_computation(i,p_green,belief,coef,belief_upd[i])
            if i==4:
                belief_upd[i] = (p_green)*((1-x)*belief[3] + (x)*belief[5])
                if report:
                    coef = [ 0,0,0,1-x,0,x ]
                    print_computation(i,p_green,belief,coef,belief_upd[i])
            if i==5:
                belief_upd[i] = (1.00- p_red)*((1-x)*belief[4] + (1-x)*belief[5])
                if report:
                    coef = [ 0,0,0,0,1-x,1-x ]
                    print_computation(i,1.00-p_red,belief,coef,belief_upd[i])
    const = 0.0
    for j in range(0,6):
        belief[j] = belief_upd[j]
        const += belief[j]
    if report:
        print(f"Normalization Factor = ",end="")
        print("{:.4f}".format(const))
        print()
    for j in range(0,6):
        belief[j] = belief[j]/const
        if report:
            print("Action: ",action+1,"State: ",j+1,"New Belief: ",belief[j])
    if report:
        print()
