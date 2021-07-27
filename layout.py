import tkinter as tk
from controller import Controller


class Layout:
    __root = tk.Tk()
    __var_mode = tk.StringVar()
    __var_display = tk.StringVar()
    # __controller = None

    # button event callback
    def __handle_input(self, char):
        self.__controller.handle_input(char)
        return

    def set_mode(self, mode):
        self.__var_mode.set('RPN') if mode else self.__var_mode.set('INFIX')
        return

    def set_display(self, val):
        self.__var_display.set(val)

    def start_gui(self):
        self.__root.mainloop()

    def __init__(self):
        self.__controller = Controller(self)

        # give the window a name
        self.__root.title('Sketchy Calculator')

        # create frame for display field
        frm_display = tk.Frame(master=self.__root, width=200, height=50, bg='black')
        frm_display.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        # create frame for button field
        frm_btns = tk.Frame(master=self.__root, height=200)
        frm_btns.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        # button displays
        num_list = ['7', '8', '9', '/', '4', '5', '6', 'x', '1', '2', '3', '-', ' ', '0', '.', '+']

        # initialize result display
        lbl_display = tk.Label(master=frm_display, width=15, height=1, textvariable=self.__var_display, anchor='e', font=('Courier', 74), bg='black', fg='white')
        lbl_display.pack(fill=tk.X, side=tk.RIGHT)
        # var_res.set('0000000000')

        # initialize number and operator layout
        self.__var_mode.set('INFIX')
        for i in range(4):
            for j in range(4):

                # create frame for button
                frm = tk.Frame(master=frm_btns)
                frm.grid(row=i, column=j)

                # create number and operator buttons
                if 4 * i + j != 12:
                    tk.Button(
                        master=frm,
                        height=4,
                        width=8,
                        text=num_list[4 * i + j],
                        font=('Courier', 34),
                        command=lambda name=num_list[4 * i + j]: self.__handle_input(name)
                    ).pack()

                # create mode button
                else:
                    tk.Button(
                        master=frm,
                        height=4,
                        width=8,
                        textvariable=self.__var_mode,
                        font=('Courier', 34),
                        command=lambda name='M': self.__handle_input(name)
                    ).pack()


def main():
    Layout().start_gui()
    return


if __name__ == '__main__':
    main()
