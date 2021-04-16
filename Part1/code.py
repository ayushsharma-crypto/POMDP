import sys

report = False
if sys.argv[1]=="REPORT":
    report = True
print(report)



roll_num_1 = 2019101004 # Ayush Sharma
roll_num_2 = 2019101024 # Nitin Chandak

last_4_digit_of_roll_no = 1004 # using roll_num_1
last_2_digit_of_roll_no = 4    # using roll_num_1

x = 1-(((last_4_digit_of_roll_no)%30 + 1)/100)
y = (last_2_digit_of_roll_no)%4 + 1

print(roll_num_1,roll_num_2)
print(x,y)

print("First Roll Number =",roll_num_1)
print("Second Roll Number =",roll_num_2)
print("Used Roll Number =",roll_num_1)
print("Value of x =",x)
print("Value of y =",y)



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

print("P(Observation = Red|State = Red) = ",p_red)
print("P(Observation = Green|State = Green) = ",p_green)
print("Initial Beliefs (S1 - S6) = ",belief)



for action in range(0,3):
    belief_upd = [0.0,0.0,0.0,0.0,0.0,0.0]
    if action == 0:
        for i in range(0,6):
            if i==0:
                belief_upd[i] = (1.00-p_red)*((1-x)*belief[0] + (1-x)*(belief[1]))
            if i==1:
                belief_upd[i] = (p_green)*(x*belief[0] + (1-x)*belief[2])
            if i==2:
                belief_upd[i] = (1.00-p_red)*(x*belief[1] + (1-x)*belief[3])
            if i==3:
                belief_upd[i] = (p_green)*(x*belief[2] + (1-x)*belief[4])
            if i==4:
                belief_upd[i] = (p_green)*(x*belief[3] + (1-x)*belief[5])
            if i==5:
                belief_upd[i] = (1.00- p_red)*(x*belief[4] + x*belief[5])

    if action == 1:
        for i in range(0,6):
            if i==0:
                belief_upd[i] = (p_red)*(x*belief[0] + x*belief[1])
            if i==1:
                belief_upd[i] = (1.00-p_green)*((1-x)*belief[0] + (x)*belief[2])
            if i==2:
                belief_upd[i] = (p_red)*((1-x)*belief[1] + (x)*belief[3])
            if i==3:
                belief_upd[i] = (1.00-p_green)*((1-x)*belief[2] + (x)*belief[4])
            if i==4:
                belief_upd[i] = (1.00-p_green)*((1-x)*belief[3] + (x)*belief[5])
            if i==5:
                belief_upd[i] = (p_red)*((1-x)*belief[4] + (1-x)*belief[5])

    if action == 2:
        for i in range(0,6):
            if i==0:
                belief_upd[i] = (1.00-p_red)*((x)*belief[0] + (x)*(belief[1]))
            if i==1:
                belief_upd[i] = (p_green)*((1-x)*belief[0] + (x)*belief[2])
            if i==2:
                belief_upd[i] = (1.00-p_red)*((1-x)*belief[1] + (x)*belief[3])
            if i==3:
                belief_upd[i] = (p_green)*((1-x)*belief[2] + (x)*belief[4])
            if i==4:
                belief_upd[i] = (p_green)*((1-x)*belief[3] + (x)*belief[5])
            if i==5:
                belief_upd[i] = (1.00- p_red)*((1-x)*belief[4] + (1-x)*belief[5])
    const = 0.0
    for j in range(0,6):
        belief[j] = belief_upd[j]
        const += belief[j]
    for j in range(0,6):
        belief[j] = belief[j]/const
        print("Action: ",action+1,"State: ",j+1,"Belief: ",belief[j])
    print()
