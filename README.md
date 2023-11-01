# MLOps Monitoring Heart Attack Prediction

Prérequis:
- Installer docker
- Python
- Un IDE: Pycharm ou Vscode

Pour créer une image docker de l'application api heart attack prediction, dans un terminal, se placer dans le dossier du projet

```
docker build -t heart_attack_prediction_api . 
```

Pour démarrer l'application dans un conteneur docker:

```
docker run -p 5000:5000 -it heart_attack_prediction_api
```

En mode dev, le plus simple c'est de démarrer l'application via vscode ou pycharm, cela nous permet de debugger plus facilement si besoin.

Pour démarrer le tendem prometheus/grafana:

```
docker compose up -d
```

Tout est configuré pour fonctionner avec l'application démarrée en mode dev, c'est à dire démrée avec Pycharm ou vscode.
