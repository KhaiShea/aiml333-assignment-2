# AIML333 Assignment 2 - Dispatching Rule Scheduler

Author: Khai Dye-Brinkman
Student ID: 300550065

This program implements FCFS, SPT, and EDD scheduling rules for a single-machine problem with five jobs.

## How to Run the Program

1. Make sure Python 3 is installed on your ECS machine.
2. Unzip `program.zip` and open a terminal in the extracted directory.
3. Run the program using the following command:

   python3 dispatching_rules.py

The program will output:
- The schedule for each rule (FCFS, SPT, EDD)
- Start and finish times
- Flowtime and tardiness for each job
- Average flowtime and average tardiness for each rule

## Program Status

✅ The program runs correctly and produces valid output for all three rules.

## Sample Output

The program prints something like this for each rule:

--- FCFS Schedule ---
A: Start=0, Finish=11, Flowtime=11, Tardiness=0
...
Average Flowtime: 51.6
Average Tardiness: 24.2