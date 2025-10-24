# Hantera larm (skapa, ta bort och visa larm)

class AlarmManager:
    def __init__(self):
        self.alarms = []  #varje larm blir en tuple (typ,nivå)

    def add_alarm(self, alarm_type: str, level: int):
        if 1 <= level <= 100:
            self.alarms.append((alarm_type, level))
            print(f"larm för {alarm_type} satt till {level}%.")
        else:
            print(f"Fel: Larmnivån måste vara mellan 1 och 100")

    def list_alarms(self):
        if not self.alarms:
            print("Inga larm konfiguerade.")
        else:
            # sortering med funktionell programmering (lambda)
            for i, (alarm_type, level) in enumerate(sorted(self.alarms, key=lambda x: (x[0], x[1])), start=1):
                print(f"{i}. {alarm_type}: larm {level}%")

    def remove_alarm(self, index: int):
        if 0 <= index < len(self.alarms):
            removed = self.alarms.pop(index)
            print(f"Tog bort larm {removed[0]} på {removed [1]}%.")
        else:
            print("Fel: ogiltigt index.")
            