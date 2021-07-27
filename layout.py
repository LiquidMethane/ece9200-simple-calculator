import tkinter as tk
from controller import Controller


class Layout:
    __root = tk.Tk()
    __var_mode = tk.StringVar()
    __var_display = tk.StringVar()

    # button event callback
    def __handle_input(self, char):
        self.__controller.handle_input(char)
        return

    def set_mode(self, mode):
        if mode == 'RPN':
            self.__var_mode.set('RPN')
            self.__btn_enter['state'] = 'normal'

        else:
            self.__var_mode.set('INFIX')
            self.__btn_enter['state'] = 'disabled'
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

        # create frame for button grid
        frm_btn_grd = tk.Frame(master=frm_btns, height=200)
        frm_btn_grd.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # button displays
        num_list = ['7', '8', '9', '/', '4', '5', '6', 'x', '1', '2', '3', '-', ' ', '0', '.', '+']

        # initialize result display
        lbl_display = tk.Label(master=frm_display, width=13, height=1, textvariable=self.__var_display, anchor='e', font=('Courier', 70), bg='black', fg='white')
        lbl_display.pack(fill=tk.X, side=tk.RIGHT)

        # initialize number and operator layout
        self.__var_mode.set('INFIX')
        for i in range(4):
            for j in range(4):

                # create frame for button
                frm = tk.Frame(master=frm_btn_grd)
                frm.grid(row=i, column=j)

                # create number and operator buttons
                if 4 * i + j != 12:
                    tk.Button(
                        master=frm,
                        height=3,
                        width=6,
                        text=num_list[4 * i + j],
                        font=('Courier', 30),
                        command=lambda name=num_list[4 * i + j]: self.__handle_input(name)
                    ).pack()

                # create mode button
                else:
                    tk.Button(
                        master=frm,
                        height=3,
                        width=6,
                        textvariable=self.__var_mode,
                        font=('Courier', 30),
                        command=lambda name='M': self.__handle_input(name)
                    ).pack()

                pass
            pass

        frm_enter = tk.Frame(master=frm_btns)
        frm_enter.pack(side=tk.LEFT)
        self.__btn_enter = tk.Button(
            master=frm_enter,
            height=14,
            width=6,
            text='ENTER',
            font=('Courier', 30),
            state='disabled',
            command=lambda name='E': self.__handle_input(name)
        )
        self.__btn_enter.pack(side=tk.RIGHT)


def main():
    Layout().start_gui()
    return


if __name__ == '__main__':
    main()
