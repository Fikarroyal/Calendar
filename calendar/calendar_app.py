import calendar
import datetime
import tkinter as tk
from tkinter import messagebox, ttk

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar")
        self.root.geometry("500x600")
        self.root.configure(bg="black")

        self.events = {}

        self.create_widgets()

    def create_widgets(self):

        self.calendar_frame = ttk.LabelFrame(self.root, text="Calendar", padding=10)
        self.calendar_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.year_label = ttk.Label(self.calendar_frame, text="Year:")
        self.year_label.grid(row=0, column=0, padx=5, pady=5)

        self.year_entry = ttk.Entry(self.calendar_frame, width=10)
        self.year_entry.grid(row=0, column=1, padx=5, pady=5)

        self.month_label = ttk.Label(self.calendar_frame, text="Month:")
        self.month_label.grid(row=0, column=2, padx=5, pady=5)

        self.month_entry = ttk.Entry(self.calendar_frame, width=5)
        self.month_entry.grid(row=0, column=3, padx=5, pady=5)

        self.show_calendar_btn = ttk.Button(self.calendar_frame, text="Show Calendar", command=self.display_calendar)
        self.show_calendar_btn.grid(row=0, column=4, padx=5, pady=5)

        self.calendar_text = tk.Text(self.calendar_frame, width=40, height=10, state="disabled", bg="black")
        self.calendar_text.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

        # Event management frame
        self.event_frame = ttk.LabelFrame(self.root, text="Event Management", padding=10)
        self.event_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.date_label = ttk.Label(self.event_frame, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=0, column=0, padx=5, pady=5)

        self.date_entry = ttk.Entry(self.event_frame, width=15)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        self.event_label = ttk.Label(self.event_frame, text="Event:")
        self.event_label.grid(row=1, column=0, padx=5, pady=5)

        self.event_entry = ttk.Entry(self.event_frame, width=30)
        self.event_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_event_btn = ttk.Button(self.event_frame, text="Add Event", command=self.add_event)
        self.add_event_btn.grid(row=1, column=2, padx=5, pady=5)

        self.view_event_btn = ttk.Button(self.event_frame, text="View Events", command=self.view_events)
        self.view_event_btn.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    def display_calendar(self):
        try:
            year = int(self.year_entry.get())
            month = int(self.month_entry.get())
            if 1 <= month <= 12:
                cal = calendar.TextCalendar().formatmonth(year, month)
                self.calendar_text.config(state="normal")
                self.calendar_text.delete("1.0", tk.END)
                self.calendar_text.insert(tk.END, cal)
                self.calendar_text.config(state="disabled")
            else:
                messagebox.showerror("Invalid Month", "Please enter a month between 1 and 12.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid year and month.")

    def add_event(self):
        date_str = self.date_entry.get()
        event = self.event_entry.get()
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            if date in self.events:
                self.events[date].append(event)
            else:
                self.events[date] = [event]
            messagebox.showinfo("Event Added", f"Event '{event}' added on {date}.")
            self.event_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")

    def view_events(self):
        date_str = self.date_entry.get()
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            if date in self.events:
                events = self.events[date]
                events_list = "\n".join(f"{idx+1}. {event}" for idx, event in enumerate(events))
                messagebox.showinfo("Events", f"Events on {date}:\n{events_list}")
            else:
                messagebox.showinfo("No Events", f"No events found for {date}.")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
