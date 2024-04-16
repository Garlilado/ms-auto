from airtest.core.api import *
import tkinter as tk
from tkinter import ttk
from utils import check_connection, add_to_accountlist
from globals import DEVICES_NAMES
from player import *
from ui_globals import *


ST.OPDELAY = 0.5
ST.CVSTRATEGY = ["mstpl", "sift"]

# Setup the test environment
auto_setup(__file__)

root.grid_rowconfigure(0, weight=0)  # Allow the first row to expand when the window size changes
root.grid_rowconfigure(1, weight=1)  # Allow the second row to expand more when the window size changes
root.grid_columnconfigure(0, weight=1)  # Allow the column to expand when the window size changes

# ---------------------------------Arrange the status Notebook----------------------------------
status_frm.grid(sticky='nsew')  # Make the frame fill the window
status_notebook.add(status_frm, text='主号组连接')
status_notebook.grid(column=0, row=0, sticky='nsew')  # Add the first Notebook to the grid
status_notebook_title.grid(column=0, row=0)  # Place the title at the top of the grid
refresh_button.grid(column=1, row=0)  # Place the refresh button at the top of the grid
acc_choose_header.grid(column=0, row=1, sticky='nsew')  # Place the title at the top of the grid
acc_name_header.grid(column=1, row=1, sticky='nsew')  # Place the title at the top of the grid
dev_status_header.grid(column=2, row=1, sticky='nsew')  # Place the title at the top of the grid

connection_status = check_connection(status_frm, accountlist=accountlist, holder_combobox=holder_combobox)  # Call the check function to initialize the connection status

for i in range(4):
    var = tk.BooleanVar()
    var.set(connection_status[i])  # Set the initial value to True
    vars.append(var)
    state = 'normal' if connection_status[i] else 'disabled'  # Set the state based on the connection status
    chk = tk.Checkbutton(status_frm, text='', variable=var, command=lambda account=keys[i], var=var, accountlist=accountlist, holder_combobox=holder_combobox: add_to_accountlist(account, var, accountlist, holder_combobox), state=state)
    chk.grid(column=0, row=i+2, sticky='nsew')  # Make the checkbox fill the cell    
    checkbuttons.append(chk)  # Add the Checkbutton to the list
    lbl = tk.Label(status_frm, text=DEVICES_NAMES[i])
    lbl.grid(column=1, row=i+2, sticky='nsew')  # Make the label fill the cell

for i in range(3):
    status_frm.grid_columnconfigure(i, weight=1)  # Allow the columns to expand when the window size changes

# ---------------------------------Arrange Option Notebook----------------------------------
option_notebook.add(stage_frm, text='打本')
option_notebook.add(friendship_frm, text='羁绊')
option_notebook.grid(column=0, row=1, sticky='nsew')  # Add the second Notebook to the grid
map_choose_frm.grid(column=0, row=0, sticky="nsew")  # Make the frame fill the window
map_label.grid(column=0, row=0, sticky="nsew")  # Add the Label to the grid
map_choose_combobox.grid(column=1, row=0, padx=(0, 20), sticky="nsew")  # Add the Combobox to the grid
run_times_label.grid(column=2, row=0, sticky="nsew")  # Add the Label to the grid with a horizontal padding of 10 pixels
run_times_entry.grid(column=3, row=0, padx=(0, 20), sticky="nsew")  # Add the Entry to the grid with a horizontal padding of 10 pixels
holder_label.grid(column=5, row=0, sticky="nsew")  # Add the Label to the grid
holder_combobox.grid(column=6, row=0, sticky="nsew")  # Add the Combobox to the grid
selectable_frm.grid(column=0, row=1, sticky="nsew")  # Make the frame fill the window
selectable_frm_title.grid(column=0, row=0)  # Add the title to the grid
resurrection_chk.grid(column=0, row=1, sticky='nsew')

start_frm.grid(column=0, row=2, sticky="nsew")
auto_run_button.grid(column=0, row=0, sticky='nsew', padx=150, pady=10)
multi_player_auto_run_button.grid(column=0, row=1, sticky='nsew', padx=150, pady=10)
start_button.grid(column=1, row=0, sticky='nsew')

root.mainloop()