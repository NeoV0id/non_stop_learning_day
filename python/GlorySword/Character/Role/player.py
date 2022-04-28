#!/usr/bin/python3
""" Module for player class (BaseClass) """


class Player():
    """ 
    Class Player:
    will include Main Player and NPC (as sub-classes)
    args:
        hp: health points
        def: defense points
        manaa: magic points
        level: current level of player
    """
    __hp = 100
    __def = 10
    __manaa = 50
    __attack = 10
    __level = 1
    required_xp = 100
    __xp = 0

    def __init__(self, name, role):
        """
        __init__ method for Player
        args:
            name: name of player
            role: class of player
        """
        self.__name = name

    @property
    def name(self):
        """ name: get name of player
            Args: none
            Returns: name
        """
        return self.__name
    
    @name.setter
    def name(self, name):
        """
            name: get name of Player
            Args:
                name (str): name of Player
        """
        try:
            self.__name = name
        except TypeError:
            print("Name must be a string")

    def leveling_up(self):
        if Player.__xp == Player.required_xp:
            Player.__level += 1
            Player.required_xp += 100
            Player.__hp += 15
            Player.__def += 5
            Player.__attack += 5
            Player.__manaa += 2
            print("Level Up!\n", Player.__level)

    def defense(self, a):
        dmg = a / Player.__def
        return dmg