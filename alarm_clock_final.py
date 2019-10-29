import tkinter
import tkinter.messagebox
import datetime as d
import winsound

global k
k = 0

#H
def clickH():
    global f
    f = 1
    n = int(counter1.get())
    if n < 23:
        if n < 9:
            counter1.set("0" + str(n+1))
        else:
            counter1.set(str(n + 1))
    else:
        counter1.set("00")


#M
def clickM():
    global f
    f = 1
    m = int(counter2.get())
    if m < 59:
        if m < 9:
            counter2.set("0" + str(m + 1))
        else:
            counter2.set(str(m + 1))
    else:
        counter2.set("00")
        counter1.set(str(int(counter1.get()) + 1))

#A
def clickA():
    global f
    global k
    now = d.datetime.now()
    h = int(counter1.get())
    m = int(counter2.get())
    if (h <= now.hour) and (m <= now.minute):
        tkinter.messagebox.showinfo('Failure', 'This time is not available today')
        f = 0
        time()
    elif k == 1:
        tkinter.messagebox.showinfo('Calm', 'Alarm clock was turned off')
        k = 0
    else:
        current_time = now.hour * 60 + now.minute
        alarm_time = h * 60 + m
        tkinter.messagebox.showinfo('Success', 'The time was successfully set')
        window.after((alarm_time - current_time) * 60000,  bebeep)
        k = 1


#time function (6000ms update)
def time():
    global f
    if f == 0:
        now = d.datetime.now()
        hh = now.hour
        mm = now.minute
        if hh <= 9:
            counter1.set("0" + str(hh))
        else:
            counter1.set(str(hh))
        if mm < 9:
            counter2.set("0" + str(mm))
        else:
            counter2.set(str(mm))
        window.after(6000, time)


#sound
def bebeep():
    global k
    if k == 1:
        winsound.Beep(1000, 5000)
        global f
        f = 0
        time()
    else:
        winsound.Beep(1000, 0)


#interface
if __name__ == '__main__':
    window = tkinter.Tk()
    window.geometry('300x140')
    window.title('Alarm clock')
    window.configure(bg="black")

    top_frame = tkinter.Frame()
    bottom_frame = tkinter.Frame()

    top_frame.pack()
    bottom_frame.pack()

    counter1 = tkinter.StringVar()
    counter2 = tkinter.StringVar()
    f = 0
    time()

    button1 = tkinter.Button(bottom_frame, text='H',  width=12, bg="white", command=clickH)
    button1.pack(side="left")

    label1 = tkinter.Label(top_frame, font='Times 70', fg='green', bg="black", textvariable=counter1)
    label1.pack(side="left")

    button2 = tkinter.Button(bottom_frame, text='M', width=12, bg="white", command=clickM)
    button2.pack(side="left")

    label2 = tkinter.Label(top_frame, text=':', font='Times 70', fg='green', bg="black")
    label2.pack(side="left")

    label3 = tkinter.Label(top_frame, font='Times 70', fg='green', bg="black", textvariable=counter2)
    label3.pack(side="left")

    button3 = tkinter.Button(bottom_frame, text='A', width=12, bg="white", command=clickA)
    button3.pack(side="right")

    window.mainloop()
