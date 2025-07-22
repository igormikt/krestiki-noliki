import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x400")

current_player = "X"
player_symbol = "X"
buttons = []
choice_made = False


def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False


def check_draw():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                return False
    return True


def reset_game():
    global current_player, buttons
    current_player = player_symbol
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j].config(state=tk.NORMAL)


def on_click(row, col):
    global current_player

    if buttons[row][col]['text'] != "" or not choice_made:
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(state=tk.DISABLED)
        return

    if check_draw():
        messagebox.showinfo("Игра окончена", "Ничья!")
        return

    current_player = "O" if current_player == "X" else "X"


def choose_symbol(symbol):
    global player_symbol, current_player, choice_made
    player_symbol = symbol
    current_player = symbol
    choice_made = True
    choice_frame.pack_forget()
    game_frame.pack(pady=10)


choice_frame = tk.Frame(window)
choice_frame.pack(pady=20)

tk.Label(choice_frame, text="Выберите символ:", font=("Arial", 12)).pack()

btn_frame = tk.Frame(choice_frame)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="X", font=("Arial", 14), width=3,
          command=lambda: choose_symbol("X")).pack(side=tk.LEFT, padx=10)
tk.Button(btn_frame, text="O", font=("Arial", 14), width=3,
          command=lambda: choose_symbol("O")).pack(side=tk.LEFT, padx=10)

game_frame = tk.Frame(window)

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(game_frame, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

reset_btn = tk.Button(window, text="Сбросить игру", font=("Arial", 12),
                      command=reset_game)
reset_btn.pack(pady=15)

window.mainloop()