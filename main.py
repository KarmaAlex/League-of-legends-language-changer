import os, winshell
from pathlib import Path

desktop = winshell.desktop()
linkPath = os.path.join(desktop,"League of legends.lnk")

languageDict = {
    "englishus" : "en_us",
    "englishuk" : "en_gb",
    "englishau" : "en_au",
    "spanishes" : "es_es",
    "spanishmx" : "es_mx",
    "french" : "fr_fr",
    "german" : "de_de",
    "japanese" : "ja_jp",
    "korean" : "ko_kr",
    "italian" : "it_it",
    
}

try:
    with open("./path.txt", "r") as file:
        for lines in file.readlines():
            path = lines
    print("Client path loaded from file, if you want to change the path delete the path.txt file in this directory")
except FileNotFoundError:
    while True:
        path = input("Enter your league client path: ")
        path.replace("\"", "")
        if os.path.exists(path) and os.path.isfile(path) and os.path.split(path)[1] == "LeagueClient.exe":
            break
        else:
            print("Invalid path")

while True:
    language = input("Enter the language you want to change the launcher to: \nAvailable options are:\nEnglishUS\nEnglishUK\nEnglishAU\nSpanishES\nSpanishMX\nFrench\nGerman\nJapanese\nKorean\nItalian\nLAnguage: ")
    if language.replace(" ","").lower() in languageDict:
        language = languageDict[language]
        break
    else:
        print("Invalid language")

target = path
if os.path.exists(linkPath):
    os.remove(linkPath)
with winshell.shortcut(linkPath) as link:
    link.path = path
    link.working_directory = path.replace("/LeagueClient.exe","")
    link.arguments = "--locale=" + language
with open("./path.txt", "w") as file:
    file.writelines(path)
print("Succsessfully created shortcut")