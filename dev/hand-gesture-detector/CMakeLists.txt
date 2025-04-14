cmake_minimum_required(VERSION 3.10)
project(hand_gesture_detector)

set(CMAKE_CXX_STANDARD 20)

find_package(OpenCV REQUIRED)

include_directories(/usr/local/include)
link_directories(/usr/local/lib)

add_executable(hand_gesture_detector main.cpp)

target_link_libraries(hand_gesture_detector
        ${OpenCV_LIBS}
        paho-mqttpp3
        paho-mqtt3as
)
