import json

# Apri il file JSON in modalità lettura
with open('filename.json', 'r') as f:
    # Leggi il contenuto del file JSON e deserializzalo in un oggetto Python
    data = json.load(f)

# Usa l'oggetto Python deserializzato
print(data)
