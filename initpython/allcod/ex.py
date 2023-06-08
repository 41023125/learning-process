import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input2_label = tk.Label(self, text="實際距離:")
        self.input2_label.pack()
        self.input2 = tk.Entry(self)
        self.input2.pack()

        self.input3_label = tk.Label(self, text="當前輪徑:")
        self.input3_label.pack()
        self.input3 = tk.Entry(self)
        self.input3.pack()

        self.submit_button = tk.Button(
            self, text="計算", command=self.show_output)
        self.submit_button.pack()

        self.output_label = tk.Label(self, text="輪徑:")
        self.output_label.pack()
        self.output = tk.Label(self, text="")
        self.output.pack()

        self.quit_button = tk.Button(
            self, text="Quit", command=self.master.quit)
        self.quit_button.pack()

    def show_output(self):
        input2_value = self.input2.get()
        input3_value = self.input3.get()

        # 在這裡加上你的處理邏輯，將結果顯示在output的Label中
        input2_value = float(self.input2.get())
        input3_value = float(self.input3.get())
        output_value = (input3_value * input2_value) / 1000
        self.output.config(text=output_value)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
