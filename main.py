import tkinter as tk
import random

from toggled_frame import Toggled_Frame

import comments
import parse

class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack(side="top", fill="both", expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for i in (Main_Menu, Character_Creation, Game):
            page_name = i.__name__
            frame = i(window, self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.Show_Frame("Game")

    def Show_Frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class Main_Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        self.lbl_title = tk.Label(self, text="PARANOIA: The Text Adventure")
        self.lbl_title.pack()

        self.lbl_comment = tk.Label(self, text=random.choice(comments.comments))
        self.lbl_comment.pack()

        self.btn_new_game = tk.Button(self, text="New Game")
        self.btn_new_game.pack()

        self.btn_load_game = tk.Button(self, text="Load Game")
        #self.btn_load_game.pack()

        self.btn_options = tk.Button(self, text="Options", command=self.Options)
        self.btn_options.pack()

        self.lbl_options = tk.Label(self, text="There are no options. Options are treason. Treason is punishable by death. Please report to the nearest booth for termination. Have a nice day!")

    def New_Game(self):
        pass

    def Load_Game(self):
        pass

    def Options(self):
        self.btn_options.pack_forget()
        self.lbl_options.pack()

class Character_Creation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

class Game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        self.frm_name = tk.Frame(self)
        self.frm_name.pack(fill=tk.X)

        self.lbl_name = tk.Label(self.frm_name, text="NAME")
        self.lbl_name.pack(fill=tk.X)

        self.frm_info = tk.Frame(self)
        self.frm_info.pack(side=tk.LEFT, fill=tk.Y, pady=20, padx=20)

        self.tgl_attributes = Toggled_Frame(self.frm_info, text="Attributes")
        self.tgl_attributes.pack()
        
        self.tgl_skills = Toggled_Frame(self.frm_info, text="Skills")
        self.tgl_skills.pack()
        
        self.tlg_inventory = Toggled_Frame(self.frm_info, text="Inventory")
        self.tlg_inventory.pack()

        self.frm_commands = tk.Frame(self)
        self.frm_commands.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=20, padx=20)

        self.txt_commands = tk.Text(self.frm_commands)
        self.txt_commands.pack(fill=tk.BOTH, expand=True)
        
        self.ent_commands = tk.Entry(self.frm_commands)
        self.ent_commands.pack(fill=tk.X)

        self.ent_commands.bind("<Return>", self.On_Enter_Pressed)
        self.txt_commands.config(state="disabled")

    def Print_Information(self):
        pass

    def Process_Command(self, text):
        print("process")

    def On_Enter_Pressed(self, e):
        user_input = e.widget.get()
        
        e.widget.delete("0", tk.END)

        self.Process_Command(parse.Parse_Input(user_input))

        self.Print_Information()

    def Insert_Text(self, text):
        self.txt_commands.config(state="normal")
        
        self.txt_commands.delete("0.0", tk.END)
        self.txt_commands.insert("0.0", text)
        
        self.txt_commands.config(state="disabled")

    def New_Game(self):
        while True:
            ""

if __name__ == "__main__":
    root = Window()
    root.resizable(width=False, height=False)
    root.geometry("800x600")
    root.title("gameu")
    #root.minsize(1200, 600)
    #root.update()
    
    root.mainloop()
