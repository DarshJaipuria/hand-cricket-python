# Python Terminal Cricket Game 🏏

A simple, fun, command-line based cricket game built in Python where you play against the computer. This game is inspired by the classic "Hand Cricket" game.

## Features ✨
- **Player vs Computer:** Enjoy a complete match featuring both batting and bowling innings.
- **Score Tracking:** Real-time updates of scores, wickets, and balls bowled.
- **Innings Limits:** Each innings is limited to 2 wickets or 12 balls (2 overs), ensuring quick and exciting matches.
- **Match Results:** Automatically calculates and displays the final match result (Win, Loss, or Draw).

## Game Rules 📜
1. **Valid Inputs:** You must enter a number between **1 and 6**.
2. **Batting:**
   - You enter a number, and the computer randomly chooses a number.
   - If the numbers **match**, you are **OUT**.
   - If the numbers **differ**, your chosen number is added to your **score**.
3. **Bowling:**
   - You enter a number (to bowl), and the computer randomly chooses a number (to bat).
   - If the numbers **match**, the computer is **OUT**.
   - If the numbers **differ**, the computer's chosen number is added to its **score**.
4. **End of Innings:** An innings ends when 2 wickets fall or 12 balls are bowled.
5. **Winning:** The player with the highest score at the end of both innings wins!

## Prerequisites 🛠️
To run this game, you need to have Python installed on your system.
- Python 3.x

## How to Run 🚀
1. Clone this repository or download the `main1.py` file to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the following command:
   ```bash
   python main1.py
   ```

## How to Play 🎮
1. Start the game by running the script.
2. You will bat first. Enter a number between 1 and 6 when prompted.
3. After your innings ends, you will switch to bowling.
4. Bowl by entering a number between 1 and 6.
5. After the computer's innings ends, the final result will be displayed.

## License 📄
This project is open-source and free to use.
