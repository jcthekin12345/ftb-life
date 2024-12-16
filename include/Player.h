//
// Created by jctheking on 12/16/24.
//

#ifndef PLAYER_H
#define PLAYER_H
#include <string>
#include <unordered_map>
#include "../include/Skill.h"
#include <vector>

class Player {
private:
  std::string _name;
  std::string _lastName;
  std::string _role;
  int _age;
  std::string country;
  std::unordered_map<std::string, Skill> skills;
  // Add additional attributes as needed

  static const std::unordered_map<std::string, std::vector<std::string>> roleSkills;

public:
  Player(const std::string& playerName
    , const std::string& playerLastName
    , const std::string& playerRole);
  void incrementSkill(const std::string& skillName, int& value);
  void decrementSkill(const std::string& skillName, int& value);
  void displaySkills() const;

};


#endif //PLAYER_H
