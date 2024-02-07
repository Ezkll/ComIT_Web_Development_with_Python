
  

### *Lecture Notes:*

  

>This will contain lecture notes from the ComIT course: Web Development with Python

---

  

### *Propositional Logic*
- Proposition
- Atomic
- Molecular
- Link terms or Connectives
  

    #### *Proposition*

    Sentence that describes a property about someone or something
    It has precise words and clear sense.
    Can be evaluated as True or False


    #### *Atomic*
    Simplest Propositions that are indivisible

    *John goes to the movies*
    *It is raining today*
    *It is sunny today*

    #### *Molecular*

    Composed of atomic propositions joined by link terms or connectives

    #### *Connectives*
    - Link terms (or connectives): It links 2 propositions.

    - Linked propositions can be atomic as well as molecular
    propositions.

        **Conjunction** ***AND*** : **^**. Connects 2 propositions stating that the two occur simultaneously.
        >John goes to the movies ***and*** María makes supper.
    
        **Disjunction** ***OR*** : **v**. Connect 2 propositions stating that at least *one of the two things happens or both at the same time*.
        >John goes to the movies or María makes supper.

        **Negation** ***NOT*** : **~**. It does not "connect" between two, but applies to one. Denies what happens in the proposal to which it applies.
        >María does not make supper. I do not live in Uruguay.
### *Truth Tables*
When interpreting the atomic propositions these can be True
or False, and this is determined by contrasting the enunciated
with the reality.

>*“It’s morning.”*

>*“The windows is open.”*

The molecular propositions can be True or False too, but are
determined from the truth or falsity of their atomic
propositions first, and then evaluating the connectives.

>*“It’s morning and the window is open.”*

How is it calculated? >> Using truth tables.

They tell us how the truths are calculated for the different
molecular propositions.

Consider a proposition p that can take one of two truth values:

**T** (true) , or **F** (false).

**Negation** ***“~”***
|p|~p|
|--|--|
|F|T|
|T|F|

**Conjunction** ***"^"***

| p | q | p^q |
|--|--|--|
|F|F|F|
|F|T|F|
|T|F|F|
|T|T|T|

**Disjunction** ***"v"***
| p | q | pvq |
|--|--|--|
|F|F|F|
|F|T|T|
|T|F|T|
|T|T|T|

### *Practice*
If P = F, Q = F, X = T
#### P AND Q OR X = V
        F AND F OR T = T
#### NOT(Q) OR P AND X = V
        T OR F AND T = T
#### P AND (Q OR X) = V 
        F AND (F OR T) = F
#### NOT(Q) AND P OR Q = V
        T AND F OR F = F
#### (P AND Q) OR X = V 
        (F AND F) OR T = T
#### NOT(Q) AND NOT(P) OR Q = V
        T AND T OR F = T

### *Algorithms*

- Purpose of programming
- Actions, interlocutor and Algorithms
- Writing Algorithms
- Data and Information
- Pseudo Code
- Structure of an algorithm
- Types of Actions
- Constants, Variables, Assignment and Expressions.
- Logical Conditions
- Resolution of a first problem
#### *Purpose of programming*
To resolve computational type problems
Flat tire  example where we follow a series of steps
What level of detail is used to execute instructions
***For some people, solution will be:***
1. Change the tire.

***Others, will understand this:***
1. Raise the car
3. Take out the flat tire
4. Bring the spare
5. Install the spare
6. Put the car back to the ground
7. Put the flat tire in the trunk

But if I’m talking to someone without any expertise (only good
will), maybe I’ll have to be more specific:

***For action 1:***
1. Locate the Jack under the car
2. Bring the Jack
3. Raise the car with the Jack

***For action 4:***
1. Lift the spare tire and put into position
2. Tighten the lug nuts

#### *Actions, interlocutor and Algorithms*
***Algorithm***: It is an ordered sequence of primitive actions
oriented to solve a problem or a certain question.

***Language***: It is the one that we talk with the interlocutor to
describe the algorithms.

#### *Writing Algorithms*
Let's make an algorithm to change a burned light bulb:

1. Set the ladder on place
2. Take out the light bulb
3. Install new light bulb
4. Store the ladder

And if I need more details?

1. Set the ladder on place
2. Climb up ladder
3. Take out light bulb
4. Step down from the ladder
5. Grab new light bulb
6. Climb up ladder
7. Set up new light bulb
8. Step down from the ladder
9. Store ladder

Let’s think about how we think...

1. Set the ladder on place
2. Take out the light bulb
	1. Climb up ladder
	2. Take out light bulb
	3. Step down from the ladder
3. Install new light bulb
	1. Grab new light bulb
	2. Climb up ladder
	3. Set up new light bulb
	4. Step down from the ladder
4. Store the ladder

First we think of it in the most general terms possible.
- With a lot of abstraction

Then we go on to break down each "big" step into a series of
"little” steps

Each large step is known by the term module
- Each one fulfills a well defined function
- Each of them, sometimes, can be done independently of the
other

This is part of modular thinking known as top-down
programming philosophy
- It's really all we have at hand to solve a problem when we do
not know the details
- It is not convenient to start with the details, because we can
get lost!!!

- We start from the most general information because it is easier
for us.
- And we go from the most general to the most specific

It looks easy but it is actually hard
- It requires a lot of practice
- Creativity

Just to think, in our previous exercise, how about electricity?
- If I remove the light bulb and the lights are on, it might be the
last algorithm I write in my whole life.

Knowing this:
- I assume things (that lights are off)
- Or I give explicit instructions to turn off the lights before
removing the light bulb.

Assumptions are facts that are not written but are part of my
solution to the problem.
- They help to define the scope of what we are doing and what
not.
#### *Data and Information*
A data is a symbolic representation of a feature or property of
an entity
- It doesn’t make sense by itself.
- If we process or interpret it, then we have information
- We associate data with something or someone.
(Contextualize)

- In computing, data is represented by a value.
- That is, in essence, that data is a value about something.
#### *Lessons Learned:*

- Application of logic in the real world
- Truth tables