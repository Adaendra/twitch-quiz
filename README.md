# Twitch-Quiz

Project made to test Python and Vue.js. There are no ambitions to do other releases after. So feel free to fork the code.

## Description
Do you like to play quiz?

Now you can do it on stream with your viewers!

<br/>

---

## Configuration

- First, in your setting account, you must enable the MultiFactor Authentication.
- Then, declare the application in the Twitch dev console: https://dev.twitch.tv/console/apps/create
- Get the clientId and change the value in the **user_configs.json** file, **clientId** parameter. 
- Get the clientSecret and change the value in the **user_configs.json** file, **clientSecret** parameter. 

*Update the settings part to use a cool interface*

<br/>

### How-to run
*From the main project folder.*
> $env:FLASK_APP = "server"
>
> flask run

<br/>


---

## Backend
[![Generic badge](https://img.shields.io/badge/Language-Python%20Flask-303f9f.svg)](https://shields.io/)

[Documentation](documentation/backend.md)

## Frontend
[![Generic badge](https://img.shields.io/badge/Language-Vue.js-303f9f.svg)](https://shields.io/)

[Documentation](documentation/frontend.md)
