import tkinter as tk
from tkinter import messagebox

class FrameRecorder(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Frame Recorder")
        self.geometry("600x300")
        self.configure(bg="pink")

        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(self, text="Frame Recorder", font=("Helvetica", 24), bg="pink")
        self.label_title.pack(pady=10)

        self.label_fps = tk.Label(self, text="create an", font=("Helvetica", 14), bg="pink")
        self.label_fps.pack()

        self.entry_fps = tk.Entry(self, font=("Helvetica", 14), width=10)
        self.entry_fps.pack()

        self.label_fps_suffix = tk.Label(self, text="fps video", font=("Helvetica", 14), bg="pink")
        self.label_fps_suffix.pack()

        self.button_pause = tk.Button(self, text="Pause", font=("Helvetica", 14), command=self.pause_recording)
        self.button_pause.pack(side=tk.LEFT, padx=20, pady=20)

        self.button_start = tk.Button(self, text="Start", font=("Helvetica", 14), command=self.start_recording)
        self.button_start.pack(side=tk.LEFT, padx=20, pady=20)

        self.button_end = tk.Button(self, text="End", font=("Helvetica", 14), command=self.end_recording)
        self.button_end.pack(side=tk.LEFT, padx=20, pady=20)

        self.label_status = tk.Label(self, text="Recording Paused", font=("Helvetica", 14), bg="pink")
        self.label_status.pack(pady=10)

    def pause_recording(self):
        self.label_status.config(text="Recording Paused")

    def start_recording(self):
        fps = self.entry_fps.get()
        if not fps.isdigit():
            messagebox.showerror("Invalid input", "Please enter a valid number for FPS")
        else:
            self.label_status.config(text="Recording Started")

    def end_recording(self):
        self.label_status.config(text="Recording Ended")


if __name__ == "__main__":
    app = FrameRecorder()
    app.mainloop()