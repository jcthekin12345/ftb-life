cmake_minimum_required(VERSION 3.30)
project(ftb_life)

set(CMAKE_CXX_STANDARD 20)

add_executable(ftb_life src/main.cpp
        src/Player.cpp
        include/Player.h
        src/Skill.h)
