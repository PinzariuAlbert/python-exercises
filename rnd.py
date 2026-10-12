import tkinter as tk
from tkinter import *
from tkinter import ttk

def validate_number(value):
    if value in ("", "-"):
        return True
    try:
        float(value)
        return True
    except ValueError:
        return False


window = tk.Tk()
window.title("Mortar/Artillery calculator (Arma Reforger)")
window.resizable(False, False)

def limit_characters(new_value):
    return len(new_value) <= 5

validation = window.register(validate_number)
validate = window.register(limit_characters)


default_color = "light gray"

########################################################################

text0 = tk.Label(window, text="Weapon system")
text0.grid(row=0, column=0, padx=5, pady=10, sticky="ew")
text0.config(width=25, height=1)

mortar = ["M252", "2B14"]
opt0 = StringVar(value="Select weapon")

Mortar_dropdown = OptionMenu(window, opt0, *mortar)
Mortar_dropdown.grid(row=1, column=0, padx=2, pady=0, sticky="ew")
Mortar_dropdown.config(width=25, height=2, indicatoron=False)
Mortar_dropdown.configure(background=default_color)

########################################################################

text1 = tk.Label(window, text="Ammunition")
text1.grid(row=0, column=1, padx=5, pady=10, sticky="ew")
text1.config(width=25, height=1)

ammo_type_rus = [
    "High-explosive (O-832DU)",
    "Smoke (D-832DU)",
    "Flare (S-832S)"
]

ammo_type_us = [
    "High-explosive (M821)",
    "Smoke (M819)",
    "Flare (M853A1)"
]

opt1 = StringVar(value="Select ammunition")

Ammo_dropdown = OptionMenu(window, opt1, "")
Ammo_dropdown.grid(row=1, column=1, padx=2, pady=0, sticky="ew")
Ammo_dropdown.config(width=25, height=2, indicatoron=False)
Ammo_dropdown.configure(background=default_color)

########################################################################

def update_ammo(*args):
    selected_mortar = opt0.get()

    if selected_mortar == "M252":
        ammo_type = ammo_type_us
    elif selected_mortar == "2B14":
        ammo_type = ammo_type_rus
    else:
        ammo_type = []

    menu = Ammo_dropdown["menu"]
    menu.delete(0, "end")

    opt1.set("Select ammunition")

    for ammo in ammo_type:
        menu.add_command(
            label=ammo,
            command=lambda value=ammo: opt1.set(value)
        )

opt0.trace_add("write", update_ammo)

########################################################################

# BASICALLY you make a function do all the work instead of rewriting all the code over and over again
def bs_shit_fuck(rowCopy, textCopy):
    text8 = tk.Label(window, text=textCopy)
    text8.grid(row=rowCopy, column=3, padx=5, pady=10, sticky="w")
    text8.config(width=25, height=1)
################
text1 = tk.Label(window, text="Weapon system coordinates")
text1.grid(row=3, column=0, padx=5, pady=10, sticky="w")
text1.config(width=25, height=1)
mortar_x = tk.Entry(window, validate="key",
                    validatecommand=(validation, "%P"))
mortar_x.grid(row=4, column=0, padx=5, pady=0, sticky="ew")

text2 = tk.Label(window, text="Target coordinates")
text2.grid(row=3, column=1, padx=5, pady=10, sticky="w")
text2.config(width=25, height=1)
mortar_y = tk.Entry(window, validate="key",
                    validatecommand=(validation, "%P"))
mortar_y.grid(row=4, column=1, padx=5, pady=0, sticky="ew")

text6 = tk.Label(window, text="Weapon system elevation")
text6.grid(row=5, column=0, padx=5, pady=10, sticky="w")
text6.config(width=25, height=1)
target_elevation = tk.Entry(window, validate="key",
                    validatecommand=(validation, "%P"))
target_elevation.grid(row=6, column=0, padx=5, pady=0, sticky="ew")

text7 = tk.Label(window, text="Target elevation")
text7.grid(row=5, column=1, padx=5, pady=10, sticky="w")
text7.config(width=25, height=1)
wind_speed = tk.Entry(window, validate="key",
                    validatecommand=(validation, "%P"))
wind_speed.grid(row=6, column=1, padx=5, pady=0, sticky="ew")

text8 = tk.Label(window, text="Wind speed")
text8.grid(row=7, column=1, padx=5, pady=10, sticky="w")
text8.config(width=25, height=1)
wind_direction = tk.Entry(window, validate="key",
                    validatecommand=(validation, "%P"))
wind_direction.grid(row=8, column=1, padx=5, pady=0, sticky="ew")

text8 = tk.Label(window, text="Wind direction")
text8.grid(row=7, column=0, padx=5, pady=10, sticky="w")
text8.config(width=25, height=1)
wind_direction = tk.Entry(window, validate="key",
                    validatecommand=(validation, "%P"))
wind_direction.grid(row=8, column=0, padx=5, pady=0, sticky="ew")

Buttoncalculate = tk.Button(text="Calculate firing solution")

Buttoncalculate.grid(row=10, column=0, padx=5, pady=10, sticky="ew")
Buttoncalculate.configure(background=default_color)

bs_shit_fuck(0,"Elevation (6400):")
bs_shit_fuck(1,"Elevation (6000):")
bs_shit_fuck(2,"Elevation (360):")
bs_shit_fuck(3,"Azimuth (6400):")
bs_shit_fuck(4,"Azimuth (6000):")
bs_shit_fuck(5,"Azimuth (360):")
bs_shit_fuck(6,"Distance (meters):")
bs_shit_fuck(7,"Charge:")

text8 = tk.Label(window, text="___________________________________________")
text8.grid(row=2, column=0, padx=0, pady=10, sticky="e")
text8.config(width=25, height=1)

text8 = tk.Label(window, text="___________________________________________")
text8.grid(row=2, column=1, padx=0, pady=10, sticky="w")
text8.config(width=25, height=1)

text8 = tk.Label(window, text="___________________________________________")
text8.grid(row=9, column=0, padx=0, pady=10, sticky="e")
text8.config(width=25, height=1)

text8 = tk.Label(window, text="___________________________________________")
text8.grid(row=9, column=1, padx=0, pady=10, sticky="w")
text8.config(width=25, height=1)

text8 = tk.Label(window, text="N/A")
text8.grid(row=0, column=4, padx=0, pady=10, sticky="w")
text8.config(width=25, height=1)

text8 = tk.Label(window, text="N/A")
text8.grid(row=1, column=4, padx=0, pady=10, sticky="w")
text8.config(width=25, height=1)

text8 = tk.Label(window, text="N/A")
text8.grid(row=2, column=4, padx=0, pady=10, sticky="w")
text8.config(width=25, height=1)

text8 = tk.Label(window, text="N/A")
text8.grid(row=3, column=4, padx=0, pady=10, sticky="w")
text8.config(width=25, height=1)

text8 = tk.Label(window, text="N/A")
text8.grid(row=4, column=4, padx=0, pady=10, sticky="w")
text8.config(width=25, height=1)

text8 = tk.Label(window, text="N/A")
text8.grid(row=5, column=4, padx=0, pady=10, sticky="w")
text8.config(width=25, height=1)

text8 = tk.Label(window, text="N/A")
text8.grid(row=6, column=4, padx=0, pady=10, sticky="w")
text8.config(width=25, height=1)

text8 = tk.Label(window, text="N/A")
text8.grid(row=7, column=4, padx=0, pady=10, sticky="w")
text8.config(width=25, height=1)

window.mainloop()