.. bizarro documentation master file, created by
   sphinx-quickstart on Mon Apr  8 17:37:56 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to bizarro's documentation!
===================================

Bizarro is a python library for Facebook Messenger Bot. It's basic task is to help developers creating payloads for Facebook Messenger Bot.
Facebook has different templates and buttons for their Messenger Platform. However, it's extremely tedious to write the payload every time. Bizarro here can help you to write awesome bot without
worrying about the payload. All you need to do is send the necessary text inputs and bizarro's function will return the appropriate payload for you.
Bizarro takes help of one of my other python package - __Zathura__, (A sqlite3 logger I wrote for one of my package).
Currently, the library is in alpha version.

**************
How to Install
**************
It's a pypi package (https://pypi.org/project/bizarro/). So::

    pip install bizarro

***************
Current support
***************
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

************************
How to work with bizarro
************************

Suppose you want to send user a simple "Hello"::

    from bizarro.utility.util import Utility

    echo_text = bizarro_utility().basic_text_reply_payload(fb_user_id, message="Hello")

now all you have to do is, send the payload __echo_text__ with your page_access_token.
Code examples are coming soon.

********
Contents
********

.. toctree::
   :maxdepth: 2

   buttons



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
