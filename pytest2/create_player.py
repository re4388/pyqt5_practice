# # contents of test_player_mechanics.py
# def test_player_hit():
#     player = create_player()
#     assert player.health == 100
#     undead = create_undead()
#     undead.hit(player)
#     assert player.health == 80


class create_player(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 100

class create_undead(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 1000
        self.p1 = create_player()
    def hit(self, p1):
        p1.health -= 20

    