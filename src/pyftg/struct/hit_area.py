class HitArea:
    def __init__(self, hit_area):
        self.left: int = hit_area.left
        self.right: int = hit_area.right
        self.top: int = hit_area.top
        self.bottom: int = hit_area.bottom\
        
    def as_dict(self):
        return {
            "left": self.left,
            "right": self.right,
            "top": self.top,
            "bottom": self.bottom,
        }
    