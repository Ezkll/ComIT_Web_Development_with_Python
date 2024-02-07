## Unit 1
### Practice II : Introduction to logics
---

#### Build the truth tables for the following prepositional forms.
---
``~q v (p ^ q)``

| p | q | ~q | p ^ q | ~q v (p ^ q) |
|---|---|----|-------|--------------|
| T | T | F  | T     | T            |
| T | F | T  | F     | T            |
| F | T | F  | F     | F            |
| F | F | T  | F     | T            |

``~p -> q``

| p | q | ~p | ~p -> q |
|---|---|----|---------|
| T | T | F  | T       |
| T | F | F  | T       |
| F | T | T  | T       |
| F | F | T  | F       |

``p ^ q ↔ q ^ p``

| p | q | p ^ q | q ^ p | p ^ q ↔ q ^ p |
|---|---|-------|-------|---------------|
| T | T | T     | T     | T             |
| T | F | F     | F     | T             |
| F | T | F     | F     | T             |
| F | F | F     | F     | T             |

``p -> q ↔ q -> p``

| p | q | p ^ q | q ^ p | p ^ q ↔ q ^ p |
|---|---|-------|-------|---------------|
| T | T | T     | T     | T             |
| T | F | F     | F     | T             |
| F | T | F     | F     | T             |
| F | F | F     | F     | T             |

``a ^ (b v ~a)``

| a | b | ~a | b v ~a | a ^ (b v ~a) |
|---|---|----|--------|--------------|
| T | T | F  | T      | T            |
| T | F | F  | F      | F            |
| F | T | T  | T      | F            |
| F | F | T  | T      | F            |

#### Interpret the previous prepositional forms.
---
p: John traveled in the 8 A.M plane.

q: Peter arrived on time to the airport.

r: The project was presented to the board of directors.

s: The flight was delayed.

t: Peter travels on the plane.

m: x + y = 0.

n: x = 2.

v: y = -2.

``~q v (p ^ q)`` This can be interpreted as “Either it is not the case that Peter arrived on time to the airport, or both John traveled in the 8 A.M plane and Peter arrived on time to the airport.”

``~p -> q`` This can be interpreted as “If it is not the case that John traveled in the 8 A.M plane, then Peter arrived on time to the airport.”

``p ^ q ↔ q ^ p`` This can be interpreted as “John traveled in the 8 A.M plane and Peter arrived on time to the airport if and only if Peter arrived on time to the airport and John traveled in the 8 A.M plane.”

``p -> q ↔ q -> p`` This can be interpreted as “If John traveled in the 8 A.M plane then Peter arrived on time to the airport if and only if If Peter arrived on time to the airport then John traveled in the 8 A.M plane.”

``a ^ (b v ~a)`` This can be interpreted as “The equation x + y = 0 is true and either the equation x = 2 is true or it is not the case that the equation x + y = 0 is true.”

#### Build the truth tables for the following prepositional forms
   ---  
``p -> (q ->r)``

| p | q | r | q -> r | p -> (q -> r) |
|---|---|---|-------|-------------|
| T | T | T |   T   |      T      |
| T | T | F |   F   |      F      |
| T | F | T |   T   |      T      |
| T | F | F |   T   |      T      |
| F | T | T |   T   |      T      |
| F | T | F |   F   |      T      |
| F | F | T |   T   |      T      |
| F | F | F |   T   |      T      |

``(p ^ q) -> r``
| p | q | r | p ^ q | (p ^ q) -> r |
|---|---|---|------|------------|
| T | T | T |   T  |      T     |
| T | T | F |   T  |      F     |
| T | F | T |   F  |      T     |
| T | F | F |   F  |      T     |
| F | T | T |   F  |      T     |
| F | T | F |   F  |      T     |
| F | F | T |   F  |      T     |
| F | F | F |   F  |      T     |


#### Build the truth tables for the following prepositional forms
---
``(p -> q) ^ (q -> r)``
 p | q | r | p -> q | q -> r | (p -> q) ^ (q -> r)
---|---|---|-------|-------|---------------------
 T | T | T |   T   |   T   |         T           
 T | T | F |   T   |   F   |         F           
 T | F | T |   F   |   T   |         F           
 T | F | F |   F   |   T   |         F           
 F | T | T |   T   |   T   |         T           
 F | T | F |   T   |   F   |         F           
 F | F | T |   T   |   T   |         T           
 F | F | F |   T   |   T   |         T           

``( p -> q ) -> r``
 p | q | r | p -> q | (p -> q) -> r
---|---|---|-------|--------------
 T | T | T |   T   |      T       
 T | T | F |   T   |      F       
 T | F | T |   F   |      T       
 T | F | F |   F   |      T       
 F | T | T |   T   |      T       
 F | T | F |   T   |      F       
 F | F | T |   T   |      T       
 F | F | F |   T   |      F       

``p -> ( q -> r )``
 p | q | r | q -> r | p -> (q -> r)
---|---|---|-------|--------------
 T | T | T |   T   |      T       
 T | T | F |   F   |      F       
 T | F | T |   T   |      T       
 T | F | F |   T   |      T       
 F | T | T |   T   |      T       
 F | T | F |   F   |      T       
 F | F | T |   T   |      T       
 F | F | F |   T   |      T       
