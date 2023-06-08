import argparse
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog

def convert_heic_to_jpg(heic_path:str, jpg_path:str):
    image = Image.open(heic_path)
    image.save(jpg_path, "JPEG")

def batch_convert_heic_to_jpg(folder_path:str):
    for filename in os.listdir(folder_path):
        if filename.endswith(".heic") or filename.endswith(".HEIC"):
            heic_path = os.path.join(folder_path, filename)
            jpg_path = os.path.join(folder_path, os.path.splitext(filename)[0] + ".jpg")
            #print(jpg_path)
            convert_heic_to_jpg(heic_path, jpg_path)

def convert_with_gui():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Sélectionnez le dossier contenant les fichiers HEIC")
    if folder_path:
        batch_convert_heic_to_jpg(folder_path)
        print("Conversion en lot réussie !")
    else:
        print("Aucun dossier sélectionné.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convertisseur HEIC en JPG")
    parser.add_argument("input", help="Chemin vers le fichier HEIC ou le dossier")
    parser.add_argument("-o", "--output", help="Chemin vers le fichier JPG de sortie ou le dossier")
    parser.add_argument("--gui", action="store_true", help="Lancer l'interface graphique pour la sélection du dossier")
    args = parser.parse_args()

    if args.gui:
        convert_with_gui()
    else:
        input_path = args.input
        output_path = args.output

        if os.path.isfile(input_path):
            if not output_path:
                output_path = os.path.splitext(input_path)[0] + ".jpg"
            convert_heic_to_jpg(input_path, output_path)
            print("Conversion réussie !")
        elif os.path.isdir(input_path):
            if not output_path:
                output_path = input_path
            batch_convert_heic_to_jpg(input_path)
            print("Conversion en lot réussie !")
        else:
            print("Chemin d'entrée invalide.")
