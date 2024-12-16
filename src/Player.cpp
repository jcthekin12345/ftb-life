// // Created by jctheking on 12/16/24.
//

#include "../include/Player.h"
#include "../include/Skill.h"

Player::Player(const std::string& playerName
  , const std::string& playerLastName
  , const std::string& playerRole)
  : _name(playerName), _lastName(playerLastName), _role(playerRole){

  // Initialize skills based on the player's role
  if (roleSkills.contains(_role) ) {
    for (const auto& skillName : roleSkills.at(_role)) {
      skills[skillName] = Skill(skillName);
    }
  }
}

const std::unordered_map<std::string, std::vector<std::string>> Player::roleSkills = {
  {"Striker", {"Shooting", "Positioning", "Dribbling", "Pace"}},
  {"Defender", {"Tackling", "Marking", "Heading", "Strength"}},
  {"Midfielder", {"Passing", "Vision", "Dribbling", "Stamina"}}
};