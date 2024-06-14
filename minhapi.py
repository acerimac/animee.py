import tkinter as tk
from tkinter import scrolledtext


animes = [
    {"nome": "Naruto", "genero": "Ação e Comédia", "ano": 2002},
    {"nome": "Death Note", "genero": "Suspense e Mistério", "ano": 2006},
    {"nome": "One Piece", "genero": "Ação e Aventura", "ano": 1999},
    {"nome": "Hunter x Hunter", "genero": "Fantasia e Drama", "ano": 2011},
    {"nome": "Ataque dos Titãs", "genero": "Mistério e Aventura", "ano": 2013},
    {"nome": "Haikyuu", "genero": "Esporte e Comédia", "ano": 2012},
    {"nome": "My Hero Academia", "genero": "Fantasia e Ação", "ano": 2016},
    {"nome": "Bungou Stray Dogs", "genero": "Mistério e Fantasia", "ano": 2016},
    {"nome": "Noragami", "genero": "Mistério e Comédia", "ano": 2014}
]

def exibir_animes():
    root = tk.Tk()
    root.title("Lista de Animes")

    text_area = scrolledtext.ScrolledText(root, width=50, height=20, wrap=tk.WORD)
    text_area.pack(padx=10, pady=10)

    for anime in animes:
        text_area.insert(tk.END, f"{anime['nome']} - {anime['genero']} ({anime['ano']})\n\n")

    root.mainloop()

exibir_animes()
