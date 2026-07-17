# 🎯 Monty Hall Simulation with Streamlit

A Python project that simulates the famous **Monty Hall Problem** and visualizes the results using **Streamlit**. This project demonstrates why switching doors statistically gives a higher probability of winning.

---

## 📖 About the Project

This project is a simulation of the classic **Monty Hall Problem**, one of the most famous probability puzzles in mathematics.

The simulation compares two different strategies:

- 🚪 Staying with the original door
- 🔄 Switching to the remaining unopened door

By running thousands of simulations, the application demonstrates that switching doors significantly increases the probability of winning.

---

## ❓ The Monty Hall Problem

Imagine a game with three doors:

- Behind one door is a 🚗 Car (Prize)
- Behind the other two doors are 🐐 Goats

The player chooses one door.

Then the host, who knows where the car is, opens one of the remaining doors that contains a goat.

The player now has two options:

- Stay with the original choice.
- Switch to the other unopened door.

Although many people think both choices have a 50% chance, mathematics proves that switching gives approximately a **66.7%** chance of winning.

---

## 🚀 Features

- Monte Carlo simulation
- Streamlit interactive interface
- Live probability visualization
- Compare switching and staying strategies
- Adjustable number of simulations

---

## 📂 Project Structure

```
.
├── app.py
├── monty_hall.py
├── images.png
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/monty-hall-simulation.git
cd monty-hall-simulation
```

Install Streamlit:

```bash
pip install streamlit
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 🧠 How the Code Works

### monty_hall.py

This file contains the simulation logic.

It performs the following steps:

1. Randomly places the car behind one of three doors.
2. Randomly selects the player's initial choice.
3. The host reveals one goat door.
4. Depending on the selected strategy:
   - Stay with the original door.
   - Switch to the remaining unopened door.
5. Returns whether the player wins.

The `simulate_games()` function repeats the experiment multiple times and counts the wins for each strategy.

---

### app.py

This file creates the graphical interface using Streamlit.

It:

- Displays the project image.
- Allows the user to choose the number of simulations.
- Runs simulations one by one.
- Updates two live charts showing the winning percentages.
- Makes it easy to observe how probabilities converge as more games are played.

---

## 📊 Expected Results

After a large number of simulations, the results should approach:

| Strategy | Win Rate |
|----------|---------:|
| Stay | ≈ 33% |
| Switch | ≈ 67% |

These results match the mathematical proof of the Monty Hall Problem.

---

## 🛠 Technologies Used

- Python
- Streamlit
- Random
- Type Hints

---

## 📚 Concepts Demonstrated

- Probability
- Monte Carlo Simulation
- Random Sampling
- Data Visualization
- Python Programming
- Interactive Applications

---

## 🎓 Educational Purpose

This project is intended for learning probability concepts and practicing Python programming with interactive visualization.

---

## 📄 License

This project is open-source and intended for educational purposes.

Feel free to use, modify, and improve it.

---

⭐ If you like this project, consider giving it a **Star** on GitHub!
