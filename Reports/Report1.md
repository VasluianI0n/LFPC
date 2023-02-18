# Regular Grammar Laboratory No.I
****
## Course: Formal Languages & Finite Automata <br /> Author: Ion Vasluian

## Objectives: 
* Understand what a language is and what it needs to have in order to be considered a formal one
* Provide the initial setup for the evolving project that you will work on during this semester. I said project because usually at lab works, I encourage/impose students to treat all the labs like stages of development of a whole project. Basically you need to do the following:

    a. Create a local && remote repository of a VCS hosting service

    b. Choose a programming language, favorably one that supports all the main paradigms

    c. Create a separate folder where you will be keeping the report. This semester I wish I won't see reports alongside source code files
* According to the variant number (30), get the grammar definition and do the following tasks:

    a. Implement a type/class for the grammar;

    b. Add one function that would generate 5 valid strings from the language expressed by the given grammar;

    c. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;

    d. For the Finite Automaton, add a method that checks if an input string can be obtained via the state transition from it;
## Implementation description:
  I chose to work with python, since it has a lot of classes and can compute some operations faster than other languages. First of all we had to make a grammar class with all of its components (Vn,Vt,P,S). We also represented the set of productions from there in tuples, since it is needed for the Finite Automaton to work properly.
  
  
  
  ![image](https://user-images.githubusercontent.com/79792299/219880206-9ec9f879-ae30-49c3-9adc-743e14cb057a.png)
  
  After that we have the method/function *getGeneratedString*, to get a String from the specific Grammar and rules. I made it through recursion, so that everytime the cycle is at 1, it ends with a letter and cannot continue further, or if it's **S** and the number of recursion is set to 1, then by our grammar rules it would be the shortest possible string, which is **ac** .
  
  ![image](https://user-images.githubusercontent.com/79792299/219880512-a2068a53-ee4d-45ae-82c7-7a8be8f166ba.png)
  
  
  If the number of recursions is more than 1 then if we have more choices of recursion, we have our randomizer which chooses either 1 or 0, and by that he chooses which recursion to go to. In the recursion, we use the letter given by our grammar rules + the function recalled with the number of iterations *-1* and the new root.
  
  
  ![image](https://user-images.githubusercontent.com/79792299/219880624-35d95d33-6829-42a3-b1d9-bd4c2ba61755.png)
  ****
  Next we have the function that changes our Grammar to Finite Automata.
  First we change the S, A, ... to q1, q2,.... just for the convenience of it. After that we convert our set of productions to a dictionary hash map, after which we append the values to the dictionary.
  
  
  ![image](https://user-images.githubusercontent.com/79792299/219881062-a85edbec-31d7-4733-b678-8c748850846d.png)
  
  ****
  
  Now for the Automaton class, we have the function of setting the Adjacency matrix, and of checking if the string belongs to the language, where we use the adjacency matrix, and go through the nodes till we reach the end of it. If it doesn't match at a specific point, then it returns false, else in the end will return true.
  
  ![image](https://user-images.githubusercontent.com/79792299/219881301-0f1fa2aa-1c80-4991-81ee-a44db0d551ff.png)
  
  ****
  
  Next for the checking part we do a class of grammar and a class of automaton, and first of all check if the matrix was done correctly. After that we assign the adjacency matrix from the Grammar to the Automata and after that we give the 5 valid strings and for each of them we check if it really is part of the grammar just to be sure. And in the end we have a string that for sure isn't a part of the grammar, and it returns false just as it should be.
  
  ![image](https://user-images.githubusercontent.com/79792299/219881520-86d65d08-f226-47ad-b957-b98e6bcd3e54.png)
  
  
  ## Conclusion
  
    I tried many methods to check if the string is valid without using tuples or anything, but it was pretty hard when coming to check the characters that are used again like "aaabba" would give me a value of 4 for both a's instead of 3 and 1, which was a big problem for me and had to come with other solutions. I still have to see for what will I personally need it in the future, but I am pretty sure it will have a usage.
