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

To run the experiments, execute the `run_match.py` python script: 

  - Run the search experiment manually (you will be prompted to select problems & search algorithms)
  ```
  $ python run_match.py -r 50 -o GREEDY -t 150
  ```

Can run experiment with different parameters values:

  ```
  •	Time limit: 100 y 150 ms
  •	Opponent model:  GREEDY, MINIMAX, SELF, RANDOM
  •	Depth: 3, 5, 7 (Parameter DEFAULT_DEPTH inside my_custom_player.py)
  •	Matches: 100 (50 rounds)
  ```

To facilitate the execution was created a shell script named experiments.sh that executes these calls:
  ```
  python run_match.py -r 50 -o GREEDY -t 100
  python run_match.py -r 50 -o MINIMAX -t 100
  python run_match.py -r 50 -o SELF -t 100
  python run_match.py -r 50 -o RANDOM -t 100
  python run_match.py -r 50 -o GREEDY -t 150
  python run_match.py -r 50 -o MINIMAX -t 150
  python run_match.py -r 50 -o SELF -t 150
  python run_match.py -r 50 -o RANDOM -t 150
  ```

It's necessary assign the right permits to execute the script: 
  ```
  chmod u+x experiments.sh
  ```

## Results report


[Results report document](https://github.com/Fer-Bonilla/Udacity-Artificial-Intelligence-forward-planning-agent/blob/main/report.pdf)


## Author 
Fernando Bonilla [linkedin](https://www.linkedin.com/in/fer-bonilla/)
