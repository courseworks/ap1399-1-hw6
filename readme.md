<center>
<h1>
In The Name Of ALLAH
</h1>
<h2>
Advanced Programming - Homework 6
</h2>
<h2>
Dr.Amir Jahanshahi
</h2>
<h3>
Deadline: Friday, 21 Azar - 23:00
</center>

<img src="stuff/f1.png" width="400" />


# Introduction
In this homework we would have a simple exercise of **STL** in C++ and a simple start in Python.

# C++
After seeing how STL can make our lives easy, we've decided to do some usual tasks of our university by STL. So we need **Student** class with the following description.

```c++
class Student{
    public:
        long id{};
        double avg{};
        size_t units{50};
        Student (long _id, double _avg, size_t _units);
};
```

Based on the application, we would need to use vector, deque or list as our container. So, ```convert``` function would convert containers for us. In other words, this function creates a new container with our desired type from an existing container. You can see gtests for its usage.

You must implement the following functions too:

*  ```show```

    This function can accept any of the mentioned containers as argument and shows them like the following.

```c++
Student s1 {9423013, 18.2, 26};
Student s2 {9423037, 19.2, 30};
Student s3 {9423091, 19.1, 10};
std::deque<Student> d {s1, s2, s3};
std::vector<Student> v {convert<std::vector<Student>>(d)};
std::list<Student> l {convert<std::list<Student>>(d)};
show(d);
show(v);
show(l);
```

The output should be 

<img src="stuff/f3.png" width="500px">

*  ```findRank```

    This function gets a container and a number *n* and returns the n'th student based on averages. You can see it's behavior in gtests.

*  ```getRanks```

    This function gets a container and sort its students based on their averages and returns the container. So the first student of this sorted container would be the one with highest average.

*  ```getInterns```

    In orther to qualify students for the internship, we need to sort them based on their units in descending orther. We need this function for this purpose. 

## Note
You are not allowed to use **any** loops (for, while, etc.) in this homework. Using a loop may cost you some points!

<img src="stuff/f2.jpg" width="400" />


# Python
Time to start python. We want to implement a football league.
There are 4 classes you should implement.

1. Match

    In this class you get a string in form of ‘ team1_name  team1_goals  -  team2_goals  team2_name  ’. all sections are separated by some spaces and maybe there are some spaces at the beginning and the end of string. It is guaranteed that there isn't any space in team names. This class has 4 instance variables:

    *  home: The name of the first team (team1_name in string)
    *  away: The name of the second team (team2_name in string)
    *  home_goals: Number of goals for the first team (team1_goals in string)
    *  away_goals: Number of goals for the second team (team2_goals in string)

    This class has only one method: ```data()```.
    In this method you should return two tuples! Each tuple shows how much each team changed in the standing! 
    For example if the input be ```‘   A     5 -    2  B’```, you should return these tuples: ```
(1,1,0,0,5,2,3,3),(1,0,0,1,2,5,-3,0)```
    The first element of each tuple is number of match played and it is always 1! The 3 next elements represent win, draw and lose. One of these 3 elements is 1 and the two others are 0. The 5-th and 6-th elements show number of goals for the team and against the team. The next one is difference between 5-th and 6-th elements and last one is points. Each team get 3 points for each win, 1 for each draw and 0 for each lose. 
    Of course if we print an object of this class, you should print a string just input string in beautiful manner. Like this: 

    ```est 1 - 3 per```

1. Weeks

    This class represents each week in the league. Each week is determined with a number and a list of matches object that comes as input! Of course, list of matches object is optional!

    So to store all matches we need to have one method to get one match and add it to the list! But there is one condition: There must not exist a team in 2 matches of one week! For cleaner code we suggest you study about **for else** in python and code it. Explain about it in your report!

    At last, we ask you one more thing: if we print your weeks object, it must print all matches in the week.

    ```
    Esteghlal 3 - 1 Zobahan
      Nassaji 2 - 1 Peykan
      Sepahan 0 - 1 Perspolis
    ```

1. Team

    Each team can be created by a name! Also, each team has a rank in standing but at first, each object created sooner, has higher rank. Rank of first team is 1.

    Other attributes of this class are: mp(matches played), w(win), d(draw), l(lose), gf(goals for), ga(goals against), gd(goal difference) and pts(points). And each team must store list of match objects that this team has played! So we need a method to add a match object to the list. This method is ```add_match``` . Also this method should update all attributes. For example:

    <img src="stuff/f4.png">

    The first line is the match result and then comes attributes of Esteghlal, before and after adding match.
    
    For the same previous class, if we print an object it, would be like this:

    <img src="stuff/f5.png">

1. League

    This is the last class. This class gets a list of teams and a year. Here are 4 instance variables:
    *   standing
    
        It is a list of team objects in some order. Notice that at the beginning, you should sort them by their ranking. After adding week objects to the league, you should sort them by pts, gd, gf, w, name!
    
    *   weeks
    
        it is a list that store week objects of league
    
    *   year
    
        year of the league
    
    *   all_standing
    
        this list stores each standing after each week!( It must store the primary standing, when the all teams have 0 points)

    This class has a public and a private method! First method is add_week which gets a week object and stores it and updates standing by adding each match of the week to the teams and updates the standing. So we use auxiliary private function named ```add_match```. How can we define private methods or attributes? Explain it in report!

    Finally if we print this class instances, you should print standing in a beautiful manner!

    <img src="stuff/f6.png">

If you are here congratulations! For the last step we’d define the function ```read_data``` for reading from files. It gets a filename and a year number to create league object.  So we read from a file that contains some lines: 

1.  The first word is table and then is a colon symbol. Then there is a list of team names separated by some spaces. Each team name doesn’t have any extra space and is in single or double quotation.

2. First word is week and there is a number after it. It's guaranteed that numbers start from 1 and end with n*(n-1)/2 (n is number of teams) respectively. After numbers,  there is colon symbol and comes result of a match after it. Like before, there may be extra spaces be in each result of matches.

You should return a league object.

Now the homework is finished, but in the last moments someone adds some extra lines between our file names. But we guarantee the list of team names come before result of matches :)

Enjoy python! 

<img src="stuff/f25.jpg" width="600" />
