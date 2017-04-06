# Welcome to the wiki!
## Quick warning
Please note, this project is a work in progress written by Python Newbies, please be gentle and use the scripts and programs contained at your own risk.

## Summery and objective
Prometheus is a python3 project that targets a Raspberry Pi running Jessie. The primary objective is to combine a Roboclaw (2x30) motor controller, a RPi(2b), a GPS chip, and other components to create a functional ground-based rover that we are calling Prometheus. This rover will be capable of autonomous movement and communication with our Airborne craft, Orion, as to seek out and tag the GPS coordinates of target objects within a level field.

## Setting up
First things first, you will need to clone this repository down to your dev Pi and checkout the desired feature branch.
   You can do this via the command 

      git clone https://github.com/MVHSRobotics2017/Prometheus.git
   and, when developing a feature, please checkout the corresponding branch

      git checkout -b <BRANCH_NAME>

Once you have the repository cloned down to your dev Pi you will need to init the projects dependencies. Currently this can be accomplished by executing the provided build scripts located in the project's root directory. Navigate into the project root directory and execute the command 

    sh makeUNIX.sh

## Setting up Git
* If you already know how to use git via the commandline to push changes to Github, you can skip this segment. 
* If you use Github desktop on Windows/Mac, you should be able to skip this segment.

To use git via the command-line, such as committing changes from a Pi's terminal, you will need to first configure an Access Token with Github. 
The Access Token is required as 2FA is enabled on this repository, and Username/password is insufficient to authenticate you.
This Access Token is used in place of your password, but only when using git via the terminal.
To generate this Access Token, please see [this link](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/).
### Please store this Token in a safe place! NEVER place it in the project workspace!
### NEVER commit your Token to the repository or anywhere online, for security reasons.

Please ensure that you are committing your changes to the desired feature branch, once a feature is reasonably done open a pull-request to merge it into master.
## NEVER commit directly to master, always target a dev branch.
