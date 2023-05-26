from PIL import Image
from PIL.ExifTags import TAGS
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        metadata = get_image_metadata(file_path)
        show_metadata(metadata)
    else:
        messagebox.showinfo("Information", "Aucune image sélectionnée.")

def get_image_metadata(image_path):
    image = Image.open(image_path)
    metadata = image._getexif()
    image_metadata = {}

    for tag, value in metadata.items():
        if tag in TAGS:
            tag_name = TAGS[tag]
            image_metadata[tag_name] = value

    return image_metadata

def show_metadata(metadata):
    metadata_text.delete(1.0, tk.END)
    for tag, value in metadata.items():
        metadata_text.insert(tk.END, "{}: {}\n".format(tag, value))

# Création de la fenêtre principale
window = tk.Tk()
window.title("Affichage des métadonnées d'une image")

# Bouton Parcourir
browse_button = tk.Button(window, text="Parcourir", command=browse_image)
browse_button.pack(pady=20)

# Cadre pour afficher les métadonnées
metadata_frame = tk.Frame(window)
metadata_frame.pack()

# Étiquette pour les métadonnées
metadata_label = tk.Label(metadata_frame, text="Métadonnées:")
metadata_label.pack()

# Zone de texte pour les métadonnées
metadata_text = tk.Text(metadata_frame, width=50, height=10)
metadata_text.pack()

# Affichage de la fenêtre principale
window.mainloop()

