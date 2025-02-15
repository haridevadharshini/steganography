from PIL import Image
import numpy as np
import os

def encrypt_message(message, passcode):
    """Encrypts the message using XOR encryption with the passcode."""
    return ''.join(chr(ord(c) ^ ord(passcode[i % len(passcode)])) for i, c in enumerate(message))

def hide_data(image_path, message, passcode, output_path):
    """Encrypts the message using a passcode and hides it in an image."""
    
    try:
        # Encrypt the message
        encrypted_msg = encrypt_message(message, passcode)
        print(f"Encrypted Message: {encrypted_msg}")

        # Convert the encrypted message to binary
        message_bits = ''.join(format(ord(i), '08b') for i in encrypted_msg)

        # Append a termination marker (eight 1s) to detect message stopping point
        message_bits += '11111111'  

        # Open the image
        img = Image.open(image_path)
        img = img.convert("RGB")  # Ensure it's in RGB mode
        pixels = np.array(img, dtype=np.uint8)

        # Get dimensions
        height, width, _ = pixels.shape
        idx = 0

        # Iterate through pixels to hide the message
        for row in range(height):
            for col in range(width):
                for color in range(3):  # Modify R, G, B channels
                    if idx < len(message_bits):
                        pixels[row, col, color] = (pixels[row, col, color] & 0xFE) | int(message_bits[idx])
                        idx += 1
                    else:
                        break
                if idx >= len(message_bits):
                    break
            if idx >= len(message_bits):
                break

        if idx < len(message_bits):
            return "Error: Image is too small to hide the full message."

        # Convert back to an image and save it
        stego_img = Image.fromarray(pixels)
        stego_img.save(output_path)

        if os.path.exists(output_path):
            print(f"Stego Image Saved at {output_path}")
            return f"Message Hidden and Encrypted Successfully! Saved at: {output_path}"
        else:
            return "Error: Failed to save the encrypted image."

    except Exception as e:
        return f"Error: {str(e)}"
