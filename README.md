# 🏏 Hand Cricket Simulator (Python)

A simple **command-line Hand Cricket game built with Python** where the user plays against the computer in a short cricket match.

The game follows a **2-wicket, 12-ball format** where the player bats first and then bowls against the computer. The winner is decided based on the final scores.

---

## 🎮 Game Rules

* The match consists of **12 balls per innings**
* Each side has **2 wickets**
* You must enter numbers **between 1 and 6**
* If your number matches the computer's number → **OUT**
* If numbers are different → runs are added

Example:

```
You choose: 4
Computer chooses: 4
OUT!
```

```
You choose: 5
Computer chooses: 2
You score 5 runs
```

---

## 🧠 Game Flow

1. **User bats first**
2. Score runs until:

   * 2 wickets fall, or
   * 12 balls are completed
3. **Computer bats second**
4. Final scores are compared to decide the winner.

---

## ⚙️ Technologies Used

* **Python 3**
* `random` module

---

## 📂 Project Structure

```
hand-cricket-python
│
├── main1.py
└── README.md
```

---

## ▶️ How to Run the Game

1. Clone the repository

```
git clone https://github.com/DarshJaipuriae/hand-cricket-python.git
```

2. Navigate to the project folder

```
cd hand-cricket-python
```

3. Run the program

```
python main1.py
```

---

## 💡 Features

* Interactive command-line gameplay
* Randomized computer decisions
* Score and wicket tracking
* Input validation for numbers between **1–6**

---

## 🚀 Future Improvements

* Toss system
* Multiple overs
* Difficulty levels
* Scoreboard display
* GUI version using **Tkinter or Pygame**

---

## 👨‍💻 Author

Created by **Darsh**
Python Project
