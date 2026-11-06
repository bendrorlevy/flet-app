import flet as ft
import random

def main(page: ft.Page):
    page.title = "Rock Paper Scissors"
    page.bgcolor = "#FFFFFF"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    moves = ["Rock", "Paper", "Scissors"]
    beats = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
    score = {"player": 0, "computer": 0, "streak": 0}

    next_pick = {"computer": random.choice(moves)}

    player_text = ft.Text("You: 0", size=46, weight=ft.FontWeight.BOLD)
    computer_text = ft.Text("Computer: 0", size=46, weight=ft.FontWeight.BOLD)
    result_text = ft.Text("Pick one!", size=46, weight=ft.FontWeight.BOLD)

    def play(_):
        player = _.control.data
        computer = next_pick["computer"]
        next_pick["computer"] = random.choice(moves)

        ##Easter egg: 1% chance the computer plays Dynamite and always wins (the round)
        if random.random() < 0.01:
            score["computer"] += 1
            score["streak"] = 0
            page.bgcolor = "#F44336"
            result_text.value = "The computer played DYNAMITE 💥 You lose!"

        elif player == computer:
            score["streak"] = 0
            page.bgcolor = "#FFFFFF"
            result_text.value = f"You both chose {player}. It's a tie!"

        elif beats[player] == computer:
            score["player"] += 1
            score["streak"] += 1

            ##Easter egg: 3 wins in a row turns the background gold
            if score["streak"] >= 3:
                page.bgcolor = "#FFD700"
                result_text.value = f"You're ON FIRE 🔥! {score['streak']} wins in a row!"

            else:
                page.bgcolor = "#4CAF50"
                result_text.value = f"{player} beats {computer}. You win!"

        else:
            score["computer"] += 1
            score["streak"] = 0
            page.bgcolor = "#F44336"
            result_text.value = f"{computer} beats {player}. You lose!"

        show_scores()
        page.update()

    def show_scores():
        if score["player"] == float("inf"):
            player_text.value = "You: ∞"

        else:
            player_text.value = f"You: {score['player']}"
        computer_text.value = f"Computer: {score['computer']}"

    def cheat(_):
        page.bgcolor = "#E8E809"
        result_text.value = "Cheat mode activated! You win!"
        score["player"] = float("inf")
        show_scores()
        page.update()

    ##Easter egg: if you long press any button you will see the computer's next move
    def peek(_):
        result_text.value = f"🔮 The computer is going to pick {next_pick['computer']}..."
        page.update()

    def make_button(move):
        return ft.Button(
            content=ft.Text(move, size=28),
            data=move,
            width=200,
            height=80,
            on_click=play,
            on_long_press=peek,
        )

    secret_button = ft.Container(
        width=50,
        height=50,
        bgcolor=ft.Colors.TRANSPARENT,
        on_click=cheat,
    )

    page.add(
        ft.Row(
            [player_text, secret_button, computer_text],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),

        result_text,

        ft.Row(
            [make_button("Rock"), make_button("Paper"), make_button("Scissors")],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=30,
        ),
    )

ft.run(main)