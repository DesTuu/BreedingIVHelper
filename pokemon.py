from tkinter import *
import requests
import webbrowser
from tkinter import messagebox

var = False
att_or_spa = ""


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
