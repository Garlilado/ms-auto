import tkinter as tk
from tkinter import ttk
from globals import DEVICES, DEVICES_NAMES
import utils

root = tk.Tk()
root.title("MS Auto")
root.geometry("700x700")  # Set the window size to 700x700 pixels

accountlist = []
vars = []
checkbuttons = []  # Create a list to store the Checkbuttons
# map = ""
keys = list(DEVICES.keys())

# First Notebook
status_notebook = ttk.Notebook(root)
status_frm = ttk.Frame(status_notebook, padding=10)
# Title of the first Notebook
status_notebook_title = tk.Label(status_frm, text="Device List", font=("Arial", 20))
# Refresh button
refresh_button = tk.Button(status_frm, text="刷新", command=lambda: utils.check_connection(status_frm, checkbuttons, accountlist, vars, holder_combobox))
# Account choose header
acc_choose_header = tk.Label(status_frm, text="选择账号", font=("Arial", 14), borderwidth=1, relief='solid')
# Device name header
acc_name_header = tk.Label(status_frm, text="账号名称", font=("Arial", 14), borderwidth=1, relief='solid')
# Device status header
dev_status_header = tk.Label(status_frm, text="设备状态", font=("Arial", 14), borderwidth=1, relief='solid')

# Second Notebook
option_notebook = ttk.Notebook(root)
# Frames for the second Notebook
stage_frm = ttk.Frame(option_notebook)
friendship_frm = ttk.Frame(option_notebook)
# Map choose frame
map_choose_frm = ttk.Frame(stage_frm)
# Map choose label and Combobox
map_label = tk.Label(map_choose_frm, text="脚本:")
map_choose_combobox = ttk.Combobox(map_choose_frm, values=["训练", "重复", "塔"])
# Run times label and Entry
run_times_label = tk.Label(map_choose_frm, text="跑本次数:")
run_times_entry = tk.Entry(map_choose_frm)
# Holder label and Combobox
holder_label = tk.Label(map_choose_frm, text="房主:")
holder_combobox = ttk.Combobox(map_choose_frm, values=accountlist)
# Selectable frame
selectable_frm = ttk.Frame(stage_frm)
# Selectable frame title
selectable_frm_title = tk.Label(selectable_frm, text="可选项", font=("Arial", 14))
# Selectable checkbox
resurrection_chk = tk.Checkbutton(selectable_frm, text='复活')

# Starter
start_frm = ttk.Frame(stage_frm)
auto_run_button = tk.Button(start_frm, text="房主自动跑图(1x)", command=lambda: utils.auto_pass_stage(holder_combobox.get(), auto_run_button))