[![Build Status](https://travis-ci.com/p1r-a-t3/bizarro.svg?token=CfEhnav87YzYRHHfKnNf&branch=master)](https://travis-ci.com/p1r-a-t3/bizarro)  [![CircleCI](https://circleci.com/gh/p1r-a-t3/bizarro.svg?style=svg&circle-token=00c9babf5256214ac6a5fd895dcca5ac1ed63fe4)](https://circleci.com/gh/p1r-a-t3/bizarro)
[![python](https://img.shields.io/badge/python-3-blue)](https://img.shields.io/badge/python-3-blue) [![Documentation Status](https://readthedocs.org/projects/bizarro/badge/?version=latest)](https://bizarro.readthedocs.io/en/latest/?badge=latest)

```
 .o8        o8o
"888        `"'
 888oooo.  oooo    oooooooo  .oooo.   oooo d8b oooo d8b  .ooooo.  
 d88' `88b `888   d'""7d8P  `P  )88b  `888""8P `888""8P d88' `88b
 888   888  888     .d8P'    .oP"888   888      888     888   888
 888   888  888   .d8P'  .P d8(  888   888      888     888   888
 `Y8bod8P' o888o d8888888P  `Y888""8o d888b    d888b    `Y8bod8P'
```

# Bizarro

=======================================
Bizarro is a python library for Facebook Messenger Bot. It's basic task is to help developers creating payloads for Facebook Messenger Bot.
Facebook has different templates and buttons for their Messenger Platform. However, it's extremely tedious to write the payload every time. Bizarro here can help you to write awesome bot without
worrying about the payload. All you need to do is send the necessary text inputs and bizarro's function will return the appropriate payload for you.
Bizarro takes help of one of my other python package - __Zathura__, (A sqlite3 logger I wrote for one of my package).
Currently, the library is in alpha version.

## How to Install

It's a pypi package (https://pypi.org/project/bizarro/). So

`pip install bizarro`

## Current support

Right now, bizarro has support for the following 

1) Echo Back (Simple text reply)
2) Quick Reply
3) Typing On
4) Marked Seen
5) Button
    1) Postback Button
    2) Url Button
    3) Call Button
6) Template
    1) Button Template
    2) Generic Template
    3) List Template

Attachment sending is not enabled in any other buttons or template right now. They will be rolled out in upcoming versions.

## How to work with bizarro

Suppose you want to send user a simple "Hello"

```from bizarro.utility.util import Utility

echo_text = bizarro_utility().basic_text_reply_payload(fb_user_id, message="Hello")
```

now all you have to do is, send the payload __echo_text__ with your page_access_token.
Code examples are coming soon.

----------------------------------
Thank you, Ibtehaz, December 09, 2019
