import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
import datetime

API_KEY = 'YOUR_API_KEY'
URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

class CurrencyConverter:
    def __init__(self, root):
        # ... (создание интерфейса)
        self.load_history()

    def get_rates(self):
        response = requests.get(URL)
        data = response.json()
        return data['conversion_rates']

    def convert(self):
        # ... (логика конвертации и валидации)
        self.save_history(...)

    def save_history(self, entry):
        try:
            with open('history.json', 'r') as f:
                history = json.load(f)
        except FileNotFoundError:
            history = []
        history.append(entry)
        with open('history.json', 'w') as f:
            json.dump(history, f)

    def load_history(self):
        # ... (загрузка истории в таблицу)

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
