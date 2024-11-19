import tkinter as tk
from tkinter import *

import font_manager as fonts
from view_tracks import TrackViewer
from create_track_list import CreateTrack
from update_tracks import UpdateTrack


class TrackPlayer():
    def __init__(self):
        self.window = Tk()
        self.window.title("Juke Box")
        self.window.geometry("520x150")
        self.window.configure(bg="cyan")

        self.create_widgets()
        fonts.configure()

    def create_widgets(self):
        
        self.header_lbl = Label(self.window, text="Select an option by clicking one of the buttons below")
        self.header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.view_tracks_btn = Button(self.window, text="View Tracks", command=self.view_tracks_clicked)
        self.view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

        self.create_track_list_btn = Button(self.window, text="Create Track List", command=self.create_track_clicked)
        self.create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

        self.update_tracks_btn = Button(self.window, text="Update Tracks", command=self.update_track_clicked)
        self.update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

        self.status_lbl = Label(self.window, bg='gray', text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def view_tracks_clicked(self):
        self.status_lbl.configure(text="View Tracks button was clicked!")
        TrackViewer(Toplevel(self.window))

    def create_track_clicked(self):
        self.status_lbl.configure(text="Create Track Lists button was clicked!")
        CreateTrack(Toplevel(self.window))

    def update_track_clicked(self):
        self.status_lbl.configure(text="Update Track Lists button was clicked!")
        UpdateTrack(tk.Toplevel(self.window))

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    track_player = TrackPlayer()
    track_player.run()



# def view_tracks_clicked():
#     status_lbl.configure(text="View Tracks button was clicked!")
#     TrackViewer(tk.Toplevel(window))

# def create_track_clicked():
#     status_lbl.configure(text="Create Track Lists button was clicked!")
#     CreateTrack(tk.Toplevel(window))


# window = tk.Tk()
# window.geometry("520x150")
# window.title("JukeBox")
# window.configure(bg="gray")

# fonts.configure()

# header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
# header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# view_tracks_btn = tk.Button(window, text="View Tracks", command=view_tracks_clicked)
# view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

# create_track_list_btn = tk.Button(window, text="Create Track List", command=create_track_clicked)
# create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

# update_tracks_btn = tk.Button(window, text="Update Tracks")
# update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

# status_lbl = tk.Label(window, bg='gray', text="", font=("Helvetica", 10))
# status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# window.mainloop()
