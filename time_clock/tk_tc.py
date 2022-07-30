#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jul 29, 2022 12:20:01 PM EDT  platform: Windows NT

import datetime
import sys, traceback
import tkinter as tk
import tkinter.ttk as ttk
import time
import requests as rq
from datetime import timedelta
#
def send_data(e_email,e_pass,p_number,p_name,p_desc,start,stop,url):
    package = {}
    package['employee_email'] = e_email
    package['employee_pass'] = e_pass
    package['project_number'] = p_number
    package['project_name'] = p_name
    package['project_desc'] = p_desc
    package['start_time'] = start
    package['stop_time'] = stop
    response = rq.post(url,json=package)
    return [response.status_code, response.text, response.json()]
#
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        self.clocked_in = False
        self.running = False
        self.url = '192.168.2.156:5000'
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("712x500+428+349")
        top.minsize(120, 1)
        top.maxsize(3604, 1061)
        top.resizable(1,  1)
        top.title("Time Clock")
        top.configure(background="#d9d9d9")
        #
        self.Clock_In = tk.Button(top)
        self.Clock_In.place(relx=0.027, rely=0.02, height=114, width=177)
        self.Clock_In.configure(activebackground="#ececec")
        self.Clock_In.configure(activeforeground="#000000")
        self.Clock_In.configure(background="#d9d9d9")
        self.Clock_In.configure(cursor="fleur")
        self.Clock_In.configure(disabledforeground="#a3a3a3")
        self.Clock_In.configure(foreground="#000000")
        self.Clock_In.configure(highlightbackground="#d9d9d9")
        self.Clock_In.configure(highlightcolor="black")
        self.Clock_In.configure(pady="0")
        self.Clock_In.configure(text='''Clock In''')

        self.Start_Project = tk.Button(top)
        self.Start_Project.place(relx=0.027, rely=0.266, height=114, width=177)
        self.Start_Project.configure(activebackground="#ececec")
        self.Start_Project.configure(activeforeground="#000000")
        self.Start_Project.configure(background="#d9d9d9")
        self.Start_Project.configure(disabledforeground="#a3a3a3")
        self.Start_Project.configure(foreground="#000000")
        self.Start_Project.configure(highlightbackground="#d9d9d9")
        self.Start_Project.configure(highlightcolor="black")
        self.Start_Project.configure(pady="0")
        self.Start_Project.configure(text='''Start Project''')

        self.Stop_Project = tk.Button(top)
        self.Stop_Project.place(relx=0.027, rely=0.51, height=114, width=177)
        self.Stop_Project.configure(activebackground="#ececec")
        self.Stop_Project.configure(activeforeground="#000000")
        self.Stop_Project.configure(background="#d9d9d9")
        self.Stop_Project.configure(disabledforeground="#a3a3a3")
        self.Stop_Project.configure(foreground="#000000")
        self.Stop_Project.configure(highlightbackground="#d9d9d9")
        self.Stop_Project.configure(highlightcolor="black")
        self.Stop_Project.configure(pady="0")
        self.Stop_Project.configure(text='''Stop Project''')

        self.Clock_Out = tk.Button(top)
        self.Clock_Out.place(relx=0.027, rely=0.756, height=114, width=177)
        self.Clock_Out.configure(activebackground="#ececec")
        self.Clock_Out.configure(activeforeground="#000000")
        self.Clock_Out.configure(background="#d9d9d9")
        self.Clock_Out.configure(disabledforeground="#a3a3a3")
        self.Clock_Out.configure(foreground="#000000")
        self.Clock_Out.configure(highlightbackground="#d9d9d9")
        self.Clock_Out.configure(highlightcolor="black")
        self.Clock_Out.configure(pady="0")
        self.Clock_Out.configure(text='''Clock Out''')

        self.email_label = tk.Label(top)
        self.email_label.place(relx=0.669, rely=0.02, height=20, width=86)
        self.email_label.configure(background="#d9d9d9")
        self.email_label.configure(disabledforeground="#a3a3a3")
        self.email_label.configure(foreground="#000000")
        self.email_label.configure(text='''Employee Email''')

        self.email_entry = tk.Entry(top)
        self.email_entry.place(relx=0.669, rely=0.058, height=20, relwidth=0.287)

        self.email_entry.configure(background="white")
        self.email_entry.configure(disabledforeground="#a3a3a3")
        self.email_entry.configure(font="TkFixedFont")
        self.email_entry.configure(foreground="#000000")
        self.email_entry.configure(insertbackground="black")

        def openview(url):
            projlist = rq.get(url).json()
            projlist.sort(key=lambda tup: tup[3])
            project_numbers = {}
            for i in projlist:
                if not i[0] == self.email_entry.get(): continue
                if i[1] not in project_numbers.keys():
                    project_numbers[i[1]] = {}
                    project_numbers[i[1]]['number'] = i[1]
                    project_numbers[i[1]]['name'] = i[2]
                    project_numbers[i[1]]['desc'] = i[3]
                    project_numbers[i[1]]['runtime'] = float(i[5])-float(i[4])
                    project_numbers[i[1]]['times'] = []
                    project_numbers[i[1]]['times'].append([i[4],i[5]])
                elif i[1] in project_numbers.keys():
                    project_numbers[i[1]]['runtime'] = project_numbers[i[1]]['runtime'] + (float(i[5])-float(i[4]))
                    project_numbers[i[1]]['times'].append([i[4],i[5]])
            new_win = tk.Toplevel(root)
            scroll = tk.Scrollbar(new_win)
            scroll.pack(side="right",fill="both")
            proj_listbox = tk.Listbox(new_win,width=200)
            proj_listbox.pack(side="left",fill="both")
            proj_listbox.config(yscrollcommand = scroll.set)
            scroll.config(command = proj_listbox.yview)
            for number in sorted(project_numbers.keys()):
                for time in project_numbers[number]['times']:
                    proj_listbox.insert('end',f"Project Number: {project_numbers[number]['number']} // Project Name: {project_numbers[number]['name']} // Project Description: {project_numbers[number]['desc']} // Start Time: {datetime.datetime.fromtimestamp(time[0]).strftime('%m/%d/%Y, %H:%M:%S')} // Stop Time: {datetime.datetime.fromtimestamp(time[1]).strftime('%m/%d/%Y, %H:%M:%S')} // Runtime: {str(timedelta(seconds=time[1]-time[0]))}")
        #
        self.menubar = tk.Menu(top)
        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="View", command=lambda: openview(self.url))
        self.menubar.add_cascade(label="File", menu=filemenu)
        top.configure(menu=self.menubar)

        self.password_label = tk.Label(top)
        self.password_label.place(relx=0.669, rely=0.114, height=20, width=105)
        self.password_label.configure(activebackground="#f9f9f9")
        self.password_label.configure(activeforeground="black")
        self.password_label.configure(background="#d9d9d9")
        self.password_label.configure(disabledforeground="#a3a3a3")
        self.password_label.configure(foreground="#000000")
        self.password_label.configure(highlightbackground="#d9d9d9")
        self.password_label.configure(highlightcolor="black")
        self.password_label.configure(text='''Employee Password''')

        self.password_entry = tk.Entry(top)
        self.password_entry.place(relx=0.669, rely=0.152, height=20
                , relwidth=0.287)
        self.password_entry.configure(background="white")
        self.password_entry.configure(disabledforeground="#a3a3a3")
        self.password_entry.configure(font="TkFixedFont")
        self.password_entry.configure(foreground="#000000")
        self.password_entry.configure(highlightbackground="#d9d9d9")
        self.password_entry.configure(highlightcolor="black")
        self.password_entry.configure(insertbackground="black")
        self.password_entry.configure(selectbackground="blue")
        self.password_entry.configure(selectforeground="white")
        self.password_entry.configure(show="*")
        #
        def clockin(email,password):
            
        self.number_label = tk.Label(top)
        self.number_label.place(relx=0.669, rely=0.208, height=20, width=86)
        self.number_label.configure(activebackground="#f9f9f9")
        self.number_label.configure(activeforeground="black")
        self.number_label.configure(background="#d9d9d9")
        self.number_label.configure(disabledforeground="#a3a3a3")
        self.number_label.configure(foreground="#000000")
        self.number_label.configure(highlightbackground="#d9d9d9")
        self.number_label.configure(highlightcolor="black")
        self.number_label.configure(text='''Project Number''')

        self.number_entry = tk.Entry(top)
        self.number_entry.place(relx=0.669, rely=0.246, height=20
                , relwidth=0.287)
        self.number_entry.configure(background="white")
        self.number_entry.configure(disabledforeground="#a3a3a3")
        self.number_entry.configure(font="TkFixedFont")
        self.number_entry.configure(foreground="#000000")
        self.number_entry.configure(highlightbackground="#d9d9d9")
        self.number_entry.configure(highlightcolor="black")
        self.number_entry.configure(insertbackground="black")
        self.number_entry.configure(selectbackground="blue")
        self.number_entry.configure(selectforeground="white")

        self.name_label = tk.Label(top)
        self.name_label.place(relx=0.669, rely=0.302, height=20, width=77)
        self.name_label.configure(activebackground="#f9f9f9")
        self.name_label.configure(activeforeground="black")
        self.name_label.configure(background="#d9d9d9")
        self.name_label.configure(cursor="fleur")
        self.name_label.configure(disabledforeground="#a3a3a3")
        self.name_label.configure(foreground="#000000")
        self.name_label.configure(highlightbackground="#d9d9d9")
        self.name_label.configure(highlightcolor="black")
        self.name_label.configure(text='''Project Name''')

        self.name_entry = tk.Entry(top)
        self.name_entry.place(relx=0.669, rely=0.34, height=20, relwidth=0.287)
        self.name_entry.configure(background="white")
        self.name_entry.configure(disabledforeground="#a3a3a3")
        self.name_entry.configure(font="TkFixedFont")
        self.name_entry.configure(foreground="#000000")
        self.name_entry.configure(highlightbackground="#d9d9d9")
        self.name_entry.configure(highlightcolor="black")
        self.name_entry.configure(insertbackground="black")
        self.name_entry.configure(selectbackground="blue")
        self.name_entry.configure(selectforeground="white")

        self.desc_label = tk.Label(top)
        self.desc_label.place(relx=0.669, rely=0.398, height=20, width=96)
        self.desc_label.configure(activebackground="#f9f9f9")
        self.desc_label.configure(activeforeground="black")
        self.desc_label.configure(background="#d9d9d9")
        self.desc_label.configure(disabledforeground="#a3a3a3")
        self.desc_label.configure(foreground="#000000")
        self.desc_label.configure(highlightbackground="#d9d9d9")
        self.desc_label.configure(highlightcolor="black")
        self.desc_label.configure(text='''Work Description''')

        self.desc_entry = tk.Entry(top)
        self.desc_entry.place(relx=0.669, rely=0.436, height=20, relwidth=0.287)
        self.desc_entry.configure(background="white")
        self.desc_entry.configure(disabledforeground="#a3a3a3")
        self.desc_entry.configure(font="TkFixedFont")
        self.desc_entry.configure(foreground="#000000")
        self.desc_entry.configure(highlightbackground="#d9d9d9")
        self.desc_entry.configure(highlightcolor="black")
        self.desc_entry.configure(insertbackground="black")
        self.desc_entry.configure(selectbackground="blue")
        self.desc_entry.configure(selectforeground="white")

        self.output_frame = tk.LabelFrame(top)
        self.output_frame.place(relx=0.294, rely=0.51, relheight=0.482
                , relwidth=0.701)
        self.output_frame.configure(relief='groove')
        self.output_frame.configure(foreground="black")
        self.output_frame.configure(text='''Console''')
        self.output_frame.configure(background="#d9d9d9")

        self.output = tk.Listbox(self.output_frame)
        self.output.place(relx=0.02, rely=0.079, relheight=0.909, relwidth=0.968
                , bordermode='ignore')
        self.output.configure(background="white")
        self.output.configure(disabledforeground="#a3a3a3")
        self.output.configure(font="TkFixedFont")
        self.output.configure(foreground="#000000")

if __name__ == '__main__':
    vp_start_gui()

