//
// Created by jctheking on 12/16/24.
//

#ifndef PLAYER_H
#define PLAYER_H
#include <string>
#include <unordered_map>
#include "../include/Skill.h"
#include <vector>

//Player position
enum class Position {RW, LW, CF, SS, AM, CM, LM, RM, RCM, LDM, CB, LCB, RCB, LB, RB, RWB, LWB, GK};

struct SkillSet
{
  int shooting{};
  int positioning{};
  int dribbling{};
  int pace{};
  int passing{};
  int tackling{};
  int marking{};
  int heading{};
  int strength{};
  int vision{};
  int stamina{};
};

class Player {
private:
  std::string _name{};
  std::string _lastName{};
  Position _position{};
  SkillSet _skillSet{};
  int _age{};
  std::string country{};

public:
  Player(const std::string& playerName
    , const std::string& playerLastName
    , const std::string& playerRole);
  //std::string getName();
  //std::string getLastName();
  //Position getPosition();
  //SkillSet getSkillSet();
  //int getAge();
  //std::string getCountry();
  void incrementSkill(int& value);
  void decrementSkill(int& value);
  void displaySkills() const;

};


#endif //PLAYER_H
