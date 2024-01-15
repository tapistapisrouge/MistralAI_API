# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:49:49 2024

@author: Antedis
"""


from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os
import sys

# Read the API key from the config file
try:
    from config import API_KEY
except ImportError:
    print("Error: The file 'config.py' is missing or does not contain the API key.")
    sys.exit()


# Initialisation du client Mistral avec la clé API
api_key = API_KEY
model = "mistral-medium"
# model = "mistral-small"
# model = "mistral-tiny"
client = MistralClient(api_key=api_key)

# Demander un prompt à l'utilisateur
user_input = input("Entrez votre texte : ")

# Préparation du message
messages = [ChatMessage(role="user", content=user_input)]

# Envoi du message et réception de la réponse
chat_response = client.chat(model=model, messages=messages)

# Affichage de la réponse
print("Réponse de Mistral AI :")
for choice in chat_response.choices:
    print("Mistral AI (Role: {}): {}".format(choice.message.role, choice.message.content))

