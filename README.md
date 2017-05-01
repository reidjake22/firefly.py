# firefly.py
This is a module to retrieve tasks from the intranet named firefly. 
The function get_tasks takes four inputs: username, password, loginURL, and tasksURL.
it returns a dictionary in form:
 {
  1 : [<d6>, <title>]
  2 : [<d6>, <title>]
  3 : [<d6>, <title>]
  4 : [<d6>, <title>]
 }
 
 the six digit number is associated with that tasks (including that number brings you to its description i.e. set-tasks/<6d>)
 The name is <title>
