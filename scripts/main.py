import time
import pyperclip  # type: ignore
from google import genai

# Nastavení klienta s API klíčem
client = genai.Client(api_key="YOUR API KEY")

def generate_content(input_text):
    """Zavolá API a vrátí vygenerovaný text."""
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=input_text,
        )
        return response.text
    except Exception as e:
        print("Chyba API:", e)
        return ""

def main():
    # Nastavíme počáteční hodnotu schránky
    try:
        last_text = pyperclip.paste()
    except Exception as e:
        print("Chyba při čtení schránky:", e)
        last_text = ""
    
    print("Skript spuštěn. Sleduji schránku (Ctrl+C pro ukončení)...")
    
    while True:
        try:
            clipboard_text = pyperclip.paste()
        except Exception as e:
            print("Chyba při čtení schránky:", e)
            time.sleep(1)
            continue

        # Volat API pouze při změně a pokud text není prázdný
        if clipboard_text != last_text and clipboard_text.strip():
            print("\nNový text ve schránce:")
            print(clipboard_text)
            last_text = clipboard_text

            print("Volám API...")
            generated_text = generate_content(clipboard_text)

            if generated_text:
                print("Vygenerovaný text:")
                print(generated_text)
                try:
                    pyperclip.copy(generated_text)
                    print("Schránka aktualizována.")
                    last_text = generated_text  # Aktualizujeme poslední hodnotu
                except Exception as e:
                    print("Chyba při zápisu do schránky:", e)
            else:
                print("API nevrátilo žádný text.")

        time.sleep(1)

if __name__ == "__main__":
    main()
