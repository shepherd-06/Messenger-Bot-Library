#!/usr/bin/env bash

python3 -m unittest Tests.test_quick_reply
python3 -m unittest Tests.test_basic
python3 -m unittest Tests.test_button_template
python3 -m unittest Tests.test_generic_template
python3 -m unittest Tests.test_list_template.py