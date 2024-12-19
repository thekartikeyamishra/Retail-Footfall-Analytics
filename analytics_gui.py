import tkinter as tk
from tkinter import filedialog, messagebox
from utils.video_processor import process_video
from utils.footfall_counter import load_model
from utils.file_handler import save_footfall_log


class FootfallAnalyticsApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Retail Footfall Analytics")

        # File Upload
        tk.Label(self.root, text="Upload Video:", font=("Helvetica", 12)).pack(pady=5)
        self.upload_button = tk.Button(self.root, text="Browse", command=self.upload_file)
        self.upload_button.pack(pady=5)

        # Total Footfall
        tk.Label(self.root, text="Total Footfall:", font=("Helvetica", 12)).pack(pad=5)
        self.footfall_label = tk.Label(self.root, text="0", font=("Helvetica", 14))
        self.footfall_label.pack(pady=5)

        # Save Log Button
        self.save_button = tk.Button(self.root, text="Save Footfall Log", command=self.save_log, state=tk.DISABLED)
        self.save_button.pack(pady=5)

        self.footfall_data = None
        self.model = load_model()

    def upload_file(self):
        video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi")])
        if video_path:
            self.footfall_data = process_video(video_path, self.model)
            total_footfall = sum([count for _, count in self.footfall_data])
            self.footfall_label.config(text=str(total_footfall))
            self.save_button.config(state=tk.NORMAL)

    def save_log(self):
        if self.footfall_data:
            log_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
            if log_path:
                save_footfall_log(self.footfall_data, log_path)
                messagebox.showinfo("Success", "Footfall log saved successfully!")
            else:
                messagebox.showerror("Error", "No data to save.")

    def run(self):
        self.root.mainloop()
