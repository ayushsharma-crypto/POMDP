# MDL Assignment 3, Part  2

* Ayush Sharma (2019101004)
* Nitin Chandak (2019101024)


<hr>

First Roll Number = 2019101004  

Second Roll Number = 2019101024  

Used Roll Number = 2019101004

LastFourDigitsOfRollNumber = 1004

x = 1 - (((LastFourDigitsOfRollNumber)%30 + 1) / 100) = 1 - 0.15 = 0.85

Success Reward = (RollNumber%90 + 10) = (2019101004%90 + 10) = 64


# Given Data



**Positions :**

* Possible Positions of an Agent or Target :

    | Pos_Grid         | col = 0 | col = 1 | col = 2 | col = 3 |
    | -                | -       | -       | -       | -       |
    |  <b>row = 0</b>  | (0, 0)  | (0, 1)  | (0, 2)  |  (0, 3) |
    |  <b>row = 1</b>  | (1, 0)  | (1, 1)  | (1, 2)  |  (1, 3) |

**Target's Actions :**

* Movement Probability Distribution of a Target is following:
    | Action      | STAY   | UP     | DOWN   | LEFT   | RIGHT  |
    | -           | -      | -      | -      | -      | -      |
    | Probability | 0.6    | 0.1    | 0.1    | 0.1    | 0.1    |
* If Target try to move out of the grid world, it will remain at the same pos. with  0.1 probability.
* The calling functionality of Target is independent of its movement.

    | Action      | Call On   | Call Off     |
    | -           | -         | -            |
    | Probability | 0.5       | 0.1          |


**Transition probabilities for the agent :**

* Since, x = 0.85 in our case. Hence, the following table:

    | Action              | STAY   | UP     | DOWN   | LEFT   | RIGHT  |
    | -                   | -      | -      | -      | -      | -      |
    | Success Probability | 1      | 0.85   | 0.85   | 0.85   | 0.85   |
    | Failure Probability | 0      | 0.15   | 0.15   | 0.15   | 0.15   |

* For, failure of `Non-STAY` action, the agent moves in the opposite direction.
* For either of success or failure, if Agent try to move outside the grid world it will stay at the same position with given success or failure prob. resp.


**Possible Observations from the Grid World :**

* All observation have 100% accuracy.

    | Observation |Target's Position w.r.t Agent's position |
    | -           | -                                       |
    | o1          | Same                                    |
    | o2          | Right                                   |
    | o3          | Below                                   |
    | o4          | Left                                    |
    | o5          | Above                                   |
    | o6          | Not in the 1 cell neighbourhood         |

**Rewards :**

* -1 for each step that Agent takes.
* (RollNumber%90 + 10) = 64 for reaching the target before the call is turned off.



# Question 1

**Target Cell :** (1, 0)

**Observation :** O6 with 100% accuracy

Therefore, initial equi-probable possible positions of the Agent: `(0,1)`, `(0,2)`, `(0,3)`, `(1,2)` and `(1,3)`.
Also, for each cell the agent is likely to be in, the target is equally likely to be or not to be on a call.

Thus,start states are following:-

S = { `(0,1,1,0,0)`,`(0,2,1,0,0)`,`(0,3,1,0,0)`,`(1,2,1,0,0)`,`(1,3,1,0,0)`,`(0,1,1,0,1)`,`(0,2,1,0,1)`,`(0,3,1,0,1)`,`(1,2,1,0,1)`, `(1,3,1,0,1)` } and all of them are equally likely.

Clearly, `|s| = 10`.

Therefore, belief state `b` i.e. probability distribution over our set of states will be:
```
b(s) = 0.1 ∀ s ∈ S 
otherwise b(s) = 0.
```

# Question 2

**Target Cell :** (1, 0)

**Observation :** O6




# Question 3

**Target Cell :** (1, 0)

**Observation :** O6




# Question 4

**Target Cell :** (1, 0)

**Observation :** O6




# Question 5

**Target Cell :** (1, 0)

**Observation :** O6