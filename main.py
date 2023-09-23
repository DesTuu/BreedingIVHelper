from tkinter import *
from tkinter import colorchooser, messagebox
import requests
import webbrowser
from breeding import *

var = False
att_or_spa = ""
option_menu_dict = {}
entry_dict = {}
label_dict = {}
text_dict = {}
selected_iv = {}
selected_option = {}
ivs = ("HP", "Att", "Def", "SpAtk", "SpDef", "Speed")

with open('settings.txt', 'r') as f:
    settings_list = f.read().split(", ")

try:
    color_label_background = settings_list[0] if settings_list[0] else 'black'
    color_background = settings_list[1] if settings_list[1] else 'white'
    color_ok = settings_list[2] if settings_list[2] else 'green'
    color_nok = settings_list[3] if settings_list[3] else 'red'
    color_labels = settings_list[4] if settings_list[4] else "#001861"
    color_optionMenu_background = settings_list[5] if settings_list[5] else "white"
    color_optionMenu_fg = settings_list[6] if settings_list[6] else "black"
    tutorial_label = settings_list[7] if str(settings_list[7]) else True
    tutorial_label = False if tutorial_label == 'False' else True
except:
    color_label_background = 'black'
    color_background = 'white'
    color_ok = 'green'
    color_nok = 'red'
    color_labels = "#001861"
    color_optionMenu_background = "white"
    color_optionMenu_fg = "black"
    tutorial_label = True


def option_selected(*args, idx):
    row, column = idx
    selected_option[str(row) + str(column)] = selected_iv[str(row) + str(column)].get()
    try:
        if row == 9:
            # 2x31
            if (column + 2) % 2 == 0 and selected_option[str(row) + str(column + 1)]:
                text_dict[str(row - 2) + str(column)] = selected_option[str(row) + str(column)] + ", " + \
                                                        selected_option[str(row) + str(column + 1)]
                text_dict[str(row - 2) + str(column)] = set(text_dict[str(row - 2) + str(column)].split(", "))
                if len(text_dict[str(row - 2) + str(column)]) == 2:
                    entry_dict[str(row - 2) + str(column)].config(fg=color_ok)
                else:
                    entry_dict[str(row - 2) + str(column)].config(fg=color_nok)
                text_dict[str(row - 2) + str(column)] = ", ".join(text_dict[str(row - 2) + str(column)])
                entry_dict[str(row - 2) + str(column)].config(state=NORMAL)
                entry_dict[str(row - 2) + str(column)].delete(0, END)
                entry_dict[str(row - 2) + str(column)].insert(0, text_dict[str(row - 2) + str(column)])
                entry_dict[str(row - 2) + str(column)].config(state="readonly")
                # 3x31
                if (column + 4) % 4 == 0 and text_dict[str(row - 2) + str(column)] and text_dict[
                    str(row - 2) + str(column + 2)]:
                    text_dict[str(row - 4) + str(column + 1)] = text_dict[str(row - 2) + str(column)] + ", " + \
                                                                text_dict[str(row - 2) + str(column + 2)]
                    text_dict[str(row - 4) + str(column + 1)] = set(
                        text_dict[str(row - 4) + str(column + 1)].split(", "))
                    if len(text_dict[str(row - 4) + str(column + 1)]) == 3:
                        entry_dict[str(row - 4) + str(column + 1)].config(fg=color_ok)
                    else:
                        entry_dict[str(row - 4) + str(column + 1)].config(fg=color_nok)
                    text_dict[str(row - 4) + str(column + 1)] = ", ".join(text_dict[str(row - 4) + str(column + 1)])
                    entry_dict[str(row - 4) + str(column + 1)].config(state=NORMAL)
                    entry_dict[str(row - 4) + str(column + 1)].delete(0, END)
                    entry_dict[str(row - 4) + str(column + 1)].insert(0, text_dict[str(row - 4) + str(column + 1)])
                    entry_dict[str(row - 4) + str(column + 1)].config(state='readonly')
                    # 4x31
                    if (column + 8) % 8 == 0 and text_dict[str(row - 4) + str(column + 1)] and text_dict[
                        str(row - 4) + str(column + 5)]:
                        text_dict[str(row - 6) + str(column + 2)] = text_dict[str(row - 4) + str(column + 1)] + ", " + \
                                                                    text_dict[
                                                                        str(row - 4) + str(column + 5)]
                        text_dict[str(row - 6) + str(column + 2)] = set(
                            text_dict[str(row - 6) + str(column + 2)].split(", "))
                        if len(text_dict[str(row - 6) + str(column + 2)]) == 4:
                            entry_dict[str(row - 6) + str(column + 2)].config(fg=color_ok)
                        else:
                            entry_dict[str(row - 6) + str(column + 2)].config(fg=color_nok)
                        text_dict[str(row - 6) + str(column + 2)] = ", ".join(text_dict[str(row - 6) + str(column + 2)])
                        entry_dict[str(row - 6) + str(column + 2)].config(state=NORMAL)
                        entry_dict[str(row - 6) + str(column + 2)].delete(0, END)
                        entry_dict[str(row - 6) + str(column + 2)].insert(0, text_dict[str(row - 6) + str(column + 2)])
                        entry_dict[str(row - 6) + str(column + 2)].config(state='readonly')
                    elif (column + 8) % 8 == 4 and text_dict[str(row - 4) + str(column - 3)] and text_dict[
                        str(row - 4) + str(column + 1)]:
                        text_dict[str(row - 6) + str(column - 2)] = text_dict[str(row - 4) + str(column - 3)] + ", " + \
                                                                    text_dict[
                                                                        str(row - 4) + str(column + 1)]
                        text_dict[str(row - 6) + str(column - 2)] = set(
                            text_dict[str(row - 6) + str(column - 2)].split(", "))
                        if len(text_dict[str(row - 6) + str(column - 2)]) == 4:
                            entry_dict[str(row - 6) + str(column - 2)].config(fg=color_ok)
                        else:
                            entry_dict[str(row - 6) + str(column - 2)].config(fg=color_nok)
                        text_dict[str(row - 6) + str(column - 2)] = ", ".join(text_dict[str(row - 6) + str(column - 2)])
                        entry_dict[str(row - 6) + str(column - 2)].config(state=NORMAL)
                        entry_dict[str(row - 6) + str(column - 2)].delete(0, END)
                        entry_dict[str(row - 6) + str(column - 2)].insert(0, text_dict[str(row - 6) + str(column - 2)])
                        entry_dict[str(row - 6) + str(column - 2)].config(state='readonly')
                # 3x31
                elif (column + 4) % 4 == 2 and selected_option[str(row) + str(column - 2)] and selected_option[
                    str(row) + str(column - 1)] and selected_option[str(row) + str(column + 1)]:
                    text_dict[str(row - 4) + str(column - 1)] = text_dict[str(row - 2) + str(column - 2)] + ", " + \
                                                                text_dict[str(row - 2) + str(column)]
                    text_dict[str(row - 4) + str(column - 1)] = set(
                        text_dict[str(row - 4) + str(column - 1)].split(", "))
                    if len(text_dict[str(row - 4) + str(column - 1)]) == 3:
                        entry_dict[str(row - 4) + str(column - 1)].config(fg=color_ok)
                    else:
                        entry_dict[str(row - 4) + str(column - 1)].config(fg=color_nok)
                    text_dict[str(row - 4) + str(column - 1)] = ", ".join(text_dict[str(row - 4) + str(column - 1)])
                    entry_dict[str(row - 4) + str(column - 1)].config(state=NORMAL)
                    entry_dict[str(row - 4) + str(column - 1)].delete(0, END)
                    entry_dict[str(row - 4) + str(column - 1)].insert(0, text_dict[str(row - 4) + str(column - 1)])
                    entry_dict[str(row - 4) + str(column - 1)].config(state='readonly')
                    # 4x31
                    if (column + 8) % 8 == 2 and text_dict[str(row - 4) + str(column - 1)] and text_dict[
                        str(row - 4) + str(column + 3)]:
                        text_dict[str(row - 6) + str(column)] = text_dict[str(row - 4) + str(column - 1)] + ", " + \
                                                                text_dict[
                                                                    str(row - 4) + str(column + 3)]
                        text_dict[str(row - 6) + str(column)] = set(
                            text_dict[str(row - 6) + str(column)].split(", "))
                        if len(text_dict[str(row - 6) + str(column)]) == 4:
                            entry_dict[str(row - 6) + str(column)].config(fg=color_ok)
                        else:
                            entry_dict[str(row - 6) + str(column)].config(fg=color_nok)
                        text_dict[str(row - 6) + str(column)] = ", ".join(text_dict[str(row - 6) + str(column)])
                        entry_dict[str(row - 6) + str(column)].config(state=NORMAL)
                        entry_dict[str(row - 6) + str(column)].delete(0, END)
                        entry_dict[str(row - 6) + str(column)].insert(0, text_dict[str(row - 6) + str(column)])
                        entry_dict[str(row - 6) + str(column)].config(state='readonly')
                    elif (column + 8) % 8 == 6 and text_dict[str(row - 4) + str(column - 5)] and text_dict[
                        str(row - 4) + str(column - 1)]:
                        text_dict[str(row - 6) + str(column - 4)] = text_dict[str(row - 4) + str(column - 5)] + ", " + \
                                                                    text_dict[
                                                                        str(row - 4) + str(column - 1)]
                        text_dict[str(row - 6) + str(column - 4)] = set(
                            text_dict[str(row - 6) + str(column - 4)].split(", "))
                        if len(text_dict[str(row - 6) + str(column - 4)]) == 4:
                            entry_dict[str(row - 6) + str(column - 4)].config(fg=color_ok)
                        else:
                            entry_dict[str(row - 6) + str(column - 4)].config(fg=color_nok)
                        text_dict[str(row - 6) + str(column - 4)] = ", ".join(text_dict[str(row - 6) + str(column - 4)])
                        entry_dict[str(row - 6) + str(column - 4)].config(state=NORMAL)
                        entry_dict[str(row - 6) + str(column - 4)].delete(0, END)
                        entry_dict[str(row - 6) + str(column - 4)].insert(0, text_dict[str(row - 6) + str(column - 4)])
                        entry_dict[str(row - 6) + str(column - 4)].config(state='readonly')
            # 2x31
            elif (column + 2) % 2 == 1 and selected_option[str(row) + str(column - 1)]:
                text_dict[str(row - 2) + str(column - 1)] = selected_option[str(row) + str(column)] + ", " + \
                                                            selected_option[str(row) + str(column - 1)]
                text_dict[str(row - 2) + str(column - 1)] = set(text_dict[str(row - 2) + str(column - 1)].split(", "))
                if len(text_dict[str(row - 2) + str(column - 1)]) == 2:
                    entry_dict[str(row - 2) + str(column - 1)].config(fg=color_ok)
                else:
                    entry_dict[str(row - 2) + str(column - 1)].config(fg=color_nok)
                text_dict[str(row - 2) + str(column - 1)] = ", ".join(text_dict[str(row - 2) + str(column - 1)])
                entry_dict[str(row - 2) + str(column - 1)].config(state=NORMAL)
                entry_dict[str(row - 2) + str(column - 1)].delete(0, END)
                entry_dict[str(row - 2) + str(column - 1)].insert(0, text_dict[str(row - 2) + str(column - 1)])
                entry_dict[str(row - 2) + str(column - 1)].config(state="readonly")
                # 3x31
                if (column + 4) % 4 == 1 and text_dict[str(row - 2) + str(column - 1)] and text_dict[
                    str(row - 2) + str(column + 1)]:
                    text_dict[str(row - 4) + str(column)] = text_dict[str(row - 2) + str(column - 1)] + ", " + \
                                                            text_dict[str(row - 2) + str(column + 1)]
                    text_dict[str(row - 4) + str(column)] = set(text_dict[str(row - 4) + str(column)].split(", "))
                    if len(text_dict[str(row - 4) + str(column)]) == 3:
                        entry_dict[str(row - 4) + str(column)].config(fg=color_ok)
                    else:
                        entry_dict[str(row - 4) + str(column)].config(fg=color_nok)
                    text_dict[str(row - 4) + str(column)] = ", ".join(text_dict[str(row - 4) + str(column)])
                    entry_dict[str(row - 4) + str(column)].config(state=NORMAL)
                    entry_dict[str(row - 4) + str(column)].delete(0, END)
                    entry_dict[str(row - 4) + str(column)].insert(0, text_dict[str(row - 4) + str(column)])
                    entry_dict[str(row - 4) + str(column)].config(state="readonly")
                    # 4x31
                    if (column + 8) % 8 == 1 and text_dict[str(row - 4) + str(column)] and text_dict[
                        str(row - 4) + str(column + 4)]:
                        text_dict[str(row - 6) + str(column + 1)] = text_dict[str(row - 4) + str(column)] + ", " + \
                                                                    text_dict[
                                                                        str(row - 4) + str(column + 4)]
                        text_dict[str(row - 6) + str(column + 1)] = set(
                            text_dict[str(row - 6) + str(column + 1)].split(", "))
                        if len(text_dict[str(row - 6) + str(column + 1)]) == 4:
                            entry_dict[str(row - 6) + str(column + 1)].config(fg=color_ok)
                        else:
                            entry_dict[str(row - 6) + str(column + 1)].config(fg=color_nok)
                        text_dict[str(row - 6) + str(column + 1)] = ", ".join(text_dict[str(row - 6) + str(column + 1)])
                        entry_dict[str(row - 6) + str(column + 1)].config(state=NORMAL)
                        entry_dict[str(row - 6) + str(column + 1)].delete(0, END)
                        entry_dict[str(row - 6) + str(column + 1)].insert(0, text_dict[str(row - 6) + str(column + 1)])
                        entry_dict[str(row - 6) + str(column + 1)].config(state='readonly')
                    elif (column + 8) % 8 == 5 and text_dict[str(row - 4) + str(column - 4)] and text_dict[
                        str(row - 4) + str(column)]:
                        text_dict[str(row - 6) + str(column - 3)] = text_dict[str(row - 4) + str(column - 4)] + ", " + \
                                                                    text_dict[
                                                                        str(row - 4) + str(column)]
                        text_dict[str(row - 6) + str(column - 3)] = set(
                            text_dict[str(row - 6) + str(column - 3)].split(", "))
                        if len(text_dict[str(row - 6) + str(column - 3)]) == 4:
                            entry_dict[str(row - 6) + str(column - 3)].config(fg=color_ok)
                        else:
                            entry_dict[str(row - 6) + str(column - 3)].config(fg=color_nok)
                        text_dict[str(row - 6) + str(column - 3)] = ", ".join(text_dict[str(row - 6) + str(column - 3)])
                        entry_dict[str(row - 6) + str(column - 3)].config(state=NORMAL)
                        entry_dict[str(row - 6) + str(column - 3)].delete(0, END)
                        entry_dict[str(row - 6) + str(column - 3)].insert(0, text_dict[str(row - 6) + str(column - 3)])
                        entry_dict[str(row - 6) + str(column - 3)].config(state='readonly')
                # 3x31
                elif (column + 4) % 4 == 3 and text_dict[str(row - 2) + str(column - 3)] and text_dict[
                    str(row - 2) + str(column - 1)]:
                    text_dict[str(row - 4) + str(column - 2)] = text_dict[str(row - 2) + str(column - 3)] + ", " + \
                                                                text_dict[str(row - 2) + str(column - 1)]
                    text_dict[str(row - 4) + str(column - 2)] = set(
                        text_dict[str(row - 4) + str(column - 2)].split(", "))
                    if len(text_dict[str(row - 4) + str(column - 2)]) == 3:
                        entry_dict[str(row - 4) + str(column - 2)].config(fg=color_ok)
                    else:
                        entry_dict[str(row - 4) + str(column - 2)].config(fg=color_nok)
                    text_dict[str(row - 4) + str(column - 2)] = ", ".join(text_dict[str(row - 4) + str(column - 2)])
                    entry_dict[str(row - 4) + str(column - 2)].config(state=NORMAL)
                    entry_dict[str(row - 4) + str(column - 2)].delete(0, END)
                    entry_dict[str(row - 4) + str(column - 2)].insert(0, text_dict[str(row - 4) + str(column - 2)])
                    entry_dict[str(row - 4) + str(column - 2)].config(state="readonly")
                    # 4x31
                    if (column + 8) % 8 == 3 and text_dict[str(row - 4) + str(column - 2)] and text_dict[
                        str(row - 4) + str(column + 2)]:
                        text_dict[str(row - 6) + str(column - 1)] = text_dict[str(row - 4) + str(column - 2)] + ", " + \
                                                                    text_dict[
                                                                        str(row - 4) + str(column + 2)]
                        text_dict[str(row - 6) + str(column - 1)] = set(
                            text_dict[str(row - 6) + str(column - 1)].split(", "))
                        if len(text_dict[str(row - 6) + str(column - 1)]) == 4:
                            entry_dict[str(row - 6) + str(column - 1)].config(fg=color_ok)
                        else:
                            entry_dict[str(row - 6) + str(column - 1)].config(fg=color_nok)
                        text_dict[str(row - 6) + str(column - 1)] = ", ".join(text_dict[str(row - 6) + str(column - 1)])
                        entry_dict[str(row - 6) + str(column - 1)].config(state=NORMAL)
                        entry_dict[str(row - 6) + str(column - 1)].delete(0, END)
                        entry_dict[str(row - 6) + str(column - 1)].insert(0, text_dict[str(row - 6) + str(column - 1)])
                        entry_dict[str(row - 6) + str(column - 1)].config(state='readonly')
                    elif (column + 8) % 8 == 7 and text_dict[str(row - 4) + str(column - 6)] and text_dict[
                        str(row - 4) + str(column - 2)]:
                        text_dict[str(row - 6) + str(column - 5)] = text_dict[str(row - 4) + str(column - 6)] + ", " + \
                                                                    text_dict[
                                                                        str(row - 4) + str(column - 2)]
                        text_dict[str(row - 6) + str(column - 5)] = set(
                            text_dict[str(row - 6) + str(column - 5)].split(", "))
                        if len(text_dict[str(row - 6) + str(column - 5)]) == 4:
                            entry_dict[str(row - 6) + str(column - 5)].config(fg=color_ok)
                        else:
                            entry_dict[str(row - 6) + str(column - 5)].config(fg=color_nok)
                        text_dict[str(row - 6) + str(column - 5)] = ", ".join(text_dict[str(row - 6) + str(column - 5)])
                        entry_dict[str(row - 6) + str(column - 5)].config(state=NORMAL)
                        entry_dict[str(row - 6) + str(column - 5)].delete(0, END)
                        entry_dict[str(row - 6) + str(column - 5)].insert(0, text_dict[str(row - 6) + str(column - 5)])
                        entry_dict[str(row - 6) + str(column - 5)].config(state='readonly')
            # 5x31
            if text_dict[str(3) + str(2)] and text_dict[str(3) + str(10)]:
                text_dict[str(1) + str(1)] = text_dict[str(3) + str(2)] + ", " + text_dict[str(3) + str(10)]
                text_dict[str(1) + str(1)] = set(text_dict[str(1) + str(1)].split(", "))
                if len(text_dict[str(1) + str(1)]) == 5:
                    entry_dict[str(1) + str(1)].config(fg=color_ok)
                else:
                    entry_dict[str(1) + str(1)].config(fg=color_nok)
                text_dict[str(1) + str(1)] = ", ".join(text_dict[str(1) + str(1)])
                entry_dict[str(1) + str(1)].config(state=NORMAL)
                entry_dict[str(1) + str(1)].delete(0, END)
                entry_dict[str(1) + str(1)].insert(0, text_dict[str(1) + str(1)])
                entry_dict[str(1) + str(1)].config(state="readonly")

    except KeyError:
        pass


def create_option_menu(row, column, columnspan, text):
    if row > 8:
        selected_iv[str(row) + str(column)] = StringVar()
        selected_iv[str(row) + str(column)].trace_add("write",
                                                      lambda *args, idx=(row, column): option_selected(idx=idx))
        option_menu_dict[str(row) + str(column)] = OptionMenu(frame, selected_iv[str(row) + str(column)], *ivs)
        option_menu_dict[str(row) + str(column)].config(width=7, relief=RAISED, bd=5, bg=color_optionMenu_background,
                                                        fg=color_optionMenu_fg)
        option_menu_dict[str(row) + str(column)].grid(row=row, column=column, columnspan=columnspan)
    else:
        entry_dict[str(row) + str(column)] = Entry(frame,
                                                   width=int(160 / (row + 3)),
                                                   font=("Arial Black", 10, "bold"),
                                                   fg=color_label_background,
                                                   bg=color_background,
                                                   relief=RAISED,
                                                   bd=5,
                                                   justify='center')
        entry_dict[str(row) + str(column)].config(state="readonly")
        entry_dict[str(row) + str(column)].grid(row=row, column=column, columnspan=columnspan)
        label_dict[str(row) + str(column)] = Label(frame,
                                                   text=f"⬆ Powinno być {text}x31IV ⬆",
                                                   font=("Arial Black", 10, "bold"),
                                                   fg=color_labels,
                                                   bg=color_background)
        label_dict[str(row) + str(column)].grid(row=row + 1, column=column, columnspan=columnspan)


def change_color_label_background():
    global color_label_background
    color = colorchooser.askcolor(title="Wybierz kolor")
    color_label_background = color[1]
    label_question.config(bg=color_label_background)


def change_color_background():
    global color_background
    color = colorchooser.askcolor(title="Wybierz kolor")
    color_background = color[1]
    frame.config(bg=color_background)
    window.config(bg=color_background)
    label_question.config(fg=color_background)
    reset_button.config(bg=color_background)
    for key in label_dict:
        label_dict[key].config(bg=color_background)


def change_color_optionMenus():
    global color_optionMenu_background
    color = colorchooser.askcolor(title="Wybierz kolor")
    color_optionMenu_background = color[1]
    for key in option_menu_dict:
        option_menu_dict[key].config(bg=color_optionMenu_background)


def change_color_ok():
    global color_ok
    if show_warning():
        color = colorchooser.askcolor(title="Wybierz kolor")
        color_ok = color[1]
        delete_all()


def change_color_nok():
    global color_nok
    if show_warning():
        color = colorchooser.askcolor(title="Wybierz kolor")
        color_nok = color[1]
        delete_all()


def change_color_labels():
    global color_labels
    color = colorchooser.askcolor(title="Wybierz kolor")
    color_labels = color[1]
    for key in label_dict:
        label_dict[key].config(fg=color_labels)


def change_color_optionMenus_fg():
    global color_optionMenu_fg
    color = colorchooser.askcolor(title="Wybierz kolor")
    color_optionMenu_fg = color[1]
    for key in option_menu_dict:
        option_menu_dict[key].config(fg=color_optionMenu_fg)


def set_colors_default():
    global color_label_background, color_background, color_ok, color_nok, color_labels, color_optionMenu_background, color_optionMenu_fg
    if show_warning():
        color_label_background = 'black'
        color_background = 'white'
        color_ok = 'green'
        color_nok = 'red'
        color_labels = "#001861"
        color_optionMenu_background = "white"
        color_optionMenu_fg = "black"

        frame.config(bg=color_background)
        window.config(bg=color_background)
        label_question.config(fg=color_background)
        label_question.config(bg=color_label_background)
        reset_button.config(bg=color_background)
        for key in label_dict:
            label_dict[key].config(fg=color_labels)
        for key in label_dict:
            label_dict[key].config(bg=color_background)
        for key in option_menu_dict:
            option_menu_dict[key].config(bg=color_optionMenu_background)
            option_menu_dict[key].config(fg=color_optionMenu_fg)
        delete_all()


def save_settings():
    with open('settings.txt', 'w') as f:
        f.write(
            f"{color_label_background}, {color_background}, {color_ok}, {color_nok}, "
            f"{color_labels}, {color_optionMenu_background}, {color_optionMenu_fg}, {str(tutorial_label)}")


def show_warning():
    return messagebox.askyesno(title="Ostrożnie!",
                               message="""Zmiana kolorów spowoduje usunięcie wpisanych/wybranych wartości!
Czy na pewno chcesz kontynuować?""")


def create_menu():
    menu = Menu(window)
    window.config(menu=menu)

    colorMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Zmień kolory", menu=colorMenu)

    infoMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Wybierz pokemona', menu=infoMenu)

    breedingMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Breedowanie', menu=breedingMenu)

    optionsMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Ustawienia', menu=optionsMenu)

    colorMenu.add_command(label="Napisu \"Powinno być\" (domyślnie: granatowy)", command=change_color_labels)
    colorMenu.add_command(label="Tła informacji (domyślnie: czarny)", command=change_color_label_background)
    colorMenu.add_command(label="Tła (domyślnie: białe)", command=change_color_background)
    colorMenu.add_command(label="Tła przycisków wyboru (domyślnie: biały)", command=change_color_optionMenus)
    colorMenu.add_command(label="Tekstu przycisków wyboru (domyślnie: czarny)", command=change_color_optionMenus_fg)
    colorMenu.add_command(label="Tekstu jeśli OK (domyślnie: zielony)", command=change_color_ok)
    colorMenu.add_command(label="Tekstu jeśli NOK (domyślnie: czerwony)", command=change_color_nok)
    colorMenu.add_separator()
    colorMenu.add_command(label="Przywróć domyślne ustawienia", command=set_colors_default)

    infoMenu.add_command(label='Informacje o pokemonie', command=pokemon)

    breedingMenu.add_command(label='Poradniki', command=breeding)

    optionsMenu.add_command(label='Usuń napis początkowy', command=delete_first_label)
    optionsMenu.add_command(label='Przywróć napis początkowy', command=recover_first_label)


def delete_all():
    for key in selected_iv:
        selected_iv[key].set("")
    for key in entry_dict:
        entry_dict[key].config(state=NORMAL, bg=color_background, fg=color_label_background)
        entry_dict[key].delete(0, END)
        entry_dict[key].config(state="readonly")
        text_dict[key] = ""


def open_urls():
    webbrowser.open(f"https://www.smogon.com/dex/bw/pokemon/{user_input.lower()}")


def submit():
    global photo_id, var, info_label, zoomed_photo_id, link_label, user_input
    if var:
        info_label.destroy()
        link_label.destroy()
    user_input = entry.get()
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_input.lower()}")
        data = response.json()

        abils = []
        tys = []

        for i in data['abilities']:
            ability = i['ability']['name'].replace("-", " ")
            hidden = i['is_hidden']
            if hidden:
                abils.append(f"{ability} - Hidden Ability")
            else:
                abils.append(ability)

        abils = "\n".join(abils).title()

        for i in data['types']:
            type = i['type']['name']
            tys.append(type)

        tys = " | ".join(tys).title()

        id = data['id']
        image_path = f"downloaded_images/{id}.png"
        photo_id = PhotoImage(file=image_path)
        zoomed_photo_id = photo_id.zoom(2, 2)
        var = True

        hp = dict(data['stats'][0])['base_stat']
        att = dict(data['stats'][1])['base_stat']
        deff = dict(data['stats'][2])['base_stat']
        spatt = dict(data['stats'][3])['base_stat']
        spdef = dict(data['stats'][4])['base_stat']
        speed = dict(data['stats'][5])['base_stat']

        if att > spatt:
            att_or_spa = f"{user_input.title()} ma więcej ataku niż specjal ataku, więc jeśli chcesz ofensywnie zrobić" \
                         f" tego pokemona to polecam zrobic IV oraz EV w atak"
        elif att < spatt:
            att_or_spa = f"{user_input.title()} ma więcej specjal ataku niż ataku, więc jeśli chcesz ofensywnie zrobić" \
                         f" tego pokemona to polecam zrobić IV oraz EV w specjal atak"
        elif att == spatt:
            if user_input.lower() == "ditto":
                att_or_spa = f"{user_input.title()} jest najsilniejszy jeśli złapiesz takiego z 31IV w HP " \
                             f"oraz wbijesz wszystko w HP"
            else:
                att_or_spa = f"{user_input.title()} ma tyle samo ataku co specjal ataku, więc jeśli chcesz zrobić go " \
                             f"ofensywnie to możesz wybrać czy wolisz go zrobić pod atak lub specjal atak"

        info_label = Label(pokemon_window, font=("Consolas", 12), image=zoomed_photo_id, compound='top',
                           text=f"""Informacje o pokemonie {user_input.title()}
Typy: {tys}

Umiejętnosći
{abils}

Bazowe statystyki
HP: {hp}
Atk: {att}
Def: {deff}
Sp. Atk: {spatt}
Sp. Def: {spdef}
Speed: {speed}

Jak breedować/zrobić tego pokemona?
{att_or_spa}

Ale lepiej upewnij się w grze w zakładce PvP/PvP Statistics oraz na stronie""")
        info_label.pack()
        link_label = Label(pokemon_window, font=("Consolas", 12), cursor="hand2", fg="blue",
                           text=f"""https://www.smogon.com/dex/bw/pokemon/{user_input.lower()}""")
        link_label.pack()
        link_label.bind("<Button-1>", lambda e: open_urls())
    except requests.exceptions.JSONDecodeError as e:
        messagebox.showerror(title="Error 404",
                             message="""Nie znaleziono takiego pokemona, nieprawidłowa nazwa pokemona""",
                             parent=pokemon_window)


def pokemon():
    global entry, pokemon_window
    pokemon_window = Toplevel()
    pokemon_window.state("zoomed")
    label = Label(pokemon_window, text="Napisz nazwę pokemona", font=("Consolas", 12))
    label.pack()
    entry = Entry(pokemon_window, font=("Consolas", 12))
    entry.pack()
    button = Button(pokemon_window, text="Wyszukaj", command=submit, font=("Consolas", 12))
    button.pack()

def delete_first_label():
    global tutorial_label
    label_question.destroy()
    tutorial_label = False

def recover_first_label():
    global tutorial_label
    tutorial_label = True
    messagebox.showinfo(title="Informacja", message="Napis pojawi się po ponownym włączeniu programu! :)")

if __name__ == "__main__":
    window = Tk()
    window.state('zoomed')
    window.title("IV Helper")
    window.config(bg=color_background)

    create_menu()

    frame = Frame(window, bg=color_background)
    frame.pack()

    if tutorial_label:
        label_question = Label(frame,
                               font=("Arial Black", 20, "bold"),
                               fg=color_background,
                               bg=color_label_background,
                               text="""Klikając na pustą budkę na dole wybierasz statystykę, w której masz 1x31 w IV.
        Wyświetli na zielono = OK, Wyświetli na czerwono = NOK.
        Aplikacja uwzględnia tylko i wyłącznie używanie braców na każdym poku.
        Nie bierze pod uwagę breedowania natury, która powinna być dodawana na samym końcu.
        Nie bierze pod uwagę również płci.
        By zrobić 5x31 poka z naturą należy zrobić pierw 5x31 bez natury, potem 4x31 bez natury itd.
        Wyjątkiem jest jeśli wyjdzie odpowiednia natura przy breedzie minimum 3x31 IV""")

        label_question.grid(pady=30, row=0, column=0, columnspan=18)

    create_option_menu(1, 1, 14, 5)
    for i in range(2):
        create_option_menu(3, (i * 8) + 2, 4, 4)
    for i in range(4):
        create_option_menu(5, (i * 4) + 1, 2, 3)
    for i in range(8):
        create_option_menu(7, i * 2, 2, 2)
    for i in range(16):
        create_option_menu(9, i, 1, 1)

    reset_button = Button(frame, text="Usuń wszystko", width=15, height=5, command=delete_all, relief=RAISED, bd=5,
                          font=("Arial Black", 10, "bold"), bg='white')
    reset_button.grid(row=11, column=7, columnspan=2)

    window.mainloop()

    save_settings()
