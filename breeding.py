from tkinter import *
import webbrowser

link_image = "https://cdn.discordapp.com/attachments/1133401796073758832/1146435926688546856/7JbVvvI.jpg"
link_video = "https://www.youtube.com/watch?v=ZV7nS8sT_Fw"
link_hidden = "https://forums.pokemmo.com/index.php?/topic/147619-hidden-ability-breeding-guide/"
link_tutorial = "https://forums.pokemmo.com/index.php?/topic/49440-the-breeding-guide/"
link_paczus = "https://docs.google.com/document/d/1AH6u07Yv87gK1ReP1BsjjzVk7Z5Ue8_O/edit?usp=sharing&ouid=110637772332510300137&rtpof=true&sd=true"

def open_urls(link):
    webbrowser.open(link)

def breeding():
    breeding_window = Toplevel()

    link_label0 = Label(breeding_window, font=("Consolas", 25), cursor="hand2", fg="blue",
                        text=f"""ILUSTRACJA""")
    link_label0.pack(pady=40)
    link_label0.bind("<Button-1>", lambda e: open_urls(link_image))

    link_label1 = Label(breeding_window, font=("Consolas", 25), cursor="hand2", fg="blue",
                       text=f"""PORADNIK WIDEO""")
    link_label1.pack(pady=40)
    link_label1.bind("<Button-1>", lambda e: open_urls(link_video))

    link_label2 = Label(breeding_window, font=("Consolas", 25), cursor="hand2", fg="blue",
                       text=f"""HIDDEN ABILITY""")
    link_label2.pack(pady=40)
    link_label2.bind("<Button-1>", lambda e: open_urls(link_hidden))

    link_label3 = Label(breeding_window, font=("Consolas", 25), cursor="hand2", fg="blue",
                       text=f"""PORADNIK NA FORUM""")
    link_label3.pack(pady=40)
    link_label3.bind("<Button-1>", lambda e: open_urls(link_tutorial))

    link_label4 = Label(breeding_window, font=("Consolas", 25), cursor="hand2", fg="blue",
                       text=f"""POLSKI PORADNIK""")
    link_label4.pack(pady=40)
    link_label4.bind("<Button-1>", lambda e: open_urls(link_paczus))