#include <limits.h>
#include "student.h"
#include "aphw6.h"
#include <iostream>
#include <iomanip>
#include <vector>
#include <deque>
#include "gtest/gtest.h"
namespace
{
/*
TEST(APHW6Test, Test0)
{
    Student s1 {9423013, 18.2, 26};
    Student s2 {9423037, 19.2, 30};
    Student s3 {9423091, 19.1, 10};
    std::vector<Student> v {s1, s2, s3};
    std::deque<Student> d = convert<std::deque<Student>>(v);  
    EXPECT_EQ(9423037,d.at(1).id)<<std::setw(50)<<"***********minus 5***********";
}

TEST(APHW6Test, Test1)
{
    Student s1 {9423013, 18.2, 26};
    Student s2 {9423037, 19.2, 30};
    Student s3 {9423091, 19.1, 10};
    std::deque<Student> d {s1, s2, s3};
    EXPECT_EQ(9423037,findRank(d, 1).id)<<std::setw(50)<<"***********minus 5***********";
}

TEST(APHW6Test, Test2)
{
    Student s1 {9423013, 18.2, 26};
    Student s2 {9423037, 19.2, 30};
    Student s3 {9423091, 19.1, 10};
    std::vector<Student> v {s1, s2, s3};
    std::list<Student> l{convert<std::list<Student>>(v)};
    l = getRanks(l);
    EXPECT_EQ(9423013, std::next(std::begin(l), 2)->id)<<std::setw(50)<<"***********minus 5***********";
}

TEST(APHW6Test, Test3)
{
    Student s1 {9423013, 18.2, 26};
    Student s2 {9423037, 19.2, 30};
    Student s3 {9423091, 19.1, 10};
    std::deque<Student> d {s1, s2, s3};
    std::vector<Student> v {convert<std::vector<Student>>(d)};
    auto interns = getInterns(v);
    EXPECT_EQ(9423037, interns[0].id)<<std::setw(50)<<"***********minus 5***********";
}

TEST(APHW6Test, Test4)
{
    Student s1 {9423013, 18.2, 26};
    Student s2 {9423037, 19.2, 30};
    Student s3 {9423091, 19.1, 10};
    std::deque<Student> d {s1, s2, s3};
    auto ranks = getRanks(d);
    EXPECT_EQ(9423013, ranks[2].id)<<std::setw(50)<<"***********minus 5***********";
}

TEST(APHW6Test, Test5)
{
    Student s1 {9423013, 18.2, 26};
    Student s2 {9423037, 19.2, 30};
    Student s3 {9423091, 19.1, 10};
    std::deque<Student> d {s1, s2, s3};
    std::vector<Student> v {convert<std::vector<Student>>(d)};
    std::list<Student> l {convert<std::list<Student>>(d)};
    show(d);
    show(v);
    show(l);
}
*/
}
