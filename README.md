🔐 Secure Data Hiding in Images Using Steganography

 It is a project that focuses on embedding secret information within digital images to ensure secure communication. Unlike encryption, which makes data unreadable, steganography hides data in plain sight, making it difficult to detect. This project explores different techniques like Least Significant Bit (LSB) substitution to embed data efficiently while maintaining image quality. By incorporating encryption and key-based embedding, this project enhances security and prevents unauthorized access. It has applications in secure messaging, digital watermarking, and cybersecurity.
How to Execute the Code 

1️⃣ Install Required Libraries  
Open a terminal or command prompt and run:  
pip install pillow pycryptodome

2️⃣ Run the GUI Application  
Execute the following command:  
python gui.py (or) open the main.py file and press f5 to run

3️⃣ Usage Instructions  

✅ Hide a Message:  
   - Select an image.  
   - Enter the message and password.  
   - The encrypted message is embedded into a new image.
     
✅ Extract & Decrypt:
   - Load the stego-image.  
   - Enter the correct password.  
   - The original message is decrypted and displayed.  

