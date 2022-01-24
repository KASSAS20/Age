import tkinter as tk

win = tk.Tk()
win.geometry('500x500')
win.title('Age')
win['bg'] = '#252526'
win.resizable(height=False, width=False)

def calculation():
    try:
        x = int(CAT_ENTRY.get())
    except:
        x = -1
    HUMAN = 0
    count = 1
    while True:
        try:
            if count > x:
                break
            elif count>0 and count<5:
                HUMAN+=7
            elif count>4 and count<16:
                HUMAN+=4
            elif count>15 and count<43:
                HUMAN+=3
            else:
                HUMAN = 'ERROR'
            count+=1
        except:
            HUMAN = 'ERROR'
    HUMAN_LABEL['text'] = HUMAN
    CAT_ENTRY.delete(0, tk.END)



CAT_ENTRY = tk.Entry(font=('Comic CAT', 30),
                     justify='center', fg='#FFFFFF', bg='#252526', bd=1)
CAT_ENTRY.grid(row=0, column=0, columnspan=3, sticky='wens', padx=10, pady=10)

HUMAN_LABEL = tk.Label(text='0', font=(
    'Comic CAT', 50), fg='#FFFFFF', bg='#252526')
HUMAN_LABEL.grid(row=1, column=0, columnspan=3, sticky='wens', padx=10, pady=10)

BUTTON = tk.Button(text='Next', font=('Comic CAT', 20), bg='#252526', fg='#FFFFFF', bd=0, command=lambda: calculation())
BUTTON.grid(row=2, column=1, sticky='wens', padx=10, pady=10)

win.grid_columnconfigure(0, minsize=125)
win.grid_columnconfigure(1, minsize=250)
win.grid_columnconfigure(2, minsize=125)
win.grid_rowconfigure(0, minsize=100)
win.grid_rowconfigure(1, minsize=250)
win.grid_rowconfigure(2, minsize=150)

win.mainloop()
