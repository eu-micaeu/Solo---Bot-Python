import tkinter as tk
import time
import sys
import PySimpleGUI as sg

if getattr(sys, 'frozen', False):
    # O aplicativo está sendo executado em um pacote exe / app
    import os
    import sys
    import site

    # Adiciona o caminho do arquivo temporário gerado pelo PyInstaller
    site.addsitedir(os.path.join(sys._MEIPASS, "pykakasi"))

try:
    from pykakasi import kakasi
except ImportError:
    print("Erro ao importar pykakasi")

    # Configuração do conversor de texto japonês
kks = kakasi()
kks.setMode("H", "a")
kks.setMode("K", "a")
kks.setMode("J", "a")
conv = kks.getConverter()

# Lista de letras japonesas com suas traduções
hiragana = [conv.do(chr(i)) for i in range(12353, 12436)]
katakana = [conv.do(chr(i)) for i in range(12449, 12532)]
japanese_letters = [
    (letter, "hiragana", conv.do(letter), chr(i + 12353))
    for i, letter in enumerate(hiragana)
] + [
    (letter, "katakana", conv.do(letter), chr(i + 12449))
    for i, letter in enumerate(katakana)
]

# Criar janela principal com um rótulo para exibir as letras japonesas
root = tk.Tk()
root.geometry("300x200+0+{}" .format(root.winfo_screenheight() - 280))
root.configure(bg="black")
root.title("Letreiro de LED")

label = tk.Label(root, text="", font=("Arial", 200))
label.configure(bg="black", fg="green")
label.place(relx=0.5, rely=0.5, anchor="center")

# Atualiza o rótulo indefinidamente
def update_label():
    index = 0
    while True:
        letter, _, translation, portuguese = japanese_letters[index]
        text = f" {portuguese} - {translation}"
        label.config(text=text)
        label.update()
        time.sleep(1)
        index = (index + 1) % len(japanese_letters)

root.attributes("-fullscreen", True)

# Iniciar a atualização do rótulo
update_label()




# Iniciar a janela principal
root.mainloop()