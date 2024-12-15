import json
import os


class SceneManager:
    def __init__(self):
        self.scenes = {}
        self._load_scenes()

    def _load_scenes(self):
        """Lädt alle Szenen aus den JSON-Dateien"""
        base_path = os.path.join("content", "day1")
        scenes_file = os.path.join(base_path, "scenes.json")

        try:
            with open(scenes_file, 'r', encoding='utf-8') as f:
                self.scenes = json.load(f)
        except FileNotFoundError:
            print(f"Fehler: Szenendatei nicht gefunden: {scenes_file}")
            self.scenes = {}
        except json.JSONDecodeError:
            print(f"Fehler: Ungültiges JSON-Format in: {scenes_file}")
            self.scenes = {}

    def get_scene(self, scene_id):
        """Gibt die Daten einer spezifischen Szene zurück"""
        return self.scenes.get(scene_id)