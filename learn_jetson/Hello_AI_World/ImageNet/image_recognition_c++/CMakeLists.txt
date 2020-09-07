cmake_minimum_required(VERSION 2.8)

project(my-recognition)

find_package(jetson-utils)
find_package(jetson-inference)

# CUDA Qt5
find_package(CUDA)
find_package(Qt5Widgets REQUIRED)

# setup Qt5 for build
include_directories(${QT_USE_FILE})   
add_definitions(${QT_DEFINITIONS})

# compile my-recogniton program
cuda_add_executable(my-recognition my-recognition.cpp)

# link my-recognition to jetson-inference library
target_link_libraries(my-recognition jetson-inference)