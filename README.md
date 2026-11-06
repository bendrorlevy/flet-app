# Rock Paper Scissors

A simple Rock Paper Scissors game I made with Flet (a Python framework for making apps).

You pick rock, paper or scissors and the computer picks one randomly. If you win the background turns green, if you lose it turns red, and if it's a tie it goes back to white. There's a score counter for you and for the computer.

## Features

- 3 buttons for rock, paper and scissors
- The computer picks a random move every round
- Score counters for both you and the computer
- A message that shows what each side picked and who won
- Background color changes depending on if you won or lost
- A few hidden easter eggs

## Dependencies

- Python 3.10+
- Flet

The game also uses the random library

## How to run

Clone the repo:
```
git clone https://github.com/bendrorlevy/flet-app.git
cd flet-app
```

Make a virtual environment and activate it (Windows):
```
python -m venv .venv
.venv\Scripts\Activate.ps1
```
(On Mac/Linux use `python3 -m venv .venv` and then `source .venv/bin/activate`)

Install Flet:
```
pip install flet
```

Run it:
```
python src/main.py
```

## Sources

- Flet docs: https://docs.flet.dev
- Flet button docs: https://docs.flet.dev/controls/button

## Easter eggs

- There's an invisible button above the 'P'. If you click it you get infinite points.
- If you hold down any of the buttons instead of clicking it, it shows you what the computer is going to pick next.
- Every round there's a 1% chance the computer plays dynamite, which beats everything you can choose.
- If you win more than 3 times in a row the background turns gold until you lose.