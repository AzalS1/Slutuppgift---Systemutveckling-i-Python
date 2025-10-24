# Slutuppgift---Systemutveckling-i-Python
Course repo for my work in systemytveckling in Python.

Systemövervakning i Python
Beskrivning

Detta är ett menybaserat övervakningsprogram som låter användaren övervaka CPU, minne och disk.
Användaren kan starta och stoppa övervakning, skapa och ta bort larm, samt köra ett övervakningsläge där larm triggas om resurserna överskrider satta nivåer.

Funktioner

Starta/stoppa övervakning av CPU, RAM och disk

Visa aktuell status med procent och GB-användning

Skapa larm för CPU, RAM eller disk (nivå 1–100%)

Visa alla larm, sorterade på typ och nivå

Ta bort valda larm

Övervakningsläge som varnar i realtid när larmnivåer överskrids

Robust felhantering för ogiltig användarinmatning

Teknisk information

Språk: Python 3

Bibliotek: psutil
 används för att läsa systeminformation

Struktur: Programmet består av flera filer:
main.py
watcher.py
alarms.py
utils.py

Objektorientering används för övervakning och larmhantering

Funktionell programmering används för att sortera larm innan visning