# Make Your Work With PowerPoint Easier
Python web application to customize PowerPoint templates including setting and removing of custom colors and removing default margins in placeholders.
## Table of contents
* [General info](#general-info)
* [Functionalities](#functionalities)
* [Technologies](#technologies)
* [Setup](#setup)
* [References](#references)
## General info
The application modifies the xml code in .pptx files. Due to not all PowerPoint options are available from the GUI level, adjusting presentation templates to your needs often requires the preparation of custom xml parts. These tasks tend to be time-consuming and monotonous, so their automation is important for people who design presentation templates. Currently, the application allows to set and remove custom colors and remove default margins in placeholders. Although, PowerPoint allows to set only 10 colors constituting the main palette named Theme Colors, but by adding custom xml part the palette can be increased by another 51 colors named Custom Colors. These colors can also be removed only by modifying xml. Another modification is needed to remove margins around text inside placeholders. This is a nuisance default setting becuase it makes graphic elements alignment difficult. Although it is possible to change the margins manually, it is necessary to do this on each placeholder separately. Additionally, copying placeholders to the slide restores the default value. Changing the default value is possible by modifying the xml code.
#### Purpose and perspectives
The main goal of developing this application was to get acquainted with the Flask microframework, creation of the application architecture assuming its further development. In order to only perform the xml modification in the .pptx file, it would be more convenient to use scripts given in [ppt-automation](https://github.com/paulinakuczynska/ppt_automation) repository, than running this application on a local server. However, in order to expand PowerPoint template customization, this application might be useful. It would be worth enriching the application with the table style customization. In addition, it would be recommended before running the application on the server to create sessions and user-specific file storage, error handler and file size limit.
## Functionalities
* set custom colors
* remove custom colors
* remove default margins in placeholders
## Technologies
* Python 3.8.10
* Flask 2.0.2
* Jinja2 3.0.3
* WTForms 3.0.1
* The complete list of requirements is available in the requirements.txt file.
## Setup
* [Install Python](https://www.python.org/downloads/) 3.8.10
* Create a folder for the project
```
$ mkdir projectname
```
* Clone a repository on your computer
```
$ cd projectname
$ git clone https://github.com/paulinakuczynska/mywwppe.git
```
* Create a [Python virtual environment](https://flask.palletsprojects.com/en/2.1.x/installation/). This step is optional, but allows to keep dependencies in a separate place, so it ensures no conflicts with other Python projects on your computer
```
$ python3 -m venv venv
```
* Activate a virtual environment
```
$ . venv/bin/activate
```
* Install dependencies from requirements.txt 
```
pip install -r /path/to/requirements.txt
```
If any problem with that installation you can get help [here](https://stackoverflow.com/questions/7225900/how-can-i-install-packages-using-pip-according-to-the-requirements-txt-file-from), or install packages separately:
```
$ pip install Flask
$ pip install flask-wtf
```
* In the project folder set the FLASK_APP environment variable 
```
$ export FLASK_APP=run.py
``` 
and run the application with 
```
$ flask run
```
Due to that launching the application and its environment is necessary each time it is started, it is convenient to create an alias, e.g.
```
FLASK_APP=run.py FLASK_ENV=development flask run
```
## References
* [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/)
* [The New Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* [Best practices on configuring Flask](https://hackersandslackers.com/configure-flask-applications/)
* [OOXML Hacking](https://www.brandwares.com/bestpractices/category/xml-hacks/) by John Korchok
* Al Sweigart. Automate the Boring Stuff with Python, 2nd Edition: Practical Programming for Total Beginners, 2021.
* Preserve namespaces when parsing xml in [Stack Overflow](https://stackoverflow.com/questions/54439309/how-to-preserve-namespaces-when-parsing-xml-via-elementtree-in-python)
