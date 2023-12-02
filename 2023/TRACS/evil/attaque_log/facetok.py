import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from datetime import datetime

# Charger le fichier CSV
data = pd.read_csv('attaque_pabx.csv')

# Filtrer les données pour les communications provenant de l'extérieur
outside_data = data[data['réseau'] == 'outside']

# Convertir la colonne de date/heure en format approprié
outside_data['timestamp'] = pd.to_datetime(outside_data['votre_colonne_temporelle'], format='%Y-%m-%d %H:%M:%S')

# Créer un graphique de lignes pour visualiser les schémas temporels
plt.plot(outside_data['timestamp'], outside_data['votre_colonne_nombre'])
plt.xlabel('Timestamp')
plt.ylabel('Nombre')
plt.title('Schéma temporel des communications extérieures')
plt.show()

# Préparer les données pour l'Isolation Forest
X = outside_data[['votre_colonne_nombre']].values

# Entraîner l'Isolation Forest
clf = IsolationForest(contamination=0.05)  # Ajustez la contamination en fonction de votre seuil d'anomalie
clf.fit(X)

# Prédire les anomalies
outside_data['anomaly'] = clf.predict(X)

# Identifier le moment où l'attaque porte ses fruits
attack_start_time = outside_data[outside_data['anomaly'] == -1]['timestamp'].min()

# Afficher le résultat
print(f"L'attaque commence à porter ses fruits à partir de : {attack_start_time}")
