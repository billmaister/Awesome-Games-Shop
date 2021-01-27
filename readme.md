# Project Plan

## 1. Team Members
* Sergei Kaukiainen 586773
* Aapo Linjama 587895
* Oskari Mäkinen 477510

## 2. Features
* Authentication - register, login, logout
* Buying games - via mockup payment service
* Search for games and filtering by category
* Adding games 
* Game/Service interaction - highscores, (saving/loading?)
* Security - players can only play games that they have purchased, only developers are allowed to make changes in their game, secure from injection attacks etc.
* Statistics - what games have been bought and when

## 3. Extra Features
First we plan to concentrate on mandatory features which are listed in the previous section and after that on the extra features that are listed in the project description. Outside those we are not planning to implement anything extra.

## 4. Implementation plan for features
* Authentication - Implemented with Django auth
* Payment - external Simple Payments service
* Search and filtering categories - different database queries
* Security - Heroku provides HTTPS, avoiding vulnerabilities in web page inputs (SQL-injection), clean up HTML before using (Cross-site scripting) this is provided mostly by Heroku
* URLs - Python module (Django) which maps URL path expressions to Python functions (Django views)
* Adding games - URL to a file which contains HTML and links to JavaScript files. Game is shown to players via iframe
* Requests - Are handled in views (Django) which fetch objects from the database, modify those objects if needed, render forms, return HTML etc. and return web responses
* Game/Service interaction - done via Ajax calls
* Statistics - combination of basic database (SQL) and JavaScript/Python

## 5. Plan of Working
At first we plan to work remotely until 15.01. and after that meet face-to-face at least once a week. We plan to do implementation at home and discuss general planning and decisions during the meetings.

## 6. Models We Plan to Use
* User (Provided by Django)
* Game
   - id
   - developerID
   - name
   - link
   - price
* GamePurchase
   - gameID
   - userID
   - date
* Score
   - gameID
   - userID
   - date
   - score

## 7. Timetable
* 2.1. Begin implementation
  - Work remotely until 15.1.
  - Set up Django project
  - Make skeleton for website
  - Create initial models
  - Create views
  - Authentication
  - Implement player UI
  - Implement developer UI
* 10.2. All mandatory requirements implemented
  - Implement extra features
* 14.2. Final deadline
# Awesome-Games-Shop
