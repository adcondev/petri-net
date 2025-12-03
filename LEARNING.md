# Petri Net Simulator - Learning & Technical Summary

## Project Overview
This project is a Python-based implementation of a **Petri Net simulator** that uses matrix algebra to model and execute discrete event systems. The core objective was to translate the mathematical formalism of Petri Nets (places, transitions, tokens) into an executable program that allows for interactive simulation of state changes.

The system represents the Petri Net structure using **Pre-incidence** and **Post-incidence matrices**, enabling efficient calculation of state transitions and enabled conditions using vector operations.

## Tech Stack and Key Technologies
- **Language:** Python 3.x
- **Core Libraries:** 
  - `numpy`: Used for high-performance matrix and vector operations to represent the net's state and transition logic.
- **Concepts:** Discrete Event Simulation, Matrix Algebra, State Machines.

## Notable Libraries
- **NumPy (`numpy`):**
  - **Purpose:** Handled the underlying data structures for the Petri Net (Marking vector, Pre/Post matrices).
  - **Problem Solved:** Replaced complex nested loops with efficient element-wise array operations for checking enabled transitions (`M >= Pre`) and updating the state (`M' = M - Pre + Post`).

## Major Achievements and Skills Demonstrated
- **Mathematical Modeling to Code:** Successfully translated the formal mathematical definition of a Petri Net (tuple $(P, T, Pre, Post, M_0)$) into a working Python class structure.
- **Matrix-Based State Logic:** Implemented the state equation logic using NumPy arrays, optimizing the calculation of the next state based on the firing vector.
- **Interactive Simulation Loop:** Designed a CLI-based simulation loop that dynamically identifies enabled transitions and prevents invalid operations (blocking).
- **Efficient State Management:** Utilized Python's `__slots__` to optimize memory usage for the `MatrixPetriNet` class instances.

## Skills Gained/Reinforced
- **Computational Linear Algebra:** Applied matrix operations to solve state transition problems in computer science.
- **Python Class Design:** Reinforced object-oriented programming principles, specifically encapsulation of state and behavior in simulation models.
- **Algorithm Implementation:** Gained experience in implementing the "firing rule" algorithm for Petri Nets.
- **NumPy Proficiency:** Deepened understanding of NumPy's broadcasting and boolean indexing for efficient data manipulation.
