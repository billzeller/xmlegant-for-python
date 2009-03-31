#!/bin/bash

sudo python setup.py register

sudo python setup.py sdist upload
sudo python setup.py bdist_egg upload
sudo python setup.py bdist_wininst upload
