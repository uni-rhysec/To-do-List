# To-Do List Application - Design Document

**Team Name**: _________________

**Team Members**: _________________

**Date**: _________________

---

## 1. Requirements Analysis

### 1.1 Research Notes
After exploring existing to-do list applications (Microsoft To-Do, Trello, GitHub Projects, etc.), we observed the following common features:

**What can these applications do?**
- add and remove elements in list
-
-

**What data do they store?**
- task
- task desc.
- date due

**How do they display data?**
- GUI element list
- 
-

---

### 1.2 Essential Features
List the features your to-do list MUST have to be functional:

1. add tasks
2. remove tasks
3. display tasks in list
4. store file representing list of tasks
5.

**Why are these essential?**


---

### 1.3 Desirable Features
List nice-to-have features that would enhance the application but aren't strictly necessary:

1. GUI
2. edit tasks
3. task order, e.g. reverse, newest, oldest
4. mark as complete without deleting

---

## 2. Data Structure Design

### 2.1 Task Data
What information does each individual task need to store?

| Data Field | Data Type | Purpose          | Example          |
|------------|-----------|------------------|------------------|
| name       | string    | name of task     | Go shopping      |
| desc.      | string    | desc. of task    | Morrisons        |
| date due   | string    | date due         | 2025-10-30 20-00 |
| complete   | bool      | if task complete | false            |

---

### 2.2 Task List Structure
How will you store the collection of tasks?

**Chosen Structure** (e.g., list of dictionaries, list of lists, list of tuples):
list of dictionaries

**Why did you choose this structure?**
class unnecessary for task structure
list appropriate for list of tasks

**Example of your data structure with 2-3 sample tasks**:
```python
# Write your example here




```

**How will you access specific fields?** (e.g., for list of dicts: `task["description"]`)


---

## 3. Input/Output Design

### 3.1 Keyboard Input
What inputs will need to be provided?

| Input Type    | When Required | Validation Needed   |
|---------------|---------------|---------------------|
| string        | | |
| date (string) | new task      | correct date format |
| | | |


---

### 3.2 Screen Output
How will you display information?

**Menu Design**:
```
[Sketch your main menu here]




```

**Task Display Format**:
```
[Show how you'll display a list of tasks]




```

---

### 3.3 File I/O
How will you handle file operations?

**File format** (CSV, JSON, plain text, etc.):
JSON

**Why this format?**
easy serialisation and deserialization of dict lists in python

**Example of file structure**:
```
[Show what your saved file will look like]




```

**When will you load data?**
program start

**When will you save data?**
after all updates to data

---

## 4. Program Flow

### 4.1 Main Loop Structure
Describe or draw a flowchart of how your program will run:

```
[Pseudocode or description of main loop]
1.
2.
3.
4.
```

---

### 4.2 Error Handling
What could go wrong, and how will you handle it?

| Potential Error | How to Handle |
|----------------|---------------|
| File doesn't exist | create new to-do list if file doesn't exist |
| Invalid user input | repeat input request |
| Empty task list | no tasks can be removed, suggest adding tasks |
| | |

---

## 5. Function Specifications

For each function your team will implement, specify:
- Function name
- Purpose
- Parameters (with types)
- Return value (with type)
- Brief description of what it does

### Example:
```python
def add_task(task_list, description, priority):
    '''
    Add a new task to the task list.

    Parameters:
        task_list (list): The list of all tasks
        description (str): The task description
        priority (str): Priority level ('high', 'medium', 'low')

    Returns:
        list: Updated task list with the new task added
    '''
    pass
```

### Your Functions:

- /get date input
	- gets a date in the required format e.g. YYYY/MM/DD HH:MM
	- wrong format -> keep requesting date unless provided escape input given (e.g. "cancel" or something)
	- return double (2-tuple) with string containing valid date and bool representing validity (cancelling operation invalidates the string)
- save
	- save list to file using json
	- no return
- load
	- load file and deserialise input into list
	- no return
- display
	- display to-do list in string format
	- include 1-based indices
	- no return
- /main
	- gives user options to add, display, close, etc.
	- invalid input -> repeat prompt
	- when operation completed, repeat prompt
	- no return
- add
	- ask user for task name
	- ask for task desc.
	- ask for due date using `get date input`
	- if the date is invalid cancel the operation
	- no return
- modify
	- select task using 1-based index
	- looping menu like in `main`
	- allow options to remove the task; change the task description, name, or date; or complete the task
	- no return
- (optional) complete
	- select task using 1-based index
	- completes task
	- shortcut for using `modify` and then completing the task
	- no return
- select_task
	- called in `complete` and `modify`
	- ask user for 1-based index of task
	- if index outside of task range repeat input request
	- returns the _0-based_ index of the task

**Function 1:**
```python




```

**Function 2:**
```python




```

**Function 3:**
```python




```

**Function 4:**
```python




```

**Function 5:**
```python




```

**Function 6:**
```python




```

*(Add/ remove functions as needed)*

---

## 6. Peer Feedback Record

### Feedback Received (from other team):
**Date**: _________  **Reviewing Team**: _________________

**Strengths of our design**:
-
-

**Suggestions for improvement**:
-
-

**Changes we made after feedback**:
-
-

---

### Feedback Given (to other team):
**Date**: _________  **Team Reviewed**: _________________

**What we liked**:
-
-

**Constructive suggestions**:
-
-

---

## 7. Design Decisions Log

As you work through the design, record important decisions and why you made them:

| Decision | Options Considered | Final Choice | Reasoning |
|----------|-------------------|--------------|-----------|
| | | | |
| | | | |
| | | | |

---

## 8. Next Steps

Before starting implementation, make sure:
√X
- [ ] All team members understand the data structure
- [ ] All function signatures are agreed upon
- [ ] Everyone knows which functions they will implement
- [ ] Git repository is set up and all members have access
- [ ] Branch naming strategy is agreed
- [ ] Testing approach is discussed (Next week's class will cover this)

**Ready to code?** Make sure all boxes are ticked!