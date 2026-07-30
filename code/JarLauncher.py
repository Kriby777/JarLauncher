import sys
import subprocess
import os

if len(sys.argv) < 2:
    print("Keine JAR-Datei angegeben")
    input()
    sys.exit()

jar_datei = sys.argv[1]

if not jar_datei.lower().endswith(".jar"):
    print("Keine JAR-Datei")
    input()
    sys.exit()

subprocess.Popen([
    "javaw",
    "-jar",
    jar_datei
])