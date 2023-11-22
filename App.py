import os
import pygame
from tkinter import filedialog, Tk, Label, Button, Scrollbar, StringVar
from tkinter import *
from tkinter import Listbox

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x300")

        self.playlist = Listbox(self.root,selectmode=SINGLE, bg="lightblue", selectbackground="gray",
                                font=("Helvetica", 12), activestyle="none")
        self.playlist.pack(fill="both", expand="yes")

        self.scrollbar = Scrollbar(self.playlist, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        self.playlist.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.playlist.yview)

        self.play_button = Button(root, text="Play", width=10, command=self.play_music)
        self.play_button.pack(pady=10)

        self.stop_button = Button(root, text="Stop", width=10, command=self.stop_music)
        self.stop_button.pack(pady=10)

        self.pause_button = Button(root, text="Pause", width=10, command=self.pause_music)
        self.pause_button.pack(pady=10)

        self.resume_button = Button(root, text="Resume", width=10, command=self.resume_music)
        self.resume_button.pack(pady=10)

        self.volume_label = Label(root, text="Volume")
        self.volume_label.pack()

        self.volume_scale = StringVar()
        self.volume_scale.set(70)  # Set the default volume to 70%
        self.volume_slider = Scale(root, from_=0, to=100, orient="horizontal", variable=self.volume_scale,
                                   command=self.change_volume)
        self.volume_slider.pack()

        self.load_button = Button(root, text="Load Music", width=10, command=self.load_music)
        self.load_button.pack(pady=20)

        self.music_list = []

        # Initialize pygame mixer
        pygame.mixer.init()

    def load_music(self):
        file_path = filedialog.askopenfilename(title="Select Music", filetypes=[("Audio Files", "*.mp3")])
        if file_path:
            filename = os.path.basename(file_path)
            self.music_list.append((filename, file_path))
            self.playlist.insert("end", filename)

    def play_music(self):
        selected_index = self.playlist.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            selected_music = self.music_list[selected_index]
            pygame.mixer.music.load(selected_music[1])
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def change_volume(self, val):
        volume = int(val) / 100  # Convert the scale value to a volume percentage
        pygame.mixer.music.set_volume(volume)

if __name__ == "__main__":
    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()
