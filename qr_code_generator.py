from tkinter import filedialog
import qrcode
import tkinter as tk
from PIL import ImageTk


class QRCodeGenerator:
    def __init__(self, master):
        self.master = master
        master.title('QR Code Generator with Python')
        master.geometry("500x500")
        master.config(bg='lavender blush')

        # Create label and entry
        self.label = tk.Label(master, text='Hello, I make QR code for you.\nEnter text or URL:', bg="lavender blush")
        self.label.pack(pady=10)
        self.entry = tk.Entry(master, width=40)
        self.entry.pack(pady=10)

        # Create button
        self.generate_button = tk.Button(master, text='Create QR code', command=self.generate_qr_code)
        self.generate_button.pack(side='top', pady=10)

        # Create save button
        self.save_button = tk.Button(master, text='Save QR code', command=self.save_qr_code, state=tk.DISABLED)
        self.save_button.pack(side='top', pady=10)

        # Create image label
        self.image_label = tk.Label(master)
        self.image_label.pack(pady=10)

        self.qr_code = None

    def generate_qr_code(self):
        data = self.entry.get()
        if data:
            qr = qrcode.QRCode(version=1, box_size=10, border=2)
            qr.add_data(data)
            qr.make(fit=True)
            self.qr_code = qr.make_image()
            display = ImageTk.PhotoImage(self.qr_code)
            self.image_label.configure(image=display)
            self.image_label.image = display
            self.save_button.config(state=tk.NORMAL)
        else:
            self.qr_code = None
            self.save_button.config(state=tk.DISABLED)

    def save_qr_code(self):
        # Save QR Code as image file
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            self.qr_code.save(file_path)


root = tk.Tk()
qrcode_generator = QRCodeGenerator(root)
root.mainloop()
