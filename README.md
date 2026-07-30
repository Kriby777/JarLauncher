# Java JAR Launcher

[🇩🇪 Deutsch](README.de.md) | [🇫🇷 Français](README.fr.md)

A simple Windows launcher that allows you to open Java `.jar` files with a double click.

## ✨ Features

* Opens any Java `.jar` file
* Automatically detects the selected JAR file
* Works like applications such as Blender opening `.blend` files
* No command line required
* Lightweight and fast
* Can be packaged as a Windows `.exe`

## 📋 Requirements

* Java installed on your computer

Check your Java installation:

```powershell
java -version
```

Recommended:

* Java 17 or newer

## 🚀 Usage

1. Install Java
2. Set the launcher as the default program for `.jar` files
3. Double-click any `.jar` file

The launcher will automatically run:

```text
javaw -jar YourFile.jar
```

## ⚙️ Installation

1. Right-click a `.jar` file
2. Select **Open with**
3. Choose `JarLauncher.exe`
4. Enable **Always use this app**

Now all `.jar` files can be opened with a double click.

## 🛠️ Building from Source

Install PyInstaller:

```powershell
pip install pyinstaller
```

Build the launcher:

```powershell
pyinstaller --onefile --noconsole JarLauncher.py
```

The executable will be created in:

```text
dist/JarLauncher.exe
```

## 🖼️ Custom Icon

Build with your own icon:

```powershell
pyinstaller --onefile --noconsole --icon=icon.ico JarLauncher.py
```

## ❓ Troubleshooting

### Java not found

Install Java and check:

```powershell
java -version
```

### JAR does not open

Possible causes:

* The JAR has no `Main-Class`
* The wrong Java version is installed
* The file is damaged

Test manually:

```powershell
java -jar YourFile.jar
```

## 📄 License

Free to use and modify.

## 👤 Author

Created with Python and PyInstaller.
