# Utiliser l'image Python officielle comme image de base
FROM python:3.10

# Définir le répertoire de travail dans le conteneur
WORKDIR .

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Mettre à jour pip et installer les dépendances
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copier l'ensemble du répertoire courant dans le répertoire de travail du conteneur
COPY . .

# Définir la commande pour exécuter l'application
CMD ["python", "./api_heart_attack_prediction.py"]
