## Awards
## It's a web application that allows users to view, post and manage projects they have done for review
### 15 March 2019
#### By **[Francis T Karagu]**

## Description
It's a web application that allows users to view, post and manage projects they have done for review

## Specifications
### Who is the target User?
* Anyone who wants to view, review and post projects online

### Front-end/User Interface Logic Objectives
* By default the page will load and provide two options.
* Sign in: This section will be used to authenticate users on the application.
* Awards (Home): This is the landing page of the application.

### Back-end/Business logic Objectives
* The application is using a POSTGRES database to store data.
* Once a user has accessed the page she/he can post or review what has been posted.

### Behaviour-Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Create User | Enter username, Email and password | Activation link via email. |
| Sign In | Click on the Sign In and enter username and password | Loads the home page. |
| Admin | Click on the Admin and enter username and password | Loads the admin page. |
| Upload Projects | Click on the Upload project to view projects | Loads all projects loaded. |


## Prerequiites
    - Python 3.6 required
    - Django
    - POSTGRES

## Application link
Here is a live working link https://thashaward.herokuapp.com/

## Set-up and Installation
    - Install python 3.6
    - Install Django

    Incase you need to access / improve the application please follow the below steps
    1.  Use this command $ git clone <https://github.com/Fkaragu/Awards.git>
        This will clone the projects repository into a local folder on your device.
    2.  Open the files with an editor( preferably Atom. )
    3.  Study the code. learn from it. Improve on it.

## Known bugs
No known errors.

## Technologies used
    - Python 3.6
    - Django
    - HTML
    - Bootstrap

## Support and contact details
In case of any problems reach me through my email:fkaragu@gmail.com

### License
Copyright (c) {2019} **{Francis Thande Karagu}**
Permission is hereby granted, free of charge, to any person willing to obtain a copy of this program for personal use. However if the program will be used for commercial gain then a royalty fee will have to be paid to the author of the program.
