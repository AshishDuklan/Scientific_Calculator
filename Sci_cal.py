# Importing the library
import tkinter
import math
import numpy as np

def open_matrix_menu():
    root1 = tkinter.Tk()
    top = tkinter.Toplevel(root1)
    top.title("Matrix calculator")
    top.geometry("400x300+100+100")
    top.config(bg="black")

    entry = tkinter.Entry(root1, font=("arial", 20, "bold"), bg="black", fg="white", bd=10, width=20)
    entry.grid(row=0, column=0, columnspan=8)

    # Buttons list
    button_list = ["Add", "Sub", "Multiply", "Transpose", "Inverse", "Eigenvalues"]
    r = 1
    c = 0

    # Loop to get the buttons on the matrix window
    for i in button_list:
        # Buttons
        button = tkinter.Button(root1, width=10, height=4, bd=2, text=i, bg="black", fg="white",
                                font=("arial", 16, "bold"), command=lambda button=i: click(button))
        button.grid(row=r, column=c, pady=1)
        c += 1
        if c > 2:
            r += 1
            c = 0

    def click(val1):
        e1 = entry.get()

        try:
            if val1 in ["Transpose", "Inverse","Eigenvalues"]:
                matrix_input(val1)

            elif val1 in ["Add", "Sub", "Multiply"]:
                matrix_input(val1, require_matrix_b=True)

            else:
                entry.insert("end", val1)
                return

        except SyntaxError:
            pass

    def matrix_input(operation, require_matrix_b=False):
        top1 = tkinter.Toplevel(top)
        top1.title(f"Matrix {operation}")
        top1.geometry("375x365+100+100")
        top1.config(bg="black")

        label1 = tkinter.Label(top1, text=f"Enter dimensions of Matrix A:", font=("arial", 12, "bold"))
        label1.grid(row=0, column=0, columnspan=2, pady=10)

        entry_rows_A = tkinter.Entry(top1)
        entry_rows_A.grid(row=1, column=0, padx=10)

        entry_columns_A = tkinter.Entry(top1)
        entry_columns_A.grid(row=1, column=1, padx=10)

        label2 = tkinter.Label(top1, text=f"Enter elements of Matrix A (comma-separated):", font=("arial", 12))
        label2.grid(row=2, column=0, columnspan=2, pady=10)

        entry_elements_A = tkinter.Entry(top1, width=50)
        entry_elements_A.grid(row=3, column=0, columnspan=2, padx=10)

        if require_matrix_b:
            label3 = tkinter.Label(top1, text=f"Enter dimensions of Matrix B:",
                                   font=("arial", 12, "bold"))
            label3.grid(row=4, column=0, columnspan=2, pady=10)

            entry_rows_B = tkinter.Entry(top1)
            entry_rows_B.grid(row=5, column=0, padx=10)

            entry_columns_B = tkinter.Entry(top1)
            entry_columns_B.grid(row=5, column=1, padx=10)

            label4 = tkinter.Label(top1, text=f"Enter elements of Matrix B (comma-separated):", font=("arial", 12))
            label4.grid(row=6, column=0, columnspan=2, pady=10)

            entry_elements_B = tkinter.Entry(top1, width=50)
            entry_elements_B.grid(row=7, column=0, columnspan=2, padx=10)

        result_label = tkinter.Label(top1, text="")
        result_label.grid(row=8, column=0, columnspan=2, pady=10)

        def perform_operation():
            rows_A = int(entry_rows_A.get())
            columns_A = int(entry_columns_A.get())
            matrix_A = np.matrix(eval(entry_elements_A.get())).reshape((rows_A, columns_A))

            if require_matrix_b:
                rows_B = int(entry_rows_B.get())
                columns_B = int(entry_columns_B.get())
                matrix_B = np.matrix(eval(entry_elements_B.get())).reshape((rows_B, columns_B))

            if operation == "Add" and require_matrix_b:
                result = matrix_A + matrix_B  # Perform addition

            elif operation == "Sub" and require_matrix_b:
                result = matrix_A - matrix_B  # Perform subtraction

            elif operation == "Multiply" and require_matrix_b:
                result = matrix_A * matrix_B  # Perform multiplication

            elif operation == "Transpose":
                result = np.transpose(matrix_A)  # Perform transpose

            elif operation == "Inverse":
                result = np.linalg.inv(matrix_A)  # Perform inverse

            elif operation == "Eigenvalues":
                eigenvalues = np.linalg.eigvals(matrix_A)
                result_label.config(text="Eigenvalues:\n" + str(eigenvalues))

            result_label.config(text="Result:\n" + str(result))

        operation_button = tkinter.Button(top1, text="Answer", command=perform_operation)
        operation_button.grid(row=9, column=0, columnspan=2, pady=10)

# To provide functionalities
def click(val):
    e = entry.get()  # getting the value
    ans = " "

    try:
        # To clear the last inserted text
        if val == "C":
            e = e[0:len(e) - 1]  # deleting the last entered value
            entry.delete(0, "end")
            entry.insert(0, e)
            return

        # To delete everything
        elif val == "CE":
            entry.delete(0, "end")

        # Square root
        elif val == "√":
            ans = math.sqrt(eval(e))

        # pi value
        elif val == "π":
            ans = math.pi

        # cos value
        elif val == "cosθ":
            ans = math.cos(math.radians(eval(e)))

        # sin value
        elif val == "sinθ":
            ans = math.sin(math.radians(eval(e)))

        # tan Value
        elif val == "tanθ":
            ans = math.tan(math.radians(eval(e)))

        # 2π value
        elif val == "2π":
            ans = 2 * math.pi

        # cosh value
        elif val == "cosh":
            ans = math.cosh(eval(e))

        # sinh value
        elif val == "sinh":
            ans = math.sinh(eval(e))

        # tanh value
        elif val == "tanh":
            ans = math.tanh(eval(e))

        # cube root value
        elif val == chr(8730):
            ans = eval(e) ** (1 / 2)

        # cube root value
        elif val == chr(8731):
            ans = eval(e) ** (1 / 3)

        # x to the power y
        elif val == "x\u02b8":
            entry.insert("end", "**")
            return

        # nCr value
        elif val == "nCr":
            values = e.split(" nCr ")
            if len(values) == 2:
                ans = math.comb(int(values[0]), int(values[1]))


        # nPr value
        elif val == "nPr":
            entry.insert("end", "P")
            return

        elif val == "=" and "P" in e:
            n, r = map(int, e.split("P"))
            ans = math.perm(n, r)

        # nCr value
        elif val == "nC'r":
            entry.insert("end", "C'")
            return
        elif val == "=" and "C'" in e:
            n, r = map(int, e.split("C'"))
            ans = math.comb(n, r)


        # cube value
        elif val == "x\u00B3":
            ans = eval(e) ** 3

        # square value
        elif val == "x\u00B2":
            ans = eval(e) ** 2

        # ln value
        elif val == "ln":
            ans = math.log2(eval(e))

        # deg value
        elif val == "deg":
            ans = math.degrees(eval(e))

        # radian value
        elif val == "rad":
            ans = math.radians(eval(e))

        # e value
        elif val == "e":
            ans = math.e

        # log10 value
        elif val == "log10":
            ans = math.log10(eval(e))

        # factorial value
        elif val == "x!":
            ans = math.factorial(eval(e))

        # division operator
        elif val == chr(247):
            entry.insert("end", "/")
            return

        elif val == "=":
            ans = eval(e)

        elif val == "Matrix":
            open_matrix_menu()

        else:
            entry.insert("end", val)
            return

        entry.delete(0, "end")
        entry.insert(0, ans)

    except SyntaxError:
        pass


# Created the object
root = tkinter.Tk()

# Setting the title and geometry
root.title("Scientific Calculator")
root.geometry("765x547+100+100")

# Setting the background color
root.config(bg="black")


# Entry field
entry = tkinter.Entry(root, font=("arial", 20, "bold"), bg="white", fg="black", bd=10, width=30)
entry.grid(row=0, column=0, columnspan=8)

# buttons list
button_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ", "nC'r", "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh", "nPr",
               "4", "5", "6", "*", chr(8730), chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", "7", "8", "9", chr(247), "ln", "deg",
               "rad", "e", "0", ".", "%", "=", "(", ")", "log10", "x!", "x","Matrix"]
r = 1
c = 0
# Loop to get the buttons on window
for i in button_list:
    # Buttons
    button = tkinter.Button(root, width=5, height=2, bd=2, text=i, bg="green", fg="white",
                            font=("arial", 18, "bold"), command=lambda button=i: click(button))
    button.grid(row=r, column=c, pady=1)
    c += 1
    if c > 8:
        r += 1
        c = 0

# Makes window on loop
root.mainloop()
