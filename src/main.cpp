#include <iostream>
#include "../include/Player.h"
int main()
{
  Player player = Player("Joaquin", "Coetzee", "Striker");
  player.incrementSkill("Shooting", 50);
  player.displaySkills();
    return 0;
}