from pytube import YouTube
import os

# Spécifiez le chemin de destination pour sauvegarder le fichier téléchargé.
# Remplacez la valeur par le chemin souhaité sur votre machine.
destination = "C:/Users/Documents/Brouillon"

# Lien de la vidéo YouTube à télécharger.
# Remplacez-le par le lien de la vidéo que vous souhaitez télécharger.
video_link = "https://youtu.be/uJHVGiUM-TA?si=wjnwnp3CTq5Jnwk_"

try:
    # Création d'un objet YouTube à partir du lien fourni.
    video = YouTube(video_link)

    # Sélection de la première piste audio disponible en format mp4.
    audio = video.streams.filter(only_audio=True, file_extension='mp4').first()

    # Génération du chemin complet du fichier de sortie en utilisant le titre de la vidéo.
    default_filename = audio.default_filename
    final_path = os.path.join(destination, default_filename)

    # Téléchargement de l'audio dans le répertoire spécifié.
    audio.download(output_path=destination)
    print(f"Téléchargement terminé ! Fichier sauvegardé sous : {final_path}")
except Exception as e:
    # Gestion des erreurs (par ex., problèmes de connexion, liens invalides).
    print(f"Erreur : {e}")
