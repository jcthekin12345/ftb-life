//
// Created by jctheking on 12/16/24.
//

#ifndef SKILL_H
#define SKILL_H
#include <string>
#include <unordered_map>
#include <utility>

class Skill {
private:
  std::string _name; // Name of the skill
  int _rating; // Rating (e.g., 0-100)

public:
  Skill(std::string  skillName, int skillRating)
    : _name(std::move(skillName)), _rating(skillRating) {}

  // Getters
  [[nodiscard]] std::string getName() const { return _name; }
  [[nodiscard]] int getRating() const {return _rating;}

  void increment(const int& value) {
    _rating += value;
    if (_rating > 100) _rating = 100;
  }

  void decrement(const int& value) {
    _rating -= value;
    if (_rating < 0) _rating = 0;
  }

};



#endif //SKILL_H
