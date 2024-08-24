
def player(*args):
    """A player generation prototype"""
    playerInfo = [i for i in args]
    return playerInfo

def player_gen():
    player()


if __name__ == "__main__":
    print(player("name", 5, "10"))
