# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:54:57 2024

@author: Antedis
"""

import tkinter as tk
from tkinter import scrolledtext
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os

# Lire la clé API depuis le fichier config.py
try:
    from config import API_KEY
except ImportError:
    print("Erreur : Le fichier 'config.py' est introuvable ou ne contient pas la clé API.")
    exit()

# Initialisation du client Mistral avec la clé API
api_key = API_KEY
model = "mistral-small"
client = MistralClient(api_key=api_key)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Mistral AI Chat")

# Création du widget pour afficher les messages
messages_frame = tk.Frame(root)
messages_frame.pack(side="top", fill="both", expand=True)

messages_scrollbar = tk.Scrollbar(messages_frame)
messages_scrollbar.pack(side="right", fill="y")

messages_box = scrolledtext.ScrolledText(messages_frame, state="disabled", wrap="word", yscrollcommand=messages_scrollbar.set)
messages_box.pack(side="left", fill="both", expand=True)

# Fonction pour envoyer le message de l'utilisateur
def send_message():
    user_input = entry_box.get()
    messages_box.config(state="normal")
    messages_box.insert("end", "Vous (Role: user): {}\n".format(user_input))
    messages_box.config(state="disabled")
    messages_box.see("end")

    messages = [ChatMessage(role="user", content=user_input)]
    chat_response = client.chat(model=model, messages=messages)

    for choice in chat_response.choices:
        messages_box.config(state="normal")
        messages_box.insert("end", "Mistral AI (Role: {}): {}\n".format(choice.message.role, choice.message.content))
        messages_box.config(state="disabled")
        messages_box.see("end")

    entry_box.delete(0, "end")

# Création du widget pour saisir le message de l'utilisateur
entry_frame = tk.Frame(root)
entry_frame.pack(side="bottom", fill="x")

entry_box = tk.Entry(entry_frame, width=80)
entry_box.pack(side="left", fill="x", expand=True)

send_button = tk.Button(entry_frame, text="Envoyer", command=send_message)
send_button.pack(side="right")

# Lancement de la boucle principale de l'application Tkinter
root.mainloop()