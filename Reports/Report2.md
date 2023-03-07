# Regular Grammar Laboratory No.II
****
## Course: Formal Languages & Finite Automata <br /> Author: Ion Vasluian

## Objectives: 
* Understand what an automaton is and what it can be used for.
* Continuing the work in the same repository and the same project, the following need to be added: 

    a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

    b. For this you can use the variant from the previous lab.

* According to the variant number (30), get the finite automaton definition and do the following tasks:

    a. Implement conversion of a finite automaton to a regular grammar.

    b. Determine whether your FA is deterministic or non-deterministic.

    c. Implement some functionality that would convert an NDFA to a DFA.

    d. Represent the finite automaton graphically (Optional, and can be considered as a bonus point):

    * You can use external libraries, tools or APIs to generate the figures/diagrams.
        
    * Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.
        
        
## Implementation description:
  The implementation, as the previous lab, was done in python. We have the Class NFA, with its init function with the basic grammar needed. After that we have the function get_transitions for making the connections between all the states.
  
  ![image](https://user-images.githubusercontent.com/79792299/223564984-a5a4cd7e-7a45-4fe0-b8bd-b95c385e042c.png)
  
  After that we have the methods/functions init_transformation and update_(states/transitions/final_states) that we make use of in transform_to_dfa. The basic work of it is to check every single state and convert it to a dfa state by changing and adding new singular states, as it should be in dfa
  
  
 ![image](https://user-images.githubusercontent.com/79792299/223565821-d7c68348-0015-4b3b-94b8-c7b8eb5107b9.png)


 ![image](https://user-images.githubusercontent.com/79792299/223565912-2b0ff797-f6f6-4bad-b0eb-316e4a3cbd2c.png)
  
  
 We use graphviz to visualize the final product as a graph, and besides that we create a table to visualize all the nodes and connections.
 
 ![image](https://user-images.githubusercontent.com/79792299/223566216-5dc85ed4-9f4c-46f4-a148-71367c7bbb1e.png)
  
  
  ****
  Now, it's time to check if everything is working properly.
  
  ![image](https://user-images.githubusercontent.com/79792299/223566502-8998044d-af9a-4b9c-ba09-e1833e860392.png)
  
  As we can see, everything works fine. As for the graph, here it is:
  
  ![image](https://user-images.githubusercontent.com/79792299/223566647-672ea0ae-5a45-433b-bc30-a68f0036cb81.png)
  
  The graph gets exported as a pdf file. But as we can see, it didn't make all the connections. That's because the graph is reduced/minimized, so that in case of q0q2, we get back to one of the previous cases that were already shown on the graph.
  
  
  
  
  ## Refferences
  
  * google.com
  * youtube.com (better understanding of how to minimize and for dfa graphs)
  * stackoverflow (finding a program that would make a graph for the dfa)
  
  
