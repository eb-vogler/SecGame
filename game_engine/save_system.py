import json
import os
from datetime import datetime


class SaveSystem:
    def __init__(self):
        self.save_dir = "data/saves"
        self.autosave_path = os.path.join(self.save_dir, "autosave.json")
        self._ensure_save_directory()

    def _ensure_save_directory(self):
        """Stellt sicher, dass das Speicherverzeichnis existiert und die autosave.json valide ist"""
        try:
            os.makedirs(self.save_dir, exist_ok=True)
            if not os.path.exists(self.autosave_path):
                # Erstelle eine leere, aber valide JSON-Datei
                self._save_to_file(self.autosave_path, {
                    "player": {
                        "name": "",
                        "progress": {
                            "current_day": 1,
                            "current_scene": "intro",
                            "completed_scenes": [],
                            "achievements": []
                        }
                    },
                    "timestamp": datetime.now().isoformat()
                })
        except Exception as e:
            print(f"Fehler beim Erstellen des Speicherverzeichnisses: {e}")
            raise

    def save_game(self, game_state, is_autosave=True):
        try:
            save_data = {
                "player": {
                    "name": game_state.player.name,
                    "progress": {
                        "current_day": game_state.player.progress["current_day"],
                        "current_scene": game_state.player.progress["current_scene"],
                        "completed_scenes": list(game_state.player.progress["completed_scenes"]),
                        "achievements": list(game_state.player.progress["achievements"])
                    }
                },
                "timestamp": datetime.now().isoformat()
            }

            if is_autosave:
                self._save_to_file(self.autosave_path, save_data)
            else:
                filename = f"save_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                filepath = os.path.join(self.save_dir, filename)
                self._save_to_file(filepath, save_data)

            return True
        except Exception as e:
            print(f"Fehler beim Speichern: {e}")
            return False

    def _save_to_file(self, filepath, data):
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Fehler beim Schreiben der Datei {filepath}: {e}")
            raise

    def load_game(self):
        try:
            if not os.path.exists(self.autosave_path):
                return None

            with open(self.autosave_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if not content.strip():  # Prüfe auf leere Datei
                    return None
                return json.loads(content)
        except json.JSONDecodeError:
            print("Warnung: Beschädigte Speicherdatei gefunden. Erstelle neue...")
            os.remove(self.autosave_path)
            self._ensure_save_directory()
            return None
        except Exception as e:
            print(f"Fehler beim Laden des Spielstands: {e}")
            return None