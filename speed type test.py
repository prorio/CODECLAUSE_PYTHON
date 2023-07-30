import tkinter as tk
import random
import time

class SpeedTypingTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Speed Typing Test")
        self.master.geometry("600x400")

        self.words = [
            "apple", "banana", "cherry", "date", "elderberry",
            "fig", "grape", "honeydew", "kiwi", "lemon"
        ]
        self.current_word = ""
        self.start_time = None

        self.label = tk.Label(self.master, text="Type the following:")
        self.label.pack()

        self.word_label = tk.Label(self.master, text="", font=("Helvetica", 24))
        self.word_label.pack()

        self.input_entry = tk.Entry(self.master, font=("Helvetica", 24))
        self.input_entry.pack()

        self.start_button = tk.Button(self.master, text="Start", command=self.start_test)
        self.start_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def start_test(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()
        self.start_time = time.time()
        self.input_entry.bind("<Return>", self.check_result)

    def check_result(self, event):
        typed_word = self.input_entry.get()
        elapsed_time = time.time() - self.start_time
        self.input_entry.unbind("<Return>")
        
        if typed_word == self.current_word:
            wpm = len(self.current_word) / (elapsed_time / 60)
            self.result_label.config(text=f"Congratulations!\nYour typing speed: {wpm:.2f} WPM")
        else:
            self.result_label.config(text="Incorrect. Please try again.")
        
        self.start_button.config(text="Restart", command=self.restart_test)

    def restart_test(self):
        self.result_label.config(text="")
        self.start_button.config(text="Start", command=self.start_test)


if __name__ == "__main__":
    root = tk.Tk()
    typing_test = SpeedTypingTest(root)
    root.mainloop()
