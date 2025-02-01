# 🔐 Simple Auth System

## 📜 Description
Ce projet est un simple système d'authentification écrit en Python qui vérifie les informations d'identification à partir d'un fichier distant hébergé sur Pastebin. Il intègre également un affichage stylisé et un indicateur de progression pour améliorer l'expérience utilisateur.

## ⚡ Fonctionnalités
- Authentification basée sur un pseudo et un mot de passe.
- Vérification des identifiants via une requête HTTP.
- Affichage d'un texte ASCII stylisé.
- Animation de chargement avec une barre de progression.

## 🛠️ Prérequis
Assurez-vous d'avoir Python installé sur votre machine ainsi que les modules suivants :

```
pip install requests pystyle colorama progressbar2
```

## 🚀 Installation et exécution
1. Clonez ce repository ou téléchargez le fichier `auth.py`.
2. Exécutez le script avec la commande :
   ```
   python auth.py
   ```
3. Entrez votre pseudo et votre mot de passe lorsqu'ils vous sont demandés.

## 🖥️ Démonstration
Une fois connecté avec succès, le système affichera une animation de chargement et confirmera l'accès au serveur.

## ⚠️ Avertissement
Ce projet est un exemple éducatif. Ne l'utilisez pas pour des applications nécessitant une authentification sécurisée sans ajouter des mesures de sécurité adaptées.

## 📜 Licence
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.
