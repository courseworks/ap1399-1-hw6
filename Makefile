CXX = g++
CXXFLAGS = -std=c++2a -Wall -I h -I /usr/local/include/gtest/ -c
LXXFLAGS = -std=c++2a -Ih -pthread
OBJECTS = ./obj/student.o ./obj/main.o ./obj/aphw6_unittest.o 
GTEST = /usr/local/lib/libgtest.a
TARGET = main


$(TARGET): $(OBJECTS)
	$(CXX) $(LXXFLAGS) -o $(TARGET) $(OBJECTS) $(GTEST)
./obj/student.o: ./cpp/student.cpp
	$(CXX) $(CXXFLAGS) ./cpp/student.cpp -o ./obj/student.o
./obj/aphw6_unittest.o: ./cpp/aphw6_unittest.cpp
	$(CXX) $(CXXFLAGS) ./cpp/aphw6_unittest.cpp -o ./obj/aphw6_unittest.o
./obj/main.o: ./cpp/main.cpp ./h/aphw6.h
	$(CXX) $(CXXFLAGS) ./cpp/main.cpp -o ./obj/main.o
clean:
	rm -fv $(TARGET) $(OBJECTS)
