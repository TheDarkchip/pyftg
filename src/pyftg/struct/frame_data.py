from .attack_data import AttackData
from .character_data import CharacterData
import numpy as np

class FrameData:
    def __init__(self, frame_data=None):
        if not frame_data:
            self.character_data = [None, None]
            self.current_frame_number = -1
            self.current_round = -1
            self.projectile_data = []
            self.empty_flag = True
            self.front = [False, False]
        else:
            self.character_data = [CharacterData(x) for x in frame_data.character_data]
            self.current_frame_number: int = frame_data.current_frame_number
            self.current_round: int = frame_data.current_round
            self.projectile_data = [AttackData(x) for x in frame_data.projectile_data]
            self.empty_flag: bool = frame_data.empty_flag
            self.front = np.array(frame_data.front, dtype=np.bool8)

    def is_front(self, player: bool):
        return self.front[0 if player else 1]
    
    def get_character(self, player: bool):
        return self.character_data[0 if player else 1]
    
    def as_dict(self):
        return {
            "character_data": [x.as_dict() for x in self.character_data],
            "current_frame_number": self.current_frame_number,
            "current_round": self.current_round,
            "projectile_data": [x.as_dict() for x in self.projectile_data],
            "empty_flag": self.empty_flag,
            "front": self.front.tolist(),
        }
