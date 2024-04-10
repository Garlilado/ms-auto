from airtest.core.api import *
from player import *
import utils
import argparse
import subprocess
import sys


ST.OPDELAY = 0.5
ST.CVSTRATEGY = ["mstpl", "sift"]

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--holder-start", help="Specify which account to start to choose map")
    # parser.add_argument("--players", help="Specify the amount of player")
    parser.add_argument("--round-hold", help="Specify if hold the room round or not")
    parser.add_argument("--join", help="Only join the room, internal use only")
    parser.add_argument("--pass-stage", help="Pass the stage, internal use only")
    parser.add_argument("--auto-pass", help="Auto pass the stage", action="store_true")
    parser.add_argument("--map", help="Specify the map to play")
    args = parser.parse_args()
    
    # Setup the test environment
    auto_setup(__file__)

    # Create accounts
    acc0 = Account("Android://127.0.0.1:5037/emulator-5554", True, idx= 0)
    acc1 = Account("Android://127.0.0.1:5037/emulator-5556", True, idx= 1)
    acc2 = Account("Android://127.0.0.1:5037/emulator-5558", True, idx= 2)
    acc3 = Account("Android://127.0.0.1:5037/emulator-5560", True, idx= 3)
    
    accountList = [acc0, acc1, acc2, acc3]
    # accountList = [acc1, acc2, acc3]
    
    # Only join the room
    if args.join:
        for acc in accountList:
            if acc.idx == int(args.join):
                acc.join()
                break
    elif args.pass_stage:
        for acc in accountList:
            if acc.idx == int(args.pass_stage):
                acc.pass_level()
                break
    elif args.auto_pass:
        utils.multiplayer_pass_stage(accountList)
    else:
        # Set the holder account
        for acc in accountList:
            if acc.idx == int(args.holder_start):
                acc.holder = True
                holder_acc = acc
                # Move holder to the first position
                accountList.insert(0, accountList.pop(accountList.index(acc)))
                break
        
        for i in range(1): #TODO: add final stage finished to break the loop
            if args.map == "Training":
                # Create a room
                if holder_acc.choose_map("Training"):
                    # Rest of the accounts join the room
                    processes = []
                    for acc in accountList[1:]:  # Skip the first account, which is the holder
                        p = subprocess.Popen(["python", "src/main.py", "--join", str(acc.idx)])
                        processes.append(p)

                # Wait for all processes to finish
                for p in processes:
                    exit_code = p.wait()
                    if exit_code != 0:
                        print(f"Process {p.pid} exited with code {exit_code}, exiting...")
                        sys.exit(exit_code)

                # Holder waits for the room to be full
                holder_acc.start_stage(len(accountList))
                
                utils.multiplayer_pass_stage(accountList)
            elif args.map == "Repeat":
                # Create a room
                if holder_acc.choose_map("Repeat"):
                    # Rest of the accounts join the room
                    processes = []
                    for acc in accountList[1:]:  # Skip the first account, which is the holder
                        p = subprocess.Popen(["python", "src/main.py", "--join", str(acc.idx)])
                        processes.append(p)

                # Wait for all processes to finish
                for p in processes:
                    exit_code = p.wait()
                    if exit_code != 0:
                        print(f"Process {p.pid} exited with code {exit_code}, exiting...")
                        sys.exit(exit_code)

                # Holder waits for the room to be full
                holder_acc.start_stage(len(accountList))
                
                utils.multiplayer_pass_stage(accountList)
