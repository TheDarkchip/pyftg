from .attack_data import AttackData
from .enumerate.action import Action
from .enumerate.state import State

class CharacterData:
    def __init__(self, character_data):
        self.player_number: bool = character_data.player_number
        self.hp: int = character_data.hp
        self.energy: int = character_data.energy
        self.x: int = character_data.x
        self.y: int = character_data.y
        self.left: int = character_data.left
        self.right: int = character_data.right
        self.top: int = character_data.top
        self.bottom: int = character_data.bottom
        self.speed_x: int = character_data.speed_x
        self.speed_y: int = character_data.speed_y
        self.state = State(character_data.state)
        self.action = Action(character_data.action)
        self.front: bool = character_data.front
        self.control: bool = character_data.control
        self.attack_data = AttackData(character_data.attack_data)
        self.remaining_frame: int = character_data.remaining_frame
        self.hit_confirm: bool = character_data.hit_confirm
        self.graphic_size_x: int = character_data.graphic_size_x
        self.graphic_size_y: int = character_data.graphic_size_y
        self.graphic_adjust_x: int = character_data.graphic_adjust_x
        self.hit_count: int = character_data.hit_count
        self.last_hit_frame: int = character_data.last_hit_frame

    def as_dict(self):
        return {
            "player_number": self.player_number,
            "hp": self.hp,
            "energy": self.energy,
            "x": self.x,
            "y": self.y,
            "left": self.left,
            "right": self.right,
            "top": self.top,
            "bottom": self.bottom,
            "speed_x": self.speed_x,
            "speed_y": self.speed_y,
            "state": self.state.__str__(),
            "action": self.action.__str__(),
            "front": self.front,
            "control": self.control,
            "attack_data": self.attack_data.as_dict(),
            "remaining_frame": self.remaining_frame,
            "hit_confirm": self.hit_confirm,
            "graphic_size_x": self.graphic_size_x,
            "graphic_size_y": self.graphic_size_y,
            "graphic_adjust_x": self.graphic_adjust_x,
            "hit_count": self.hit_count,
            "last_hit_frame": self.last_hit_frame,
        }
    