//
// Created by jctheking on 12/16/24.
//

#ifndef PLAYER_H
#define PLAYER_H
#include <string>
#include <unordered_map>
#include "../include/Skill.h"

class Player {
private:
  std::string _name;
  std::string _surname;
  int _age;
  std::unordered_map<std::string, Skill> skills;
  // Add additional attributes as needed

public:

};


#endif //PLAYER_H
