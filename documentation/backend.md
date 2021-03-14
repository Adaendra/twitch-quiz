# Twitch-Quiz Backend

## Twitch API Documentation
* Channel Points : https://dev.twitch.tv/docs/api/reference#create-custom-rewards

## Technologies
* Flask : https://flask.palletsprojects.com/en/1.1.x/
* Flask SocketIO : https://flask-socketio.readthedocs.io/en/latest/
* PyTest : https://docs.pytest.org
* Unit Testing : 
    - https://github.com/pytest-dev/pytest-mock/
    - https://docs.python.org/3/library/unittest.mock.html
    - https://code-maven.com/slides/python/pytest-class

## Commands
### Install dependencies
> pip install -r requirements.txt

### List dependencies
> python -m pip list

### Run unit tests
> pytest tests/

---

## Features
### 1 - Play
#### 1.1 - Generate quiz
[![Generic badge](https://img.shields.io/badge/Done-1b5e20.svg)](https://shields.io/)

#### 1.2 - Start quiz
[![Generic badge](https://img.shields.io/badge/Done-1b5e20.svg)](https://shields.io/)

#### 1.3 - Stop quiz
[![Generic badge](https://img.shields.io/badge/Done-1b5e20.svg)](https://shields.io/)

#### 1.4 - Add player
[![Generic badge](https://img.shields.io/badge/Done-1b5e20.svg)](https://shields.io/)

#### 1.5 - Player answer
[![Generic badge](https://img.shields.io/badge/Done-1b5e20.svg)](https://shields.io/)

#### 1.6 - Calculate rankings
[![Generic badge](https://img.shields.io/badge/TODO-b71c1c.svg)](https://shields.io/)

#### 1.7 - Calculate stats
[![Generic badge](https://img.shields.io/badge/TODO-b71c1c.svg)](https://shields.io/)

#### 1.8 - Next answer
[![Generic badge](https://img.shields.io/badge/Done-1b5e20.svg)](https://shields.io/)

#### 1.9 - Use Joker
[![Generic badge](https://img.shields.io/badge/TODO-b71c1c.svg)](https://shields.io/)

* Copy the response of someone
* Copy the response of the majority
* Skip the question

### 2 - Configure Options
#### 2.1 - Game Type
[![Generic badge](https://img.shields.io/badge/TODO-b71c1c.svg)](https://shields.io/)

* Limited number of questions : The quiz will end after X questions
* King of the kill : The quiz will end when only one person survive. (or zero if every last players fail simultaneously)

#### 2.2 - Player Options
[![Generic badge](https://img.shields.io/badge/TODO-b71c1c.svg)](https://shields.io/)

* Lives : Number of lives for each player (0 = infinite). In a King of the hill mode, must be at least 1.

#### 2.3 Question duration
[![Generic badge](https://img.shields.io/badge/TODO-b71c1c.svg)](https://shields.io/)

* Time 
* Event

### 3 - Events
#### 3.1 - Send event to external elements
[![Generic badge](https://img.shields.io/badge/TODO-b71c1c.svg)](https://shields.io/)

Send event to external elements to have a light animation or this kind of events.
