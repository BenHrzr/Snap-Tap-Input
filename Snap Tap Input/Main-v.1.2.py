import tkinter as tk
from tkinter import ttk
import keyboard

## Start

n = int(0)
running = False

def start_programm():
    window.iconphoto(False, tk.PhotoImage(file="Snap Tap Input\padlock_11189748.png"))
    global running
    running = True
    StartButton.config(bg='#388E3C', fg='white')  
    StoppButton.config(bg='#FF8A80', fg='white')
    main()

def stopp_programm():
    window.iconphoto(False, tk.PhotoImage(file="Snap Tap Input\padlock_8847721.png"))
    global running
    running = False
    keyboard.unhook_all()
    StoppButton.config(bg='#FF5252', fg='white')  
    StartButton.config(bg='#81C784', fg='white')
    print("Programm gestoppt")

## GUI

window = tk.Tk()

window.iconphoto(False, tk.PhotoImage(file="Snap Tap Input\pyramid-chart_7791415.png"))
window.title("Snap Tap Input")
window.geometry("280x320")
window.config(bg="#263238")  
window.resizable(False, False)
#window.iconphoto(False, tk.PhotoImage(file="Snap Tap Input\pyramid-chart_7791415.png"))



## Snap Tap Programmierung

def main ():

    alle_tasten={'esc': 1, 'f1': 2, 'f2': 3, 'f3': 4, 'f4': 5, 'f5': 6, 'f6': 7, 'f7': 8, 'f8': 9, 'f9': 10, 'f10': 11, 'f11': 12, 'f12': 13,'print_screen': 14, 'scroll_lock': 15, 'pause': 16,'backtick': 17, '1': 18, '2': 19, '3': 20, '4': 21, '5': 22, '6': 23, '7': 24, '8': 25, '9': 26, '0': 27, 'minus': 28, 'equals': 29, 'backspace': 30,'tab': 31, 'q': 32, 'w': 33, 'e': 34, 'r': 35, 't': 36, 'y': 37, 'u': 38, 'i': 39, 'o': 40, 'p': 41, 'left_bracket': 42, 'right_bracket': 43, 'backslash': 44,'caps_lock': 45, 'a': 46, 's': 47, 'd': 48, 'f': 49, 'g': 50, 'h': 51, 'j': 52, 'k': 53, 'l': 54, 'semicolon': 55, 'quote': 56, 'enter': 57,'left_shift': 58, 'z': 59, 'x': 60, 'c': 61, 'v': 62, 'b': 63, 'n': 64, 'm': 65, 'comma': 66, 'period': 67, 'slash': 68, 'right_shift': 69,'left_ctrl': 70, 'left_windows': 71, 'left_alt': 72, 'space': 73, 'right_alt': 74, 'right_windows': 75, 'menu': 76, 'right_ctrl': 77,'insert': 78, 'home': 79, 'page_up': 80, 'delete': 81, 'end': 82, 'page_down': 83,'up': 84, 'down': 85, 'left': 86, 'right': 87,'num_lock': 88, 'num_divide': 89, 'num_multiply': 90, 'num_subtract': 91, 'num_add': 92, 'num_enter': 93,'num_1': 94, 'num_2': 95, 'num_3': 96, 'num_4': 97, 'num_5': 98, 'num_6': 99, 'num_7': 100, 'num_8': 101, 'num_9': 102, 'num_0': 103, 'num_decimal': 104,'ä': 105, 'ö': 106, 'ü': 107, 'ß': 108}

    
    gedrueckte_tasten = set()
    erlaubte_tasten = {'a', 'd', 'left', 'right'}

    if running:

        print("Programm gestartet") #Debugging

        def on_key_event(event):
            tasten_status = event.event_type
            gedrueckteTaste = event.name

            if gedrueckteTaste in erlaubte_tasten:
                if tasten_status == 'down':
                    
                    if gedrueckteTaste not in ['w', 'up']:
                        for Taste in list(gedrueckte_tasten):
                            if Taste != gedrueckteTaste:
                                keyboard.release(Taste)
                                gedrueckte_tasten.remove(Taste)

                    gedrueckte_tasten.add(gedrueckteTaste)
                elif tasten_status == 'up':
                    if gedrueckteTaste in gedrueckte_tasten:
                        gedrueckte_tasten.remove(gedrueckteTaste)

        keyboard.hook(on_key_event)
    else:
        print("Programm gestoppt (running)") #Debugging


button_style = {
    'font': ('Roboto', 16, 'bold'),
    'height': 1,
    'width': 12,
    'cursor': 'hand2',
    'bd': 0,  
    'relief': tk.RIDGE
}

StartButton = tk.Button(window,
                        text="START",
                        bg='#81C784',  
                        fg='white',
                        activebackground='#388E3C',  
                        activeforeground='white',
                        command=start_programm,
                        **button_style)


StoppButton = tk.Button(window,
                        text="STOP",
                        bg='#FF8A80',  
                        fg='white',
                        activebackground='#FF5252',  
                        activeforeground='white',
                        command=stopp_programm,
                        **button_style)

StartButton.pack(pady='70')
StoppButton.pack()
window.mainloop()

## Change log

#v1.2

#changed design
