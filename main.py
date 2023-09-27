import tkinter as tk


def is_valid_input(p):
    # This function checks if the input is a valid float between 0 and 100, or an empty string
    if p == "":
        return True
    try:
        value = float(p)
        return 0 <= value <= 100
    except ValueError:
        return False


def percentage_calculator(english, sub1, sub2, sub3, sub4, sub5):
    # this function calculates the percentage using eng+best 4 and returns it
    sub_marks = [sub1, sub2, sub3, sub4, sub5]
    sub_marks.sort(reverse=True)
    sub_marks_without_last = sub_marks[:-1]
    total = english + sum(sub_marks_without_last)
    percentage = total / 5
    return percentage


def get_user_input():
    english_marks = float(entries["English"].get())
    sub1_marks = float(entries["Dzongkha"].get())
    sub2_marks = float(entries["Che/Comm/Geo"].get())
    sub3_marks = float(entries["Phy/Acc/His"].get())
    sub4_marks = float(entries["IT"].get())
    sub5_marks = float(entries["Math/Biology"].get())
    result_label.config(
        text="Percentage: {:.2f}%".format(
            percentage_calculator(english_marks, sub1_marks, sub2_marks, sub3_marks, sub4_marks, sub5_marks)))


# Create the main application window
app = tk.Tk()
app.title("Class 12 Percentage Calculator")

# Set the window size (width x height)
app.geometry("400x400")

# Create labels and entry widgets for user input
subjects = ["English", "Dzongkha", "Che/Comm/Geo", "Phy/Acc/His", "IT", "Math/Biology"]
entries = {}

for subject in subjects:
    label = tk.Label(app, text=f"Enter your {subject} Marks:")
    label.pack()

    entry = tk.Entry(app, validate="key", validatecommand=(app.register(is_valid_input), "%P"))
    entry.pack()

    entries[subject] = entry

# Create a button to submit the input
submit_button = tk.Button(app, text="Calculate", command=get_user_input)
submit_button.pack()

# Create a label to display the result
result_label = tk.Label(app, text="")
result_label.pack()

# Start the main event loop
app.mainloop()
