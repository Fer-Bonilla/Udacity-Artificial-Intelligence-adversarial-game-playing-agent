# Adversarial game playing agent
 Third project from the Udacity's Artificial Intelligence Nanodegree build an Adversarial Game Playing Agent

Project sections:

- Problem understanding
- Project structure
- Running experiments
- Results report

## Problem understanding

Planning is an important topic in AI because intelligent agents are expected to automatically plan their own actions in uncertain domains. Planning and scheduling systems are commonly used in automation and logistics operations, robotics and self-driving cars, and for aerospace applications like the Hubble telescope and NASA Mars rovers. This project development combine symbolic logic and classical search to implement an agent that performs progression search to solve planning problems.


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

  - You can also run specific problems & search algorithms - e.g., to run breadth first search and UCS on problems 1 and 2:
```
$ python run_search.py -p 1 2 -s 1 2
```

  - Running all the experiments
```
$ python run_search.py -p 1 2 3 4 -s 1 2 3 4 5 6 7 8 9 10 11
```

## Results report


[Results report document](https://github.com/Fer-Bonilla/Udacity-Artificial-Intelligence-forward-planning-agent/blob/main/report.pdf)


## Author 
Fernando Bonilla [linkedin](https://www.linkedin.com/in/fer-bonilla/)
