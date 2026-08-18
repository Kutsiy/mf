from tkinter import *
from .two_d import *

def command_creator(root):
    def get_command_with_root(command):
        return lambda: command(root=root)

    return get_command_with_root


def create_button(root, text: str, row: int, column: int, command, pad=5):
    button = Button(master=root, text=text, font=("Arial", 10, "bold"), width=12, height=2, padx=10, pady=10, command=command)

    button.grid(row=row, column=column, padx=pad, pady=pad)


def start():
    root = Tk()
    root.title("Choose what you want to see!")

    root.geometry("500x450")
    root.configure(bg='gray')

    buttons_frame = Frame(root, bg="gray")
    buttons_frame.pack(padx=20, pady=20)

    command_cr = command_creator(root=root)

    first_scene = command_cr(command=start_first_scene)

    create_button(root=buttons_frame, text="First scene", row=0, column=0, command=first_scene)
    create_button(root=buttons_frame, text="Second scene", row=0, column=1, command=None)
    create_button(root=buttons_frame, text="Third scene", row=1, column=0, command=None)
    create_button(root=buttons_frame, text="Four scene", row=1, column=1, command=None)


    button = Button(root, text="Quit", font=("Arial", 12, "bold"), width=12, height=2, command=root.destroy)
    button.pack(side=BOTTOM, pady=25)

    root.mainloop()