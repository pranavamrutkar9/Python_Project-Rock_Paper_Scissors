# 🪨 Rock Paper Scissors – Python Terminal Game

A classic game of Rock, Paper, Scissors — now playable in your terminal!  

A beginner-friendly, terminal-based Rock-Paper-Scissors game built in Python. It uses simple logic, user input validation, and random computer moves to simulate one of the most classic games ever — all in under 50 lines of code!

This simple Python project uses basic input handling and random number generation to create an interactive and fun experience for beginners and Python enthusiasts.

---

## 🎮 Gameplay Overview

- You play against the computer.
- Choose between Rock (`r`), Paper (`p`), or Scissors (`s`).
- The computer randomly selects its move.
- The game announces the winner based on traditional rules.

---

## 🧠 How It Works

- Your input is mapped using a dictionary (`youDict`) to a numerical value.
- The computer randomly selects a number between 0 and 2.
- The winner is determined using conditional logic based on standard RPS rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
