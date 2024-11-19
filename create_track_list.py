from tkinter import *
import tkinter as tk

import font_manager as fonts 
import library_item as lib
from tkinter import messagebox as msg

# def set_text(text_area, content):
#     text_area.delete("1.0", END)
#     text_area.insert(1.0, content)

class CreateTrack():
    def __init__(self):
        self.window = Tk()
        self.window.title("Create Track Lists")
        self.window.geometry("750x350")

        self.create_widgets()

    def create_widgets(self):
        self.lbl_enter = Label(self.window, text="Enter a track number")
        self.lbl_enter.grid(row=0, column=0, padx=10, pady=10)

        self.txt_enter = Entry(self.window,width=5)
        self.txt_enter.grid(row=0, column=1, padx=10, pady=10,sticky=W)

        self.btn_add_track = Button(self.window, text="Add track to a playlist")
        self.btn_add_track.grid(row=1, column=0, padx=10, pady=10, sticky=N)

        self.lbl_playlist = Label(self.window, text="Playlist")
        self.lbl_playlist.grid(row=0, column=2, padx=10, pady=10)

        self.lst_playlist = Listbox(self.window, width=48, height=12)
        self.lst_playlist.grid(row=1, column=2, padx=10, pady=10)
        
    # def add_track_clicked(self):
    #     key = self.txt_enter.get()
    #     name = lib.get_name(key)
    #     if name is not None:
    #         artist = lib.get_artist(key)
    #         rating = lib.get_rating(key)
    #         play_count = lib.get_play_count(key)
    #         track_details = f"Name:{name}\nArtist{artist}\nRating{rating}\nPlays{play_count}"
    #         set_text(self.lst_playlist ,track_details)
    #     else:
    #         msg.showerror("Tracks", f"Track {key} not found")

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    create = CreateTrack()
    create.run()


