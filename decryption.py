from PIL import Image
import numpy as np

def decrypt_message(encrypted_message, passcode):
    """Decrypts the message using XOR decryption with the passcode."""
    return ''.join(chr(ord(c) ^ ord(passcode[i % len(passcode)])) for i, c in enumerate(encrypted_message))

def extract_data(image_path, passcode):
    """Extracts the encrypted message from the image and decrypts it."""
    
    try:
        # Open the image
        img = Image.open(image_path)
        pixels = np.array(img)

        binary_data = ""
        for row in pixels:
            for pixel in row:
                for i in range(3):  # Extract LSB from RGB
                    binary_data += str(pixel[i] & 1)

        # Convert binary to characters (8 bits = 1 character)
        byte_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

        # Convert binary to readable text
        message = ''.join(chr(int(b, 2)) for b in byte_data if len(b) == 8)

        # Stop at the first occurrence of the terminator (`11111111`)
        terminator_index = message.find(chr(255))
        if terminator_index != -1:
            hidden_encrypted_message = message[:terminator_index]
        else:
            hidden_encrypted_message = message

        print(f"Extracted Encrypted Message: {hidden_encrypted_message}")

        # Decrypt the message with the entered passcode
        decrypted_message = decrypt_message(hidden_encrypted_message, passcode)

        return f"Decrypted Message: {decrypted_message}"
    
    except Exception as e:
        return f"Error: {str(e)}"
