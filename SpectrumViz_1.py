import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

class SpectrumAnalyzer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Spectrum Analyzer")

        self.image_path = None

        # Create GUI elements
        self.label = tk.Label(self.root, text="Select Image:")
        self.label.pack()

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_image)
        self.browse_button.pack()

        self.analyze_button = tk.Button(self.root, text="Analyze", command=self.analyze_spectrum)
        self.analyze_button.pack()

        self.root.mainloop()

    def browse_image(self):
        self.image_path = filedialog.askopenfilename()

    def analyze_spectrum(self):
        if self.image_path:
            # Load the image
            im = Image.open(self.image_path)
            pix = im.load()
            im_width, im_height = im.size
            wl_offset = 73.671  # wavelength start value for the spectra
            wl_p_pix = 0.3726  # wavelength per pixel

            x_all = []
            y_all = []

            # Process each column of the image to get spectral intensity values
            for i in range(0, im_width):
                x_sum = 0.0
                for j in range(0, im_height):
                    x_sum += sum(pix[i, j])

                x_all.append(i * wl_p_pix + wl_offset)
                y_all.append(x_sum)

            # Normalize the intensity values
            y_max = max(y_all)
            y_trans = np.array(y_all, dtype='f') / y_max

            # Plot the intensity graph
            plt.plot(x_all, y_trans, c='green', linewidth=2.0)
            plt.xlabel('Wavelength (nm)', fontsize=16)
            plt.ylabel('Intensity', fontsize=16)
            plt.show()
        else:
            print("Please select an image first.")

if __name__ == "__main__":
    app = SpectrumAnalyzer()
