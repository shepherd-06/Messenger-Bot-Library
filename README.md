# Messenger Bot Library [![Build Status](https://travis-ci.org/p1r-a-t3/Messenger-Bot-Library.svg?branch=master)](https://travis-ci.org/p1r-a-t3/Messenger-Bot-Library)

Messenger Bot Library (formerly known as bizarro) is a python library for Facebook Messenger Bot. Its basic task is to help developers creating payloads for Facebook Messenger Bot.
Facebook has different templates and buttons for its Messenger Platform. However, it's extremely tedious to write payload every time. This library is here to help you build a bot without worrying about the payload. All you need to do is send the necessary inputs and this library will return the appropriate payload for you.

## How to Install

It's a [PyPI package](https://pypi.org/project/messenger-bot-library/).

`pip install messenger-bot-library`

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
    3) ~~List Template~~ ([List Template was deprecated on July 29, 2019](https://developers.facebook.com/docs/messenger-platform/send-messages/template/list/))

Attachment sending is not enabled in any other buttons or template right now. They will be rolled out in upcoming versions.

## Documentation

[The documentation of this project is on the wiki page.](https://github.com/p1r-a-t3/Messenger-Bot-Library/wiki)
