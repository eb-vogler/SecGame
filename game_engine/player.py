class Player:
    def __init__(self):
        self.name = ""
        self.progress = {
            "current_day": 1,
            "current_scene": "intro",
            "completed_scenes": [],
            "achievements": []
        }

    def set_name(self, name):
        self.name = name

    def update_progress(self, scene_id):
        if scene_id not in self.progress["completed_scenes"]:
            self.progress["completed_scenes"].append(scene_id)