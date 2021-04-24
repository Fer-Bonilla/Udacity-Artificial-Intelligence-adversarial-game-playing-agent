# Adversarial game playing agent
 Third project from the Udacity's Artificial Intelligence Nanodegree build an Adversarial Game Playing Agent

Project sections:

- Problem understanding
- Project structure
- Running experiments
- Results report

## Problem understanding

Experiment with adversarial search techniques by building an agent to play knights Isolation. Unlike the examples in lecture where the players control tokens that move like chess queens, this version of Isolation gives each agent control over a single token that moves in L-shaped movements--like a knight in chess.


## Project structure

The project structure is based on the Udacity's project template:

```
+ aimacode: aima code library + logic.py
                              + planning.py
                              + search.py
                              + search.pyc
                              + utils.py          
+ tests                       + test_my_planning_graph.py:  Test cases for my_planning_graph implementation
+ _utils.py                                                 Utility functions used
+ air_cargo_problems.py:                                    Contains the cargo problem scenarios 
+ layers.py                                                 Layers implementation
+ my_panning_graph.py:                                      Planning implementation 
+ run_search.py:                                            Main script to run the simulation          
```

## Running the experiments

To run the experiments run the `run_search.py` script. The script can be executed manually or in batch mode:

  - Run the search experiment manually (you will be prompted to select problems & search algorithms)
```
$ python run_search.py -m
```

```

  - Running all the experiments
```
$ python run_search.py -p 1 2 3 4 -s 1 2 3 4 5 6 7 8 9 10 11
```

## Results report


[Results report document](https://github.com/Fer-Bonilla/Udacity-Artificial-Intelligence-forward-planning-agent/blob/main/report.pdf)


## Author 
Fernando Bonilla [linkedin](https://www.linkedin.com/in/fer-bonilla/)
