# Java JAR Launcher

[🇬🇧 English](README.md) | [🇩🇪 Deutsch](README.de.md)

Un lanceur Windows simple permettant d'ouvrir des fichiers Java `.jar` avec un double-clic.

## ✨ Fonctionnalités

* Ouvre tous les fichiers Java `.jar`
* Détecte automatiquement le fichier JAR sélectionné
* Fonctionne comme Blender avec les fichiers `.blend`
* Aucun terminal nécessaire
* Léger et rapide
* Peut être transformé en fichier `.exe`

## 📋 Prérequis

* Java doit être installé sur votre ordinateur

Vérifier Java :

```powershell
java -version
```

Recommandé :

* Java 17 ou supérieur

## 🚀 Utilisation

1. Installer Java
2. Définir le lanceur comme application par défaut pour les fichiers `.jar`
3. Double-cliquer sur un fichier `.jar`

Le lanceur exécutera automatiquement :

```text
javaw -jar VotreFichier.jar
```

## ⚙️ Installation

1. Faire un clic droit sur un fichier `.jar`
2. Choisir **Ouvrir avec**
3. Sélectionner `JarLauncher.exe`
4. Activer **Toujours utiliser cette application**

Les fichiers `.jar` pourront ensuite être ouverts par double-clic.

## 🛠️ Compilation depuis le code source

Installer PyInstaller :

```powershell
pip install pyinstaller
```

Créer le fichier exécutable :

```powershell
pyinstaller --onefile --noconsole JarLauncher.py
```

Le fichier sera créé ici :

```text
dist/JarLauncher.exe
```

## 🖼️ Icône personnalisée

Créer avec une icône :

```powershell
pyinstaller --onefile --noconsole --icon=icon.ico JarLauncher.py
```

## ❓ Dépannage

### Java introuvable

Installez Java puis vérifiez :

```powershell
java -version
```

### Le fichier JAR ne démarre pas

Causes possibles :

* Le fichier JAR n'a pas de `Main-Class`
* Mauvaise version de Java
* Fichier endommagé

Tester :

```powershell
java -jar VotreFichier.jar
```

## 📄 Licence

Libre à utiliser et modifier.

## 👤 Auteur

Créé avec Python et PyInstaller.
