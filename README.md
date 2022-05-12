## Dataset description 
You have a table called students that represents a daily schedule of each student in a school (suppose all students have the same schedule every day).
Table contains the following columns:
1. **student_id** [int] -- unique identifier of a student.
2. **class** [str] -- name of the class each student attends in this particular order. Can take one of the following values: _'english', 'math', 'history', 'chemistry', 'gym', 'civics', 'writing', 'engineering'_
3. **grade** [int] -- final grade of a student for a particular class.

| student_id | class| grade | 
|---|---|---|
| 0 | engineering | 86 |
| 0 | chemistry | 75 |
| 1 | math | 85 |
| 1 | engineering | 0 |
| 1 | english | 73 |
| 1 | history |81 |
| 2 | math | 12 |
| 2 | history | 81 |
| 2 | gym | 79 |
| 2 | english | 5 |

<br>

## Task description
You have a theory that the sequence of class-to-class transitions affects students' grades. For instance, you suspect student #1 would do better in his engineering class if it immediately followed his english class instead of his math class.

1. Write a function to determine the average and median grade for groups of students based on the class they have immediately prior to a given class. Also report how many students fall into each group. How would you interpret the results? 

[BONUS]
<br>

2. Add support of command line arguments. Make sure the script can be run from command line and the following two arguments can be specified: 
    - path to the .csv file
    - name of the target class

3. Run your application inside of a docker container.

Good luck!!!