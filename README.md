#Catalog

Web application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. Download,installed Git from git-scm.com.](http://git-scm.com/downloads) Install the version for your operating system.
2. VirtualBox is the software that actually runs the VM. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads)  Install the *platform package* for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.
3. Download and install Vagrant 2.2.0
4. Download Vagrantfile and run:

'''
$ git clone https://github.com/udacity/fullstack-nanodegree-vm.git FSND_VM
$ cd FSND_VM/vagrant
$ vagrant up
$ vagrant ssh

'''

### Installing

**Windows:** Use the Git Bash program (installed with Git) to get a Unix-style terminal.  
**Other systems:** Use your favorite terminal program.

From the terminal :
1. make shure you are start the virtual by vagrant up and log in by ssh then ''' cd /vagrant '''
2. clone this repo 
'''
git clone https://github.com/hadeelkh/Catalog.git
'''

## Running the tests

1. run  model.py to initialize the database
'''
python model.py
'''
2. run lotsofmenus.py to populate the database with categories and thire items
'''
python lotsofmenus.py
'''
3. then run the Flask web server
'''
python application.py
'''
4. Access and test the application by visiting http://localhost:5000

## Authors

* **hadeel khaled** - *Initial work* - [hadeelkh](https://github.com/hadeelkh)
