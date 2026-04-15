import datetime
import tkinter as tk

# ------------------ CONFIG ------------------
BG_COLOR = "#0f172a"       # dark navy
CARD_COLOR = "#1e293b"     # soft card
ACCENT = "#38bdf8"         # blue accent
TEXT = "#e2e8f0"           # soft white
FUN = "#facc15"            # yellow highlight

# ------------------ LOGIC ------------------
def countdown():
    global t, paused

    if t.total_seconds() <= 0:
        timere.set("⏰ Boom! Time’s up, legend 😎")
        return

    if not paused:
        timer = datetime.datetime(1, 1, 1) + t
        timerbet = timer.strftime("%M:%S.%f")[:-3]
        timere.set(timerbet)
        t -= datetime.timedelta(milliseconds=10)

    root.after(10, countdown)


def toggle_timer():
    global t, paused

    state = toggle_button_text.get()

    if state == "🚀 Start":
        try:
            seconds = int(input_entry.get())
            if seconds <= 0:
                timere.set("🤨 Bruh... give me a real number")
                return
        except:
            timere.set("😵 Numbers only, human!")
            return

        t = datetime.timedelta(seconds=seconds)
        paused = False
        countdown()
        toggle_button_text.set("⏸ Chill")

    elif state == "⏸ Chill":
        paused = True
        toggle_button_text.set("▶️ Resume")

    elif state == "▶️ Resume":
        paused = False
        countdown()
        toggle_button_text.set("⏸ Chill")


# ------------------ UI ------------------
root = tk.Tk()
root.title("⏳ Chill Timer")
root.geometry("320x420")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Card Frame (for modern look)
card = tk.Frame(root, bg=CARD_COLOR, bd=0)
card.place(relx=0.5, rely=0.5, anchor="center", width=280, height=360)

# Title
title = tk.Label(
    card,
    text="⏳ Chill Timer",
    font=("Helvetica", 16, "bold"),
    bg=CARD_COLOR,
    fg=ACCENT
)
title.pack(pady=(15, 5))

# Timer display
timere = tk.StringVar()
timere.set("00:00.000")

timer_label = tk.Label(
    card,
    textvariable=timere,
    font=("Courier", 28, "bold"),
    bg=CARD_COLOR,
    fg=TEXT
)
timer_label.pack(pady=10)

# Input
input_entry = tk.Entry(
    card,
    font=("Helvetica", 16),
    justify="center",
    bd=0,
    bg="#334155",
    fg=TEXT,
    insertbackground=TEXT
)
input_entry.pack(pady=10, ipadx=10, ipady=8)

# Helper text
label = tk.Label(
    card,
    text="⏱ Seconds pls... don't be shy 😏",
    font=("Helvetica", 10),
    bg=CARD_COLOR,
    fg=FUN
)
label.pack(pady=(0, 10))

# Button
toggle_button_text = tk.StringVar(value="🚀 Start")

toggle_button = tk.Button(
    card,
    textvariable=toggle_button_text,
    font=("Helvetica", 14, "bold"),
    bg=ACCENT,
    fg="#0f172a",
    activebackground="#0ea5e9",
    activeforeground="white",
    bd=0,
    padx=10,
    pady=8,
    command=toggle_timer,
    cursor="hand2"
)
toggle_button.pack(pady=15)

# Footer fun 😄
footer = tk.Label(
    card,
    text="Built with ☕ + questionable life choices",
    font=("Helvetica", 8),
    bg=CARD_COLOR,
    fg="#64748b"
)
footer.pack(side="bottom", pady=10)

# ------------------ STATE ------------------
t = datetime.timedelta()
paused = False

root.mainloop()