#  SecGame

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


#  SecGame

A text-based learning game to prepare for the CompTIA Security+ certification. Players take on the role of a Security Analyst and learn IT security fundamentals through practical scenarios and interactive stories.

## 🎯 Features

- Interactive story-based learning environment
- Practical scenarios from IT security
- Progress saving
- Integration of security tools (planned)
- Various learning paths and difficulty levels (planned)

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- pip (Python Package Manager)

### Installation

1. Clone repository:
```bash
git clone https://github.com/yourusername/CompTiaSecGame.git
cd CompTiaSecGame
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start game:
```bash
python main.py
```

## 📁 Project Structure

```
ComptiaSecGame/
├── game_engine/          # Game logic
│   ├── engine.py        # Main game engine
│   ├── scene_manager.py # Scene management
│   ├── player.py        # Player data
│   └── save_system.py   # Save system
├── content/             # Game content
│   └── day1/           # Content for day 1
│       ├── scenes.json  # Scene definitions
│       └── dialogues.json
├── data/               # Player data
│   └── saves/          # Save states
├── utils/             # Helper functions
│   └── text_handler.py
├── docs/              # Documentation
├── requirements.txt   # Project dependencies
├── README.md         # Project documentation
└── main.py          # Main entry point
```

## 🎮 Game Mechanics

The game is based on a text-based user interface where players navigate through various scenarios and make decisions. The main components are:

- Story Mode: Follows a Security Analyst through their workday
- Practice Mode: Separate exercises for specific security topics
- Knowledge Base: Reference guide for security concepts

## 🛠️ Development

### Adding New Scenes

Scenes are defined in JSON format. Example:

```json
{
    "scene_id": {
        "text": "Scene description",
        "choices": [
            {
                "text": "Choice option 1",
                "next_scene": "id_of_next_scene"
            }
        ]
    }
}
```

### Code Conventions

- PEP 8 Style Guide for Python code
- Docstrings for all functions and classes
- Typing with Python Type Hints
- Detailed comments for complex logic

## 📝 Planned Features

- [ ] Graphical User Interface
- [ ] YARA rules integration
- [ ] Python scripting tasks




