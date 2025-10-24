# Huvudmeny + programstart

from watcher import Watcher
from alarms import AlarmManager
from utils import input_int
import time


def main():
    watcher = Watcher()
    alarms = AlarmManager()

    while true:
        print("\n---Huvudmeny---")
        print("1. Starta övervakning")
        print("2. Stoppa övervakning")
        print("3. Visa övervakningsstatus")
        print("4. Skapa larm")
        print("5. Visa larm")
        print("6. Ta bort larm")
        print("7. övervakningasläge (kör larmkontroll)")
        print("0. Avsluta")

        choice = input("Välj ett alternativ")

        if choice == '1':
            watcher.start()

        elif choice == '2':
            watcher.stop()

        elif choice == '3':
            watcher.status()
        elif choice == '4':
            print("\n--- Skapa larm ---")
            print("1.CPU")
            print("2. Minne")
            print("3. Disk")
            print("0. Tillbaka")

            sub_choice = input("Välj ett alternativ:")
            if sub_choice == '1':
                val = input_int("Ange CPU-larmnivå (1-100): ", 1, 100)
                if val is not None:
                    alarms.add_alarm("CPU", val)
            elif sub_choice == '2':
                val = input_int("Ange minneslarmnivå (1-100): ", 1, 100)
                if val is not None:
                    alarms.add_alarm("Minne", val)
            elif sub_choice == '3':
                val = input_int("Ange disklarmnivå (1-100): ", 1, 100)
                if val is not None:
                    alarms.add_alarm("disk", val)
                
        elif choice == '5':
            alarms.list_alarms()
            input("Tryck på Enter för att gå vidare")

        elif choice == '6':
            alarms.list_alarms()
            if alarms.alarms:
                index = input_int("Ange index för att ta bort larm (1-based, 0 för att avbryta) ", 0, len(alarms.alarms))
                if index is not None and index != 0:
                    alarms.remove_alarm(index - 1)

        elif choice == '7':
            print("Övervakningsläge startat. Tryck Ctrl+C för att stoppa.")
            try:
                while True:
                    stats = watcher.status()
                    if stats:
                        cpu, mem, disk = stats
                        for alarm_type, level in alarms.alarms:
                            if alarm_type == "CPU" and cpu >= level:
                                print(f*** VARNING, CPU ÖVERSTIGER {level}% ***)
                            if alarm_type == "Minne" and mem >= level:
                                print(f*** VARNING, MINNE ÖVERSTIGER {level}% ***)
                            if alarm_type == "Disk" and disk >= level:
                                print(f*** VARNING, DISK ÖVERSTIGER {level}% ***)
                    time.sleep(2)
            except KeyboardInterrupt:
                print("Återgå till huvudmenyn")

        elif choice == '0':
            print("Prigrammet avslutas...")
            break
        
        else:
            print("felaktigt val. Försök igen.")


if __name__ == "__main__":
    main()


