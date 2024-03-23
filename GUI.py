import binary_float_add as bin
import tkinter as tk
from tkinter import ttk
print('Tkinter Successfully Imported')

# Variables
input1 = 0      # 1st Operand Value
exp1 = 0        # 1st Operand Exponent

input2 = 0      # 2nd Operand Value
exp2 = 0        # 2nd Operand Exponent

numBits = 0     # Number of Bits

sum = 0         # Sum

# Output Variables
global initA
global initB
global initAexp
global initBexp

global step1A_OP    # Step 1
global step1B_OP
global step1A_OPexp
global step1B_OPexp 

global step2A_OP    # Step 2
global step2B_OP
global step2A_OPexp
global step2B_OPexp 

global step3_OP     # Step 3
global step3_OPexp

global step4_OP     # Step 5
global step4_OPexp

global final_OP     # Final Answer
global final_OPexp


# Wrapping Label
class WrapLabel(tk.Label):
    '''a type of Label that automatically adjusts the wrap to the size'''
    def __init__(self, master=None, **kwargs):
        tk.Label.__init__(self, master, **kwargs)
        self.bind('<Configure>', lambda e: self.config(wraplength=self.winfo_width()))

# Main Window
root = tk.Tk()
root.title("IEEE-754 Binary-32 Floating Point Operation")
root.geometry("960x600")
root.grid_columnconfigure((0), weight=1)

# Title
title = tk.Label(
    root,
    text="IEEE-754 Binary-32 Floating Point Operation",
    font = ("Times New Roman Bold", 25),
    fg = 'black'
)
title.grid(row=0, column=0)

# Program Description
desc = WrapLabel(
    root,
    text="Enter two binary floating point numbers, input the number of digits for the final answer, " + 
    "then choose to either round to the nearest even, or use Guard-Round-Sticky bits. " + 
    "The program will add the two operands, output steps of the solution, then show the sum.",
    font = ("Times New Roman", 14),
    fg = 'black'
)
desc.grid(row=1, column=0)

# Input Frame
inFrame = tk.Frame(root)
inFrame.grid(row=2, column=0)
inFrame.grid_columnconfigure((0,1,2,3,4,5), weight=1)

#Operand 1: Warning
opA_Warn = tk.Label(
    inFrame,
    text="----------------------",
    font = ("Consolas", 10),
    fg = 'red'
)
opA_Warn.grid(row=0, column=0)

# Operand 1: Text
opA_Txt = WrapLabel(
    inFrame,
    text="Operand A",
    font = ("Times New Roman", 14),
    fg = 'black'
)
opA_Txt.grid(row=0, column=1)

# Operand 1: Input
opA_Input = tk.Entry(
    inFrame,
    font = ("Times New Roman", 14),
    fg = 'black'
)
opA_Input.insert(0, '1.000')
opA_Input.grid(row=0, column=2)

# Operand 1: Exponent Text
opA_expTxt = WrapLabel(
    inFrame,
    width = 6,
    text="x 2^",
    font = ("Times New Roman", 14),
    fg = 'black'
)
opA_expTxt.grid(row=0, column=3)

# Operand 1: Exponent Value
opA_expInput = tk.Entry(
    inFrame,
    width = 4,
    font = ("Times New Roman", 14),
    fg = 'black'
)
opA_expInput.insert(0, '0')
opA_expInput.grid(row=0, column=4)

#Operand 1: Exponent Warning
opA_expWarn = tk.Label(
    inFrame,
    text="---------------------",
    font = ("Consolas", 10),
    fg = 'red'
)
opA_expWarn.grid(row=0, column=5)

#Operand 2: Warning
opB_Warn = tk.Label(
    inFrame,
    text="---------------------",
    font = ("Consolas", 10),
    fg = 'red'
)
opB_Warn.grid(row=1, column=0)

# Operand 2: Text
opB_Txt = WrapLabel(
    inFrame,
    text="Operand B",
    font = ("Times New Roman", 14),
    fg = 'black'
)
opB_Txt.grid(row=1, column=1)

# Operand 2: Input
opB_Input = tk.Entry(
    inFrame,
    font = ("Times New Roman", 14),
    fg = 'black'
)
opB_Input.insert(0, '1.000')
opB_Input.grid(row=1, column=2)

# Operand 2: Exponent Text
opB_expTxt = WrapLabel(
    inFrame,
    width = 6,
    text="x 2^",
    font = ("Times New Roman", 14),
    fg = 'black'
)
opB_expTxt.grid(row=1, column=3)

# Operand 2: Exponent Value
opB_expInput = tk.Entry(
    inFrame,
    width = 4,
    font = ("Times New Roman", 14),
    fg = 'black'
)
opB_expInput.insert(0, '0')
opB_expInput.grid(row=1, column=4)

#Operand 2: Exponent Warning
opB_expWarn = tk.Label(
    inFrame,
    text="---------------------",
    font = ("Consolas", 10),
    fg = 'red'
)
opB_expWarn.grid(row=1, column=5)

# Number of Bits: Warning
numBits_Warn = tk.Label(
    inFrame,
    text="---------------------",
    font = ("Consolas", 10),
    fg = 'red'
)
numBits_Warn.grid(row=2, column=0)

# Number of Bits: Text
numBits_Txt = WrapLabel(
    inFrame,
    text="Number of Bits",
    font = ("Times New Roman", 14),
    fg = 'black'
)
numBits_Txt.grid(row=2, column=1)

# Number of Bits: Input
numBits_Input = tk.Entry(
    inFrame,
    font = ("Times New Roman", 14),
    fg = 'black'
)
numBits_Input.insert(0, 1)
numBits_Input.grid(row=2, column=2)

# Rounding Choice: Text
round_Txt = WrapLabel(
    inFrame,
    text="Rounding",
    font = ("Times New Roman", 14),
    fg = 'black'
)
round_Txt.grid(row=3, column=1)

# Rounding Choice: Dropdown Options
clicked = tk.StringVar()
clicked.set("Nearest Ties To Even")
rndChoice = ttk.Combobox(
    inFrame, 
    width = 26, 
    state = "readonly",
    textvariable=clicked
)
rndChoice['values'] = ["Nearest Ties To Even", "Guard, Round, Sitcky Bits"]
rndChoice.grid(row = 3, column = 2)

# Step 1: Normalize Inputs
step1 = WrapLabel(
    inFrame,
    text="",
    width = 25,
    font = ("Times New Roman", 14),
    fg = 'red'
)
step1.grid(row=5, column=1)

# Step 1: Normalized Input 1
step1OpA = WrapLabel(
    inFrame,
    text="",
    width = 25,
    font = ("Times New Roman", 14),
    fg = 'black'
)
step1OpA.grid(row=5, column=2)

# Step 1: Normalized Input 2
step1OpB = WrapLabel(
    inFrame,
    text="",
    width = 25,
    font = ("Times New Roman", 14),
    fg = 'black'
)
step1OpB.grid(row=6, column=2)

# Step 2: RNE or GRS
step2 = WrapLabel(
    inFrame,
    text="",
    width = 25,
    font = ("Times New Roman", 14),
    fg = 'red'
)
step2.grid(row=7, column=1)

# Step 2: RNE/GRS Input 1
step2OpA = WrapLabel(
    inFrame,
    text="",
    width = 25,
    font = ("Times New Roman", 14),
    fg = 'black'
)
step2OpA.grid(row=7, column=2)

# Step 2: RNE/GRS Input 2
step2OpB = WrapLabel(
    inFrame,
    text="",
    width = 25,
    font = ("Times New Roman", 14),
    fg = 'black'
)
step2OpB .grid(row=8, column=2)

# Step 3: Addition Text
step3 = WrapLabel(
    inFrame,
    text="",
    width = 25,
    font = ("Times New Roman", 14),
    fg = 'red'
)
step3.grid(row=9, column=1)

# Step 3: Addition Value
step3_Val = WrapLabel(
    inFrame,
    text="",
    width = 25,
    font = ("Times New Roman", 14),
    fg = 'black'
)
step3_Val.grid(row=9, column=2)

# Step 4: Normalize Text
step4 = WrapLabel(
    inFrame,
    text="",
    width = 25,
    font = ("Times New Roman", 14),
    fg = 'red'
)
step4.grid(row=10, column=1)

# Step 4: Normalize Value
step4_Val = WrapLabel(
    inFrame,
    text="",
    width = 25,
    font = ("Times New Roman", 14),
    fg = 'black'
)
step4_Val.grid(row=10, column=2)

# Step 5: Round Sum Text
step5 = WrapLabel(
    inFrame,
    text="",
    width = 25,
    font = ("Times New Roman Bold", 14),
    fg = 'green'
)
step5.grid(row=11, column=1)

# Step 5: Round Value
step5_Val = WrapLabel(
    inFrame,
    text="",
    width = 25,
    font = ("Times New Roman Bold", 14),
    fg = 'green'
)
step5_Val.grid(row=11, column=2)

# Output Text File Function
def output_txtFile():
    with open("Output.txt", "w") as text_file:
        text_file.write(f"Initial Inputs: \t\t{initA} x 2^{initAexp}" + 
                        f"\n\t\t\t\t\t\t{initB} x 2^{initBexp}" + 
                        f"\n\nNormalized Inputs: \t\t{step1A_OP} x 2^{step1A_OPexp}" + 
                        f"\n\t\t\t\t\t\t{step1B_OP} x 2^{step1B_OPexp}" + 
                        f"\n\nRounded Inputs: \t\t{step2A_OP} x 2^{step2A_OPexp}" + 
                        f"\n\t\t\t\t\t\t{step2B_OP} x 2^{step2B_OPexp}"+ 
                        f"\n\nInitial Sum: \t\t\t{step3_OP} x 2^{step3_OPexp}"+ 
                        f"\n\nNormalized Sum: \t\t{step4_OP} x 2^{step4_OPexp}"+ 
                        f"\n\nFinal Answer: \t\t\t{final_OP} x 2^{final_OPexp}"
                        )

# Output Text Button
outputBtn = tk.Button(
    inFrame,
    text="Output to Text File",
    font=("Times New Roman", 12),
    command=output_txtFile   
)

# Submit Button Function
def submit():
    global flag1 
    flag1 = False
    global flag2
    flag2 = False
    global outflag
    outflag = False

    # Reset Error Messages
    opA_Warn.config(text="                              ") 
    opB_Warn.config(text="                              ") 
    opA_expWarn.config(text="                              ")
    opB_expWarn.config(text="                              ")
    numBits_Warn.config(text="                              ")

    # Validation Score
    vScore = 0

    # Validate 3rd Input
    input1 = opA_Input.get()
    check1 = bin.validate_binary(input1)
    if(check1):
        vScore+=1
    else:
        opA_Warn.config(text="Enter a binary floating point ")

    # Validate 2nd Input
    input2 = opB_Input.get()
    check2 = bin.validate_binary(input2)
    if(check2):
        vScore+=1
    else:
        opB_Warn.config(text="Enter a binary floating point ")

    # Validate 1st Input Exponent
    exp1 = opA_expInput.get()
    try:
        int(exp1)        
        vScore+=1
    except ValueError:
        opA_expWarn.config(text="Enter a whole decimal number! ")
        

    # Validate 2nd Input Exponent
    exp2 = opB_expInput.get()
    try:
        int(exp2)        
        vScore+=1
    except ValueError:
        opB_expWarn.config(text="Enter a whole decimal number! ")
        
    # Validate Number of Digits
    numBits = numBits_Input.get()
    try:
        int(numBits)
        if(int(numBits) > 0):
            vScore+=1
        else:
            numBits_Warn.config(text="Only a POSITIVE whole decimal!")   
    except ValueError:
        numBits_Warn.config(text="Enter a whole decimal number! ")
    
    # Perform Operation
    if(vScore == 5):
        # Store Initial Input 1
        global initA
        initA = input1
        global initAexp
        initAexp = exp1
        
        # Store Initial Input 2
        global initB
        initB = input2
        global initBexp
        initBexp = exp1

        if input1[0] == '-':
            flag1 = True
            input1 = input1[1:]
        if input2[0] == '-':
            flag2 = True
            input2 = input2[1:]

        # Step 1: Normalize Inputs
        input1, input2, exp1, exp2 = bin.match_inputs(input1, input2, int(exp1), int(exp2))
        step1.config(text="Normalize Inputs: ")
        if flag1: input1 = "-" + input1
        if flag2: input2 = "-" + input2
        str1 = "{val} x 2^{exp}".format(val = input1, exp = exp1)
        str2 = "{val} x 2^{exp}".format(val = input2, exp = exp2)
        step1OpA.config(text=str1)
        step1OpB.config(text=str2)

        # Store Rounded Inputs
        global step1A_OP    
        step1A_OP = input1
        global step1B_OP    
        step1B_OP = input2

        # Store Rounded Exponents
        global step1A_OPexp    
        step1A_OPexp = exp1
        global step1B_OPexp    
        step1B_OPexp = exp2

        if input1[0] == '-':
            flag1 = True
            input1 = input1[1:]
        if input2[0] == '-':
            flag2 = True
            input2 = input2[1:]

        # Step 2: "Nearest Ties To Even", "Guard, Round, Sitcky Bits"
        if(clicked.get()=="Nearest Ties To Even"):
            input1 = bin.rounding(input1, int(numBits))
            input2 = bin.rounding(input2, int(numBits))
            if flag1: input1 = "-" + input1
            if flag2: input2 = "-" + input2
            step2.config(text="Rounded Inputs: ")            
            str1 = "{val} x 2^{exp}".format(val = input1, exp = exp1)
            str2 = "{val} x 2^{exp}".format(val = input2, exp = exp2)
            step2OpA.config(text=str1)
            step2OpB.config(text=str2)

        else:            
            input1 = bin.transform_to_GRS(input1, int(numBits))
            input2 = bin.transform_to_GRS(input2, int(numBits))
            step2.config(text="GRS Inputs: ")   
            if flag1: input1 = "-" + input1
            if flag2: input2 = "-" + input2         
            str1 = "{val} x 2^{exp}".format(val = input1, exp = exp1)
            str2 = "{val} x 2^{exp}".format(val = input2, exp = exp2)
            step2OpA.config(text=str1)
            step2OpB.config(text=str2)            

        # Store Rounded Inputs
        global step2A_OP    # Step 2
        step2A_OP = input1
        global step2B_OP    # Step 2
        step2B_OP = input2

        # Store Rounded Exponents
        global step2A_OPexp    # Step 2
        step2A_OPexp = exp1
        global step2B_OPexp    # Step 2
        step2B_OPexp = exp2

        # Step 3: Get Sum
        sum = bin.binary_addition(input1, input2)
        step3.config(text="Initial Sum: ")            
        step3_Val.config(text="{val} x 2^{exp}".format(val = sum, exp = exp1))

        # Store Sum and Exponent
        global step3_OP
        step3_OP = sum
        global step3_OPexp
        step3_OPexp = exp1

        # Step 4: Normalize Sum
        if sum[0] == '-':
            outflag = True
            sum = sum[1:]

        normal, expf = bin.normalize_binary(sum, exp1)
        step4.config(text="Normalized Sum: ")
        if outflag: normal = "-" + normal
        str="{val} x 2^{exp}".format(val = normal, exp = expf)
        step4_Val.config(text=str)

        # Store Normal and Exponent
        global step4_OP
        step4_OP = normal
        global step4_OPexp
        step4_OPexp = expf

        if normal[0] == '-':
            outflag = True
            normal = normal[1:]

        # Step 5: Round
        answer = bin.rounding(normal, int(numBits))
        if(answer.count('.')==2): answer = answer.replace('.', '', 1)
        step5.config(text="Final Answer: ") 
        str="{val} x 2^{exp}".format(val = answer, exp = expf)  
        if outflag: str = "-" + str
        step5_Val.config(text=str)

        if outflag: answer = "-" + answer

        # Store Normal and Exponent
        global final_OP
        final_OP = answer
        global final_OPexp
        final_OPexp = expf

        # Place Button
        outputBtn.grid(row=12, column=2)

# Submit Button
sbmtBtn = tk.Button(
    inFrame,
    text="Submit",
    font=("Times New Roman", 12),
    command=submit   
)
sbmtBtn.grid(row=4, column=2)

# Start Window
root.mainloop()