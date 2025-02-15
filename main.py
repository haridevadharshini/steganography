import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from encryption import hide_data  
from decryption import extract_data  

class StegoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Image Steganography")
        self.root.geometry("400x350")

        self.message_label = tk.Label(self.root, text="Enter the message to hide:")
        self.message_label.pack(pady=10)

        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.pack(pady=5)

        self.passcode_label = tk.Label(self.root, text="Enter passcode:")
        self.passcode_label.pack(pady=10)

        self.passcode_entry = tk.Entry(self.root, width=50, show="*")
        self.passcode_entry.pack(pady=5)

        self.encrypt_button = tk.Button(self.root, text="Encrypt & Hide in Image", command=self.encrypt_image)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(self.root, text="Extract & Decrypt Message", command=self.decrypt_image)
        self.decrypt_button.pack(pady=10)

    def encrypt_image(self):
        image_path = filedialog.askopenfilename(title="Select Image for Encryption")
        if image_path:
            message = self.message_entry.get()
            passcode = self.passcode_entry.get()
            if message and passcode:
                result = hide_data(image_path, message, passcode, "encrypted_image.png")
                messagebox.showinfo("Success", result)
            else:
                messagebox.showwarning("Input Error", "Please enter both message and passcode.")
        else:
            messagebox.showwarning("File Error", "Please select an image.")

    def decrypt_image(self):
        image_path = filedialog.askopenfilename(title="Select Image for Decryption")
        if image_path:
            # Ask for passcode in a pop-up
            passcode = simpledialog.askstring("Passcode Required", "Enter the passcode:", show="*")
            
            if passcode:
                result = extract_data(image_path, passcode)
                messagebox.showinfo("Decrypted Message", result)
            else:
                messagebox.showwarning("Input Error", "Passcode cannot be empty.")
        else:
            messagebox.showwarning("File Error", "Please select an image.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StegoApp(root)
    root.mainloop()
