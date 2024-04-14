from airtest.core.api import *
from globals import DEVICES
import subprocess
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from player import Account

def multiplayer_pass_stage(accountList: list):
    """
    This function is used to pass the stage in multiplayer mode. 
    It starts a new process for each account in the provided list, 
    passing the stage for each account concurrently. 
    If any of the processes exit with a non-zero status code, 
    indicating an error, the function will print an error message 
    and exit the main program with the same status code.

    Args:
        accountList (list): A list of Account objects representing 
                             the accounts that will pass the stage.
    """
    # pass the level
    # All accounts pass the stage
    processes = []
    for acc in accountList:
        p = subprocess.Popen(["python", "src/main.py", "--pass-stage", str(acc.idx)])
        processes.append(p)

    # Wait for all processes to finish
    for p in processes:
        exit_code = p.wait()
        if exit_code != 0:
            print(f"Process {p.pid} exited with code {exit_code}, exiting...")
            sys.exit(exit_code)

def auto_pass_stage(holder:str, button: tk.Button):
    """Automatically pass the stage for the given account holder.

    Args:
        holder (str): The name of the account holder.
        button (tk.Button): The button that triggers the function.
    """
    button.after(100, button.config, {'state': tk.DISABLED})  # Add a delay before disabling the button
    try: 
        if not holder:
            messagebox.showerror("错误", "请选择房主")
            return
        hodler_acc = Account(DEVICES[holder], False, True)
        hodler_acc.pass_level()
    finally:
        button.after(100, button.config, {'state': tk.NORMAL})

def add_to_accountlist(account:str, var: tk.BooleanVar, accountlist: list, holder_combobox: ttk.Combobox = None):
    """
    Add or remove an account from the account list based on the state of a checkbox.

    Args:
        account (str): The account associated with the Checkbutton.
        var (tk.BooleanVar): The variable associated with the Checkbutton. Its value is True when the Checkbutton is checked, and False otherwise.
        accountlist (list): The list of accounts. This function will add the account to this list when the Checkbutton is checked, and remove it when the Checkbutton is unchecked.
        holder_combobox (ttk.Combobox): The Combobox that holds the account list.
    """
    holder_combobox.set("")
    if var.get():
        accountlist.append(account)
    else:
        accountlist.remove(account)
    holder_combobox["values"] = accountlist
    print(accountlist)  # Print the accountlist whenever a checkbox is checked or unchecked


def check_connection(frm: ttk.Frame, checkbuttons: list = None, accountlist: list = None, vars: list = None, holder_combobox: ttk.Combobox = None)->list:
    """
    Check the connection status of each device and update the GUI.

    Args:
        frm (ttk.Frame): The frame in which the connection status indicators are displayed.
        checkbuttons(list): check buttons for each device.
        accountlist(list): The list of accounts to be onboard.
        vars(list): The list of variables associated with the Checkbuttons.
        holder_combobox (ttk.Combobox): The Combobox that holds the account list.
    
    Returns:
        list: The connection status of the devices.
    """
    connection_status = []
    accountlist.clear()
    devices = list(DEVICES.keys())
    device_urls = DEVICES.values()
    holder_combobox.set("")
    for device_url in device_urls:
        try:
            connect_device(device_url)
            connection_status.append(True)  # Device is connected
        except:
            connection_status.append(False)  # Device is not connected
    for i in range(len(DEVICES)):
        color = 'green' if connection_status[i] else 'yellow'
        cnv = tk.Canvas(frm, width=20, height=20)
        cnv.grid(column=2, row=i+2)  # Make the canvas fill the cell
        cnv.create_oval(5, 5, 15, 15, fill=color)
        if checkbuttons is not None:
            state = 'normal' if connection_status[i] else 'disabled'  # Set the state based on the connection status
            checkbuttons[i].config(state=state)  # Update the state of the Checkbutton
            vars[i].set(connection_status[i])
        if connection_status[i]:
            accountlist.append(devices[i])
            print("Account list: ", accountlist)
            holder_combobox["values"] = accountlist
    return connection_status
