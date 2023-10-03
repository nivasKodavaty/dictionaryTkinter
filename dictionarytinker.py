import tkinter as tk
import requests

API_KEY = 'YOUR_API_KEY'

def get_definition(word):
    try:
        url = f'https://wordsapiv1.p.rapidapi.com/words/{word}'
        headers = {
            'X-RapidAPI-Host': 'wordsapiv1.p.rapidapi.com',
            'X-RapidAPI-Key': API_KEY
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        definition = data.get('results', {}).get('definition', 'Word not found.')

        definition_label.config(text=f"Definition: {definition}")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

app = tk.Tk()
app.title("Dictionary App")

# Create GUI elements
word_label = tk.Label(app, text="Enter a word:")
word_label.pack()

word_entry = tk.Entry(app)
word_entry.pack()

get_definition_button = tk.Button(app, text="Get Definition", command=lambda: get_definition(word_entry.get()))
get_definition_button.pack()

definition_label = tk.Label(app, text="")
definition_label.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
