# School Lunch Management System - SLMS
*The School Lunch Management System (SLMS)* is a web application that intends to help elementary schools efficiently participate in their county's school lunch program.

This web application is written in Python and utilizes the Django framework.  See the *Getting Started* section for information how to run the application locally.

- [School Lunch Management System - SLMS](#school-lunch-management-system---slms)
  - [Goals and Overview](#goals-and-overview)
  - [Getting Started](#getting-started)
    - [Install Python](#install-python)
    - [Install Django](#install-django)
    - [Clone this Repo](#clone-this-repo)
    - [Make migrations and run the server](#make-migrations-and-run-the-server)
  - [Navigation and Use](#navigation-and-use)
    - [New User Registration and Log in](#new-user-registration-and-log-in)
    - [User Dashboard](#user-dashboard)
    - [Lunch Selections](#lunch-selections)
    - [People](#people)
    - [Snack Dashboard](#snack-dashboard)
    - [Log out](#log-out)

## Goals and Overview
* The elementary school requires their students to choose a lunch type for each day that they are attending:
  * *hot lunch* (served by the cafeteria)
    * Also required to select *parent attendance* with this lunch type 
  * *cold lunch* (brought with them from home)
  * *field trip lunch* (on days they are participating in a field trip and would like a lunch provided)
* Students can reference the county's lunch calendar (link on the school website) to reference upcoming lunch details.
* The school tracks lunch selections to ensure lunches prepared and space available is adequate.  
* Teachers track student selections as needed. 
* Snacks are distributed during school days by staff who can:
  * Create new *snack counts* detailing the distribution.
  * Add new *snack foods* available for distribution.
* Users may follow other users to be notified of their lunch selections.
* Users may "like" lunch selections made by other users.
## Getting Started
### Install Python
Open a terminal and type `python`.  If you see something like `Python 3.8.5...`, then Python is installed.  If not, then [download Python](https://www.python.org/downloads/) and install it.
### Install Django
Install Django using pip by running the following in the terminal `pip install "Django==3.0.*"`.  Check that it was successful by typing `python` into the terminal prompt, importing Django, and then checking the Django version:
````
import django
django.get_version()
````
If you get a response like `'3.0.10'`, you've successfully installed Django.
### Clone this Repo
[Clone this repository](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository) to a location where you want to house the files.
### Make migrations and run the server
From the terminal, change to the `slms` directory where you cloned the repository files.  In the terminal, run `python manage.py migrate` to create the associated tables for the application.  Once complete, run `python manage.py runserver` to start the local server, and navigate in a browser to http://127.0.0.1:8000/ where you should see SLMS running.
## Navigation and Use
The information below provides new users to the SLMS system with direction on how to get started.
### New User Registration and Log in
New users to the system can register for an account by clicking the *Register here* link where they'll be asked to create an account as shown below.

![Register](account/static/images/CreateAccount.png)

Once registered, users can enter their username and password and then press the Log-in button to enter SLMS via the Log-in screen:
  
![Log in](account/static/images/Login.png)

Users also have the option to indicate that they've forgotten their password by clicking the *Forgot password?* link.  They'll be asked to enter the email used when registering their account so that a password reset email may be sent to them.  

![Forgot password](account/static/images/ForgotPassword.png)

### User Dashboard
Once a user is logged into SLMS, they are greeted by the User Dashboard screen where they'll be able to see the activity of the users they've chosen to follow:

![User Dashboard](account/static/images/UserDashboard.png)

From here, users can select the *edit your profile* link to edit their account details: 

![Edit Profile](account/static/images/EditAccount.png)

Users can also select the *change your password* link to change their current account password.

![Change password](account/static/images/ChangePassword.png)

### Lunch Selections
Student users can create a lunch selection for the day by first clicking on *Selections* in the top navigation bar where they'll be presented with the view of recent selections that have been made by SLMS users.  They can then click on the *create a new selection* link where they can fill in the details and publish their selection by selecting the *Make Selection* button.

![Make selection](account/static/images/MakeSelection.png)

From the *Selections made* page, a user can click on any of the selections listed to see it's details.  From the detail view, they can click the *Like* button to like the selection.

### People
Users may view the listing of SLMS users by selecting the *People* link in the top navigation bar.  They may then click on a user to see their follower count, as well as their recent activity.  They can follow that user by clicking the *Follow* button.

![User detail](account/static/images/PeopleDetail.png)

### Snack Dashboard
When a **Staff User** is logged into SLMS, they are presented with a slightly different navigation bar indicating that they also have a *Snack Dashboard* navigation option.

![Snack Dashboard Nav](account/static/images/Nav.png)

By clicking on the *Snack Dashboard* link, a user is presented with the view of recent snack counts that have been made by staff along with links to *create a new snack count* and to *view available snack foods*.

![Snack Dashboard](account/static/images/SnackCountDashboard.png)

Clicking on a snack count takes the user to the count's details, and clicking the *Edit* link for a snack count allows the user to edit the count's details (if they are the user who created the count).

![Edit Snack Count](account/static/images/EditSnackCount.png)

By selecting the *create a new snack count* link, a user is presented with the snack count form where they can fill in the details and create the snack count by pressing the *Create Count* button.

![Snack Count](account/static/images/CreateSnackCount.png)

By selecting the *view available snack foods* link, a user is presented with the *Snack Food Dashboard* where they can view the listing of snack foods.

![Snack Food Dashboard](account/static/images/SnackFoodDashboard.png)

Clicking on a food takes the user to the food details.

![Snack Food Detail](account/static/images/SnackFoodDetail.png)

Clicking the *Edit* link on a snack food allows the user to edit the food's details.

![Edit Snack Food](account/static/images/EditSnackFood.png)

Clicking the *create a new snack food* link allows the user to create a new snack food item by providing valid inputs and selecting the *Create Food* button.

![Create Snack Food](account/static/images/CreateSnackFood.png)

### Log out
Users can log out of SLMS at any time by selecting the *Logout* link in the top right section of the navigation bar.

![Logout](account/static/images/Logout.png)
