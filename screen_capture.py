import cv2
import numpy as np
import mss
import time

def capture_screen_video(filename="enregistrement_ecran.avi", fps=20.0):
    # Définir la résolution de l'écran
    with mss.mss() as sct:
        ecran = sct.monitors[1]  # Capturer le premier écran
        largeur, hauteur = ecran["width"], ecran["height"]

        # Initialiser l'enregistrement vidéo
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter(filename, fourcc, fps, (largeur, hauteur))

        try:
            while True:
                # Capturer l'image de l'écran
                img = np.array(sct.grab(ecran))
                
                # Convertir l'image en format BGR pour OpenCV
                frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

                # Enregistrer la trame dans le fichier vidéo
                out.write(frame)

                # Quitter la capture si on appuie sur 'q'
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        finally:
            # Libérer les ressources
            out.release()
            cv2.destroyAllWindows()

# Appeler la fonction de capture d'écran
capture_screen_video()
