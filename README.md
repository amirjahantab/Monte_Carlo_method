Monte Carlo method is a statistical technique that uses random sampling and probability to solve complex problems or estimate unknown quantities. It is named after the famous Monte Carlo Casino in Monaco, known for its games of chance. In the context of the code you provided, the Monte Carlo method is used to simulate a gambling scenario and calculate the probability of winning and the average number of bets required to reach a goal.

Here's a README.md file for publishing on GitHub:

# Gambler Problem using Monte Carlo Method

This repository contains a Python script that solves the Gambler Problem using the Monte Carlo method.

## Problem Description

The Gambler Problem is a classic probability problem that simulates a gambling scenario. The goal of the gambler is to reach a certain amount of money (the goal) starting from an initial stake. The gambler can make bets, and each bet has an equal chance of winning or losing. The game continues until the gambler either reaches the goal or runs out of money.

## Monte Carlo Method

The Monte Carlo method is a statistical technique that uses random sampling to estimate unknown quantities or solve complex problems. In this script, the Monte Carlo method is used to simulate multiple trials of the gambling scenario. Each trial starts with the initial stake, and bets are made until the goal is reached or the money is depleted. By running a large number of trials, we can estimate the probability of winning and the average number of bets required to reach the goal.

## Usage

To run the script, follow these steps:

1. Make sure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using the following command:

   ```
   python gambler.py <stake> <goal> <trials>
   ```

   Replace `<stake>` with the initial amount of money, `<goal>` with the desired amount to reach, and `<trials>` with the number of trials to simulate.

## Results

After running the script, it will output the following results:

- The estimated probability of reaching the goal (winning percentage).
- The average number of bets required to reach the goal.

These results provide insights into the expected outcomes of the gambling scenario using the Monte Carlo method.
