from .player import Player
from .save_system import SaveSystem
from .scene_manager import SceneManager
import os
import json


class GameEngine:
    def __init__(self):
        self.save_system = SaveSystem()
        self.player = None
        self.scene_manager = SceneManager()
        self.current_scene = None
        self.running = False

    def start_game(self):
        """Startet das Spiel und prüft auf vorhandene Speicherstände"""
        self.running = True
        try:
            save_data = self.save_system.load_game()

            if save_data and save_data.get("player") and save_data["player"].get("name"):
                if self._ask_load_save():
                    self._load_game_state(save_data)
                else:
                    self._start_new_game()
            else:
                self._start_new_game()

            self.game_loop()
        except Exception as e:
            print(f"Fehler beim Spielstart: {e}")
            self._start_new_game()
            self.game_loop()

    def _start_new_game(self):
        """Initialisiert ein neues Spiel"""
        self.player = Player()
        print("Willkommen zum CompTIA Security+ Lernspiel!")
        name = input("Wie ist dein Name? ")
        self.player.set_name(name)
        self.current_scene = "intro"
        self._auto_save()

    def _load_game_state(self, save_data):
        """Lädt einen bestehenden Spielstand"""
        self.player = Player()
        self.player.name = save_data["player"]["name"]
        self.player.progress = save_data["player"]["progress"]
        self.current_scene = self.player.progress["current_scene"]
        print(f"Willkommen zurück, {self.player.name}!")

    def _ask_load_save(self):
        """Fragt den Spieler, ob er den Spielstand laden möchte"""
        while True:
            choice = input("Ein Spielstand wurde gefunden. Möchten Sie ihn laden? (ja/nein): ").lower()
            if choice in ['ja', 'j', 'yes', 'y']:
                return True
            if choice in ['nein', 'n', 'no']:
                return False
            print("Bitte antworten Sie mit 'ja' oder 'nein'.")

    def game_loop(self):
        """Hauptspiel-Loop"""
        while self.running:
            self._display_current_scene()
            choice = self._handle_player_input()
            if choice == 'quit':
                self.quit_game()
            else:
                self._process_choice(choice)
            self._auto_save()

    def _display_current_scene(self):
        """Zeigt die aktuelle Szene an"""
        scene_data = self.scene_manager.get_scene(self.current_scene)
        if not scene_data:
            print("Fehler: Szene nicht gefunden!")
            self.quit_game()
            return

        print("\n" + "=" * 50 + "\n")
        print(scene_data["text"])
        print("\nOptionen:")
        for i, choice in enumerate(scene_data["choices"], 1):
            print(f"{i}. {choice['text']}")
        print("\n(q zum Beenden)")

    def _handle_player_input(self):
        """Verarbeitet die Eingabe des Spielers"""
        scene_data = self.scene_manager.get_scene(self.current_scene)
        valid_choices = range(1, len(scene_data["choices"]) + 1)

        while True:
            choice = input("\nDeine Wahl: ").lower()
            if choice == 'q':
                return 'quit'
            try:
                choice_num = int(choice)
                if choice_num in valid_choices:
                    return choice_num - 1
                print("Ungültige Eingabe. Bitte wähle eine der angezeigten Optionen.")
            except ValueError:
                print("Bitte gib eine Zahl ein oder 'q' zum Beenden.")

    def _process_choice(self, choice_index):
        """Verarbeitet die Wahl des Spielers"""
        scene_data = self.scene_manager.get_scene(self.current_scene)
        next_scene = scene_data["choices"][choice_index]["next_scene"]
        self.current_scene = next_scene
        self.player.progress["current_scene"] = next_scene
        self.player.update_progress(next_scene)

    def _auto_save(self):
        """Automatisches Speichern"""
        self.save_system.save_game(self)

    def quit_game(self):
        """Beendet das Spiel"""
        print("\nSpiel wird gespeichert und beendet...")
        self._auto_save()
        self.running = False