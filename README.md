## Project definition 

This project is an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Instruction

follow the instruction below to run the application successfully, If you are familiar with python and flask you might know your own way .


- Install Vagrant and VirtualBox.
- Clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm).
- Clone this project.
- Move the files and folders inside [./app/src](/app/src) to the catalog (fullstack-nanodegree-vm/vagrant/catalog/) folder, The others files is just for development purpose.
- Launch the Vagrant VM (vagrant up).
- Run the application within the VM (python3 /vagrant/catalog/application.py).
- Access and test the application by visiting [http://localhost:5000](http://localhost:5000) locally.

> Check out [this guide](README__prepare-software.md) helps you install VM ( virtual machine).


Assuming the application is running successfully, you'll see that there's no category, so you need to run "python3 /vagrant/catalog/lotsofCategory.py" to add some categories.


## third-party authentication

+ ## Google OAuth 2.0
   You need OAuth 2.0 credentials, including a client ID and client secret, to authenticate users and gain access to Google's APIs.

   After creating an OAuth Client ID download it as a JSON data file, rename the file as "client_secrets.json" and pasted into the folder [./app/src](/app/src).

   > visit [this link](https://developers.google.com/identity/protocols/OpenIDConnect) helps yous create an OAuth Client ID.

+ ## facebook OAuth 2.0
   To enable authentication with Facebook, you need a Facebook App ID, which you can create and retrieve in the [App Dashboard](https://developers.facebook.com/apps/). 

   Navigate into the file [./app/src/fb_client_secrets.json](/app/src/fb_client_secrets.json), 
   and replace "APP_ID" with your App ID and "APP_SECRECT" with App secret.
   ```
   {
	  "web": {
	    "app_id": "APP_ID",
	    "app_secret": "APP_SECRECT"
	  }
	}
   ```
   > see [this link](https://developers.facebook.com/docs/facebook-login/web) for more information about Facebook Login for the Web.

## Demonstration

- The homepage displays all current categories with the latest added items.
- Selecting a specific category shows you all the items available for that category.
- Selecting a specific item shows you specific information about that item.
- After logging in, a user has the ability to add, update, or delete item information. Users should be able to modify only those items that they themselves have created.


## JSON endpoint 

- ```/catalog.json``` : Display all categories including its items.

