Original project plan can be found here
Working App in Heroku can be found [here](https://mostawesomegames.herokuapp.com/home/)

## 1. Team Members
* Sergei Kaukiainen 
* Aapo Linjama 
* Oskari Mäkinen 

## 2. My workload in this project
* Web site appearance
* Contributing to the software architecture design, database design and basic functionalities
* Appearance and mechanism for highscores
* Email verification
* 3rd party login
* Heroku deployment

## 3. Features
* Authentication - register, login, logout
* Buying games - via mockup payment service
* Basic user and developer functionalities
* Payment - external Simple Payments service
* Search for games and filtering by category
* Adding games 
* Game/Service interaction - highscores, (saving/loading)
* Security - players can only play games that they have purchased, only developers are allowed to       make changes in their game, secure from injection attacks etc.
* Statistics - what games have been bought and when
* 3rd party login - signing with google account
* RESTful API

## 4. Instructions
When testing our app locally:
1. Firstly install these:
```
 pip install six
 pip install django-allauth
 pip install djangorestframework
```
And you need 
```
 Python 3.6 or newer
 Django 3.0.2
``` 

2. Create admin (superuser) for app and add necessary settings for 3rd party login
- Note: For the deployed app use the domain instead of localhost

- In the project root folder is a text file called gmail.txt where you will find Client
ID and Client Secret -key. You need to add these to admin page in order 3rd
party login (gmail login) to work.

- In admin page first go to sites -> click example.com and change Domain
name to “localhost:8000” and Display name to whatever you want (for
example “Gmail login”). Save changes.

- Then in admin home page go to Social applications -> “Add social
application”. New page will open after this. Choose from Provider drop menu
“Google”, name application as you want and from gmail.txt file add Client id
and Secret key. Lastly in Sites, move “localhost:8000” from Available sites to
Chosen sites. Save changes and you are good to go with the app.

- In the admin page you can also add a profile for your superuser (player or
developer). You need to create a devProfile if you want to add games and
receive payments.

- To add our test game to the service use
https://localhost:8000/play/test_game2/ as the source url

3. In the web app when you create a new account you will need to verify your account
via a link that is sent to your email. Since we are using Django’s email backend, you
will find this link in the console. You can also activate a user’s account in the admin
page.

**When testing in Heroku:**
Link to Heroku: https://mostawesomegames.herokuapp.com/home/

For testing purposes we have created one superuser and one developer account to which
we added given example game. Login infos:
- Superuser:
   - Username: admin
   - Password: salasana1234
- Developer account:
   - Username: dev
   - Password: salasana1234
   
- If you want to add additional developers to the deployed app, create a player user
and then create a DevProfile and Profile for the user through django admin. (Since
the verification email is sent to console backend)


