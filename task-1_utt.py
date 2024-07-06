import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator
def translate_text():
    try:
        text = text_entry.get("1.0", tk.END).strip()
        src_lang = src_lang_combobox.get()
        dest_lang = dest_lang_combobox.get()
        
        if not text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        translator = Translator()
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        result_text.set(translation.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))
# Create the main window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("400x300")

# Create and place widgets
# Source language
tk.Label(root, text="Source Language:").pack(pady=5)
src_lang_combobox = ttk.Combobox(root, values=["en", "es", "fr", "de", "it", "pt", "zh-cn", "ja"])
src_lang_combobox.pack(pady=5)
src_lang_combobox.set("en")  # Default value

# Destination language
tk.Label(root, text="Destination Language:").pack(pady=5)
dest_lang_combobox = ttk.Combobox(root, values=["en", "es", "fr", "de", "it", "pt", "zh-cn", "ja"])
dest_lang_combobox.pack(pady=5)
dest_lang_combobox.set("es")  # Default value

# Text entry
tk.Label(root, text="Enter text to translate:").pack(pady=5)
text_entry = tk.Text(root, height=5, width=40)
text_entry.pack(pady=5)

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=5)

# Result label
tk.Label(root, text="Translated text:").pack(pady=5)
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=300)
result_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
