import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

def plot_spectrum(image_path):
    global canvas_graph, canvas_image
    im = Image.open(image_path)
    pix = im.load()
    im_width, im_height = im.size
    wl_offset = 73.671  # wavelength start value for the spectra
    wl_range = 0.3726 * im_width  # wavelength range
    y_bin = 3050  # bin size for adding spectral intensity for each wavelength
    wl_p_pix = 0.3726  # wavelength per pixel

    x_all = []
    y_all = []

    for i in range(0, im_width):
        x_sum = 0.0
        for j in range(0, y_bin):
            x_sum += sum(pix[i, j])

        x_all.append(i * wl_p_pix + wl_offset)
        y_all.append(x_sum)

    y_max = max(y_all)
    y_all = np.array(y_all, dtype='f')
    y_trans = y_all / 1
    index_max = np.where(y_trans == max(y_trans))
    index_max = np.array(index_max, dtype='i')
    index_max = index_max * wl_p_pix + wl_offset

    start1 = 300
    end1 = 900
    index_max1 = np.where(y_trans[start1:end1] == max(y_trans[start1:end1]))
    index_max1 = start1 + np.array(index_max1, dtype='i')
    index_max1 = index_max1 * wl_p_pix + wl_offset

    start2 = 900
    end2 = 1000
    index_max2 = np.where(y_trans[start2:end2] == max(y_trans[start2:end2]))
    index_max2 = start2 + np.array(index_max2, dtype='i')
    index_max2 = index_max2 * wl_p_pix + wl_offset

    start3 = 1000
    end3 = 1200
    index_max3 = np.where(y_trans[start3:end3] == max(y_trans[start3:end3]))
    index_max3 = start3 + np.array(index_max3, dtype='i')
    index_max3 = index_max3 * wl_p_pix + wl_offset

    start4 = 1200
    end4 = 1300
    index_max4 = np.where(y_trans[start4:end4] == max(y_trans[start4:end4]))
    index_max4 = start4 + np.array(index_max4, dtype='i')
    index_max4 = index_max4 * wl_p_pix + wl_offset

    start5 = 1300
    end5 = 1500
    index_max5 = np.where(y_trans[start5:end5] == max(y_trans[start5:end5]))
    index_max5 = start5 + np.array(index_max5, dtype='i')
    index_max5 = index_max5 * wl_p_pix + wl_offset

    violet_index = int(wl_offset)
    red_index = int(wl_offset + wl_range)

    plt.figure(figsize=(8, 8))
    plt.plot(index_max, [50000], 'o', c='red')
    plt.plot(index_max, [200000], 'o', c='red')
    plt.plot(index_max, [300000], 'o', c='red')
    plt.plot(index_max, [100000], 'o', c='red')
    plt.plot(index_max, [150000], 'o', c='red')
    plt.plot(index_max, [350000], 'o', c='red')
    plt.plot(index_max, [250000], 'o', c='red')

    plt.plot(index_max5, [50000], 'o', c='black')
    plt.plot(index_max5, [100000], 'o', c='black')
    plt.plot(index_max5, [150000], 'o', c='black')
    plt.plot(index_max5, [200000], 'o', c='black')
    plt.plot(index_max5, [250000], 'o', c='black')
    plt.plot(index_max5, [300000], 'o', c='black')
    plt.plot(index_max5, [350000], 'o', c='black')

    plt.plot(x_all, y_trans, c='green', linewidth=2.0)
    plt.xlabel('Wavelength (nm)', fontsize=16)
    plt.ylabel('Intensity', fontsize=16)
    plt.xlim(violet_index, red_index)
    plt.savefig("graph.jpg")

    # Resize both the image and the graph to specified sizes before displaying
    img = Image.open(image_path)
    img = img.resize((100, 100), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    canvas_image.config(width=100, height=100)
    canvas_image.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas_image.image = photo

    graph_img = Image.open("graph.jpg")
    graph_img = graph_img.resize((800, 800), Image.LANCZOS)
    graph_photo = ImageTk.PhotoImage(graph_img)
    canvas_graph.config(width=800, height=800)
    canvas_graph.create_image(0, 0, anchor=tk.NW, image=graph_photo)
    canvas_graph.image = graph_photo

def open_file():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    plot_spectrum(file_path)

def close_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Spectrum Plotter")

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create a button to open file
open_button = tk.Button(button_frame, text="Open File", command=open_file)
open_button.pack(side=tk.LEFT, padx=5)

# Create a button to close the app
close_button = tk.Button(button_frame, text="Close", command=close_app)
close_button.pack(side=tk.LEFT, padx=5)

# Create a frame for the image and graph
display_frame = tk.Frame(root)
display_frame.pack()

# Create a canvas to display the selected image
canvas_image = tk.Canvas(display_frame, width=100, height=100, bg="white")
canvas_image.pack(side=tk.TOP, padx=10, pady=10)

# Create a canvas to display the spectrum plot
canvas_graph = tk.Canvas(display_frame, width=800, height=800, bg="white")
canvas_graph.pack(side=tk.BOTTOM, padx=10, pady=10)

# Create a horizontal scrollbar
scrollbar = tk.Scrollbar(display_frame, orient="horizontal", command=canvas_graph.xview)
scrollbar.pack(side="bottom", fill="x")
canvas_graph.configure(xscrollcommand=scrollbar.set)

root.mainloop()
