import random

class Cube:
    def __init__(self):
        self.reset()

    def reset(self):
        self.faces = {
            "U": ["⬜"] * 9,
            "D": ["🟨"] * 9,
            "F": ["🟩"] * 9,
            "B": ["🟦"] * 9,
            "L": ["🟥"] * 9,
            "R": ["🟧"] * 9,
        }

    def rotate_face(self, face):
        f = self.faces[face]
        self.faces[face] = [
            f[6], f[3], f[0],
            f[7], f[4], f[1],
            f[8], f[5], f[2]
        ]

    def move(self, move):
        if move not in ["U", "D", "L", "R", "F", "B"]:
            return False

        self.rotate_face(move)
        return True

    def shuffle(self, n=20):
        for _ in range(n):
            self.move(random.choice(["U", "D", "L", "R", "F", "B"]))

    def render(self):
        f = self.faces
        return (
            f"      {f['U'][0]} {f['U'][1]} {f['U'][2]}\n"
            f"      {f['U'][3]} {f['U'][4]} {f['U'][5]}\n"
            f"      {f['U'][6]} {f['U'][7]} {f['U'][8]}\n\n"
            f"{f['L'][0]} {f['L'][1]} {f['L'][2]}   "
            f"{f['F'][0]} {f['F'][1]} {f['F'][2]}   "
            f"{f['R'][0]} {f['R'][1]} {f['R'][2]}\n"
            f"{f['L'][3]} {f['L'][4]} {f['L'][5]}   "
            f"{f['F'][3]} {f['F'][4]} {f['F'][5]}   "
            f"{f['R'][3]} {f['R'][4]} {f['R'][5]}\n"
            f"{f['L'][6]} {f['L'][7]} {f['L'][8]}   "
            f"{f['F'][6]} {f['F'][7]} {f['F'][8]}   "
            f"{f['R'][6]} {f['R'][7]} {f['R'][8]}\n\n"
            f"      {f['D'][0]} {f['D'][1]} {f['D'][2]}\n"
            f"      {f['D'][3]} {f['D'][4]} {f['D'][5]}\n"
            f"      {f['D'][6]} {f['D'][7]} {f['D'][8]}"
        )
