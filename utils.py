# Hjälpfunktioner (inmatningaskontroller, format mm)

def input_int(prompt: str, min_val: int, max_val: int):
    try:
        value = int(input(prompt))
        if min_val <= value <= max_val:
            return value
        else:
            print(f"Fel: värdet måste vara mellan {min_val} och {max_val}.")
            return None
    except ValueError:
        print("Fel: ogiltig inmatning, du måste mata in en siffra.")
        return None