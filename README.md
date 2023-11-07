# AirBnB clone project

In this project, we are cloning [AirBnB](https://www.airbnb.com/) website with its basic functions and usage.
We use python as the main programming language for developing.
In terms of storage system in this project, we use two formats: JSON file and MySQL DBMS, firstly, we use JSON and later on we will use MySQL for store website data efficiently.
Our main purpose is to be able to build the core of AirBnB from scratch making use of OOP princples using python. 

## Overview

Our project is consisting from mutliple parts and systems integrated together to have the work done, so let us get through each one of them:    

**1. The console**
- creating our data model
- managing (create, update, destroy, etc) objects via a console command interpreter
- storing and persisting objects to a file (JSON file)      
![first-img](./imgs/first.png)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.
This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console will be a tool to validate this storage engine

**2. Web Static**
- using HTML/CSS
- creating the HTML of our application
- creating template of each object
![second-img](./imgs/second.png)

**3. MySQL Storage**
- replacing the file storage by a Database storage
- mapping our models to a table in database by using an O.R.M.
![third-img](./imgs/third.png)

**4. Web framework - templating**
- creating our first web server in Python
- making our static HTML file dynamic by using objects stored in a file or database
![fourth-img](./imgs/fourth.png)

**5. RESTful API**
- exposing all our objects stored via a JSON web interface
- manipulating our objects via a RESTful API
![fifth-img](./imgs/fifth.png)

**6. Web dynamic**
- using JQuery
- loading objects from the client side by using our own RESTful API
![sixth-img](./imgs/sixth.png)


## Getting Started

### Dependencies

**1. Platforms**
- Python 3.x
- Linux OS (Ubunut 20.04 LTS preferable)


**2. Packages**
- cmd
- uuid
- datetime


### Installing

**1. clone the repo locally**
```
git clone https://github.com/jomanaehabb/AirBnB_clone.git
```
**2. get into the root directory**
```
cd AirBnB_clone
```
**3. run the console**
```
./console.py
```

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues will be welcomed by making pull request for us to review and once it is approved, changes will be commited into *master* branch immediately
<!-- ```
command to run if program contains helper info
``` -->

## Authors

Contributors names and contact info

* Ahmed Eldeeb  
 [@Linkedin](https://www.linkedin.com/in/ahmedsabrieldeeb/), [@X](https://twitter.com/AhmedEl52390142)

* Nour Ibrahim
[@Linkedin](https://www.linkedin.com/in/nourmibrahimmbs/), [@X](https://twitter.com/NourIbrahim1290)


## Version History

* 1.0
    * Initial Release

<!-- ## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details -->

## Acknowledgments

Concepts, Inspiration, code snippets, etc.
* [cmd in depth](http://pymotw.com/2/cmd/)
* [official uuid](https://docs.python.org/3.8/library/uuid.html)



## Summary
The `HBNBCommand` class is a command-line interface that allows users to interact with the program for testing and administrative purposes. It provides functionalities such as creating new instances, showing instance details, destroying instances, listing all instances, updating instance attributes, and exiting the program.

## Example Usage
```python
# Create a new instance of BaseModel and save it
(hbnb) create BaseModel
# Output: <new instance id>

# Show the details of an instance based on the class name and id
(hbnb) show BaseModel <instance id>
# Output: [BaseModel] (<instance id>) <instance details>

# Destroy an instance based on the class name and id
(hbnb) destroy BaseModel <instance id>
# Output: None

# List all instances or instances of a specific class
(hbnb) all
# Output: [<instance 1 details>, <instance 2 details>, ...]

(hbnb) all BaseModel
# Output: [<instance 1 details>, <instance 2 details>, ...]

# Update an instance attribute based on the class name, id, attribute name, and value
(hbnb) update BaseModel <instance id> <attribute name> <value>
# Output: None

# Exit the program
(hbnb) quit
```

## Code Analysis
### Main functionalities
- Creating a new instance of a specified class and saving it to a JSON file
- Showing the details of an instance based on the class name and id
- Destroying an instance based on the class name and id
- Listing all instances or instances of a specific class
- Updating an instance attribute based on the class name, id, attribute name, and value
- Exiting the program
___
### Methods
- `do_create(self, line)`: Creates a new instance of a specified class, saves it, and prints the id.
- `do_show(self, line)`: Prints the string representation of an instance based on the class name and id.
- `do_destroy(self, line)`: Deletes an instance from the JSON file based on the class name and id.
- `do_all(self, line)`: Prints the string representation of all instances based on the class name (optional).
- `do_update(self, line)`: Updates an instance in the JSON file based on the class name, id, attribute name, and value.
- `do_EOF(self, line)`: Exits the program by pressing Ctrl+D.
- `do_quit(self, line)`: Exits the program by typing 'quit'.
- `emptyline(self)`: Does nothing when pressing Enter.
___
### Fields
- `prompt`: The prompt displayed in the command-line interface.
- `class_dict`: A dictionary mapping class names to their corresponding classes.
___
