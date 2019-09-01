# Math Exam Project

## Setup
*todo*

## Structure
This section describes intended final structure and overall guidance. Upon completion it should be replaced with full documentation

### core
Anything that needs to reference multiple models. This will also contain any abstract classes and code that is shared. This breaks the Django app paradigm but should keep the project organized a bit better.

### admin


- add/remove other users
- assume other users's views
- view students's performance/individual exams
- view teacher metrics

### teacher
A teacher has control over their students and groupings (classes) of students. A teacher chooses their admin and grants that admin access to their students.

- create/assign exams
- view students's performance/individual exams
- export information

### student
A student has the least access to data, but the most control over who is allowed to view. A student's data can **only be viewed by teachers chosen by the student**

- take exam
- view exam results

### exam
- contains questions
- contains solutions (or range of solutions)