### lift programe by code lancer
import sys
import time 
from tkinter import *


class Lift:
    num_flors=10        # total numbers of flors
    ground_flore=0      # ground position 
    lift_position=0     # lift position
    dest_flor=0         # dfestination flore
    lift_speed=0.5      # lift speed in seconds between 0-1

    # moves lift up or down
    def move(self, dest, side):
        while True:
            if self.lift_position == dest:
                print("riched at destination",self.dest_flor)
                break
            if side=="UP":
                self.lift_position+=1
            elif side == "DOWN":
                self.lift_position-=1
            print(f"going {side} for ", self.lift_position)
            time.sleep(self.lift_speed)

    # GUI setting for lift
    def setting(self):
        root=Tk()
        root.geometry("400x300")
        root.title("Python Elevator")
        root.resizable(0,0)

        flor_var=StringVar()
        flor_var.set(str(self.num_flors))

        speed_var=StringVar()
        speed_var.set((self.lift_speed)*10)

        def saveSett():
            self.num_flors=int(flor_var.get())
            self.lift_speed=int(speed_var.get())/10
            root.destroy()

        frame1=LabelFrame(root, text="flor setting")
        frame1.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        Label(frame1, text="Number of Flors").grid(row=0, column=0, padx=10, pady=10)
        noFlor=Entry(frame1, textvariable=flor_var).grid(row=0, column=1, padx=10, pady=10)

        frame2=LabelFrame(root, text="lift speed")
        frame2.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        speed=Scale(frame2, from_=0, to=10, orient=HORIZONTAL, variable=speed_var)
        speed.pack(fill=X)

        Button(root, text="Save Settings", command=saveSett).pack(fill=X, pady=20, padx=10)

        root.mainloop()
    
    # starting point of program
    def start(self):
        while True:
            self.dest_flor=int(input(f"Enter destination flor({str(self.lift_position)}/{str(self.num_flors)}) : "))
            if self.dest_flor == 100:
                self.setting()
            elif self.dest_flor == 000:
                print("out of service ")
                sys.exit()
            elif self.dest_flor > self.num_flors:
                print("out of flores")
                continue
            elif self.dest_flor == self.lift_position:
                pass
            elif self.dest_flor <= self.lift_position:
                self.move(self.dest_flor, side="DOWN")
            elif self.dest_flor >= self.lift_position:
                self.move(self.dest_flor, side="UP")
            


if __name__=="__main__":
    lift=Lift()
    lift.start()

