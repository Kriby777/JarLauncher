# Java JAR Launcher

[🇬🇧 English](README.md) | [🇫🇷 Français](README.fr.md)

Ein einfacher Windows-Launcher, mit dem Java-`.jar`-Dateien per Doppelklick geöffnet werden können.

## ✨ Funktionen

* Öffnet beliebige Java-`.jar`-Dateien
* Erkennt automatisch die angeklickte JAR-Datei
* Funktioniert ähnlich wie Blender mit `.blend`-Dateien
* Keine Kommandozeile nötig
* Klein und schnell
* Kann als Windows-`.exe` erstellt werden

## 📋 Voraussetzungen

* Java muss installiert sein

Java testen:

```powershell
java -version
```

Empfohlen:

* Java 17 oder neuer

## 🚀 Verwendung

1. Java installieren
2. Den Launcher als Standardprogramm für `.jar` festlegen
3. Eine `.jar` doppelklicken

Der Launcher startet automatisch:

```text
javaw -jar DeineDatei.jar
```

## ⚙️ Installation

1. Rechtsklick auf eine `.jar`-Datei
2. **Öffnen mit** auswählen
3. `JarLauncher.exe` auswählen
4. **Immer diese App verwenden** aktivieren

Danach können `.jar`-Dateien einfach per Doppelklick geöffnet werden.

## 🛠️ Aus dem Quellcode erstellen

PyInstaller installieren:

```powershell
pip install pyinstaller
```

Launcher bauen:

```powershell
pyinstaller --onefile --noconsole JarLauncher.py
```

Die fertige Datei befindet sich hier:

```text
dist/JarLauncher.exe
```

## 🖼️ Eigenes Icon

Mit Icon bauen:

```powershell
pyinstaller --onefile --noconsole --icon=icon.ico JarLauncher.py
```

## ❓ Fehlerbehebung

### Java wurde nicht gefunden

Java installieren und prüfen:

```powershell
java -version
```

### JAR startet nicht

Mögliche Gründe:

* Die JAR besitzt keine `Main-Class`
* Falsche Java-Version installiert
* Datei beschädigt

Test:

```powershell
java -jar DeineDatei.jar
```

## 📄 Lizenz

Frei verwendbar und anpassbar.

## 👤 Autor

Erstellt mit Python und PyInstaller.
