﻿# Lets-Cheat 🚀

Tento Python skript sleduje změny ve schránce a automaticky volá Gemini AI API, aby vygeneroval text na základě zkopírovaného obsahu. Vygenerovaný text následně přepíše obsah schránky. 💡
Ideální pro "neviditelné" AI cally, když nemůžete jít na Gemini či ChatGPT

## Požadavky

- Python 3.6+
- API klíč pro Gemini AI

## Instalace

```bash
git clone https://github.com/fragyyyDev/lets-cheat.git
cd lets-cheat
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

## Konfigurace

Otevřete skript a nahraďte YOUR_API_KEY svým API klíčem:

```py
client = genai.Client(api_key="YOUR_API_KEY")
```

## Spuštění

```bash
python scripts/main.py
```

## Použití

Nyní stačí kdekoliv zkopírovat text do schránky a za chvíli budete mít odpověď.
PSTTT V TESTECH JE TO NEJLEPŠÍ 
