from PIL import Image
import sys

def clean_image(input_image_path, output_image_path):
    # Ouvre l'image
    img = Image.open(input_image_path)

    # Convertit l'image en mode RGB
    img = img.convert("RGB")

    # Obtient les dimensions de l'image
    width, height = img.size

    # Parcourt tous les pixels de l'image
    for i in range(width):
        for j in range(height):
            # Obtient les valeurs de chaque canal de couleur (rouge, vert, bleu)
            r, g, b = img.getpixel((i, j))
            
            # Transforme le pixel en gris en calculant la moyenne des valeurs RGB
            gray_value = (r + g + b) // 3
            img.putpixel((i, j), (gray_value, gray_value, gray_value))

    # Enregistre l'image nettoyée
    img.save(output_image_path)

if __name__ == "__main__":
    # Vérifie si le nombre d'arguments est correct
    if len(sys.argv) != 3:
        print("Usage: python clean_image.py input_image_path output_image_path")
        sys.exit(1)

    # Récupère les chemins d'entrée et de sortie des images depuis les arguments de la ligne de commande
    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]

    # Nettoie l'image
    clean_image(input_image_path, output_image_path)

    print("Image nettoyée avec succès!")
