# CompTIA SecGame

Ein textbasiertes Lernspiel zur Vorbereitung auf die CompTIA Security+ Zertifizierung. Die Spieler schlüpfen in die Rolle eines Security Analysten und lernen durch praktische Szenarien und interaktive Geschichten die Grundlagen der IT-Sicherheit.

## 🎯 Features

- Interaktive Story-basierte Lernumgebung
- Praxisnahe Szenarien aus der IT-Sicherheit 
- Fortschrittsspeicherung
- Integration von Security-Tools (geplant)
- Verschiedene Lernpfade und Schwierigkeitsgrade (geplant)

## 🚀 Getting Started

### Voraussetzungen

- Python 3.12 oder höher
- pip (Python Package Manager)

### Installation

1. Repository klonen:
```bash
git clone https://github.com/yourusername/CompTiaSecGame.git
cd CompTiaSecGame
```

2. Virtuelle Umgebung erstellen und aktivieren:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# oder
.venv\Scripts\activate     # Windows
```

3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

4. Spiel starten:
```bash
python main.py
```

## 📁 Projektstruktur

```
ComptiaSecGame/
├── game_engine/          # Spiellogik
│   ├── engine.py        # Hauptspiel-Engine
│   ├── scene_manager.py # Szenenverwaltung
│   ├── player.py        # Spielerdaten
│   └── save_system.py   # Speichersystem
├── content/             # Spielinhalte
│   └── day1/           # Inhalte für Tag 1
│       ├── scenes.json  # Szenendefinitionen
│       └── dialogues.json
├── data/               # Spielerdaten
│   └── saves/          # Speicherstände
├── utils/             # Hilfsfunktionen
│   └── text_handler.py
├── docs/              # Dokumentation
├── requirements.txt   # Projektabhängigkeiten
├── README.md         # Projektdokumentation
└── main.py          # Haupteinstiegspunkt
```

## 🎮 Spielmechanik

Das Spiel basiert auf einer textbasierten Benutzeroberfläche, bei der Spieler durch verschiedene Szenarien navigieren und Entscheidungen treffen. Die Hauptkomponenten sind:

- Story-Modus: Folgt einem Security Analysten durch seinen Arbeitsalltag
- Übungsmodus: Separate Übungen zu spezifischen Security-Themen
- Wissensdatenbank: Nachschlagewerk für Security-Konzepte

## 🛠️ Entwicklung

### Neue Szenen hinzufügen

Szenen werden in JSON-Format definiert. Ein Beispiel:

```json
{
    "scene_id": {
        "text": "Beschreibung der Szene",
        "choices": [
            {
                "text": "Auswahlmöglichkeit 1",
                "next_scene": "id_der_nächsten_szene"
            }
        ]
    }
}
```


### Codekonventionen

- PEP 8 Style Guide für Python Code
- Docstrings für alle Funktionen und Klassen
- Typisierung mit Python Type Hints
- Ausführliche Kommentierung bei komplexer Logik

## 📝 Geplante Features

- [ ] Grafische Benutzeroberfläche
- [ ] Integration von YARA-Regeln
- [ ] Python-Scripting-Aufgaben



