from tkinter import *
from tkinter import messagebox
import time

root = Tk()

root.title("Capitals of europe quiz")
root_label=Label(text="Capital of europe quiz",font=("Century Gothic",36))
root_label.grid(row=0,column=2)

score_label=Label(text="Score :",font=("Monaco",22))
score_label.grid(row=1,column=2)

Score_r_label=Label(text="",font=("Arial",18))
Score_r_label.grid(row=2,column=2)

Lives_label=Label(text="Lives :",font=("Monaco",18))
Lives_label.grid(row=3,column=2)

Lives_r_label=Label(text="",font=("Arial",18))
Lives_r_label.grid(row=4,column=2)

Country_label=Label(text="",font=("Monaco",24))
Country_label.grid(row=5,column=2)

answr_label=Label(text="Answer :",font=("Monac",16))
answr_label.grid(row=6,column=2)

answer_entry=Entry()
answer_entry.grid(row=7,column=2)

wrong_ans_label=Label(text="",font=("Monaco",16),fg="red")
wrong_ans_label.grid(row=8,column=2)


x=True

score=0
lives=3
con =0

Capials = european_countries = [
    ["Albania", "tirana"],
    ["Andorra", "andorralavella"],
    ["Austria", "vienna"],
    ["Belgium", "brussels"],
    ["Bulgaria", "sofia"],
    ["Croatia", "zagreb"],
    ["Czech Republic", "prague"],
    ["Denmark", "copenhagen"],
    ["Estonia", "tallinn"],
    ["Finland", "helsinki"],
    ["France", "paris"],
    ["Germany", "berlin"],
    ["Greece", "athens"],
    ["Hungary", "budapest"],
    ["Ireland", "dublin"],
    ["Italy", "rome"],
    ["Latvia", "riga"],
    ["Liechtenstein", "vaduz"],
    ["Lithuania", "vilnius"],
    ["Luxembourg", "luxembourgcity"],
    ["Malta", "valletta"],
    ["Moldova", "chisinau"],
    ["Monaco", "monaco"],
    ["Netherlands", "amsterdam"],
    ["Norway", "oslo"],
    ["Poland", "warsaw"],
    ["Portugal", "lisbon"],
    ["Romania", "bucharest"],
    ["Russia", "moscow"],
    ["Slovakia", "bratislava"],
    ["Slovenia", "ljubljana"],
    ["Spain", "madrid"],
    ["Sweden", "stockholm"],
    ["Switzerland", "bern"],
    ["Ukraine", "kyiv"],
    ["United Kingdom", "london"],
]

def start():
    global con 
    Start_button.destroy()
    Country_label.config(text=Capials[con][0])
    Lives_r_label.config(text=lives)
        
def answer(event=None):
    global score
    global con
    global lives
    answer_user=answer_entry.get()
    wrong_ans_label.config(text="")
    if answer_user.lower().strip()==Capials[con][1]:
        score+=1
        Score_r_label.config(text=score)
        con+=1
    else:

        lives-=1
        Lives_r_label.config(text=lives)
        wrong_ans_label.config(text=Capials[con][1])
        time.sleep(1)
        con+=1
        if lives==0:
            messagebox.showinfo("Quiz","No more lives")
            exit()
        
        
    Country_label.config(text=Capials[con][0])
    answer_entry.delete(0,END)

def show():
    global con 
    global lives
    wrong_ans_label.config(text=Capials[con][1])
    lives-=1
    Lives_r_label.config(text=lives)

root.bind("<Return>",answer)

Start_button=Button(text="Start",font=("Arial",16),padx=22,command=start)
Start_button.grid(row=9,column=2)

answer_button=Button(text="Answer",font=("Arial",16),padx=10,command=lambda: answer())
answer_button.grid(row=10,column=2)

show_button=Button(text="Show answer",font=("Arial",11),padx=2,command=show)
show_button.grid(row=11,column=2)

root.mainloop()