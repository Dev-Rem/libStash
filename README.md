# LibStash API

A Restful Api for book e-commerce, using the Python Django web framework and Django Rest framework.

This is my final year project of my Computer Science BSC.

<br>

# Prerequisites and Requirements

* A Stripe Payment Gateway account (API Keys needed)
* A Twilio SendGrid account (API Keys needed)
* Basic knowlegde of Django and Django Rest Framework
* Basic knowledge of HTML/CSS and JavaScript
* Docker Engine or Docker Desktop installed
* An IDE or code editor

<br>

# Installation and Downloads

Click on the green button above labeled "Code" Then click on "Download ZIP"

Save the ZIP file to your "Desktop" folder as future instructions would build on this.

Once download is complete, unzip the file and open it in your favorite IDE or code editor.

If you do no have one you can download anyone but i would suggest these two

VScode: <https://code.visualstudio.com/download>

Sublime: <https://www.sublimetext.com/3>

Now create a new file in the project root directory called ".env"  this file would be used to hold environment variables for the application same directory as the "docker-compose.yaml".

Now i am assuming you have obtained the necassary API keys. Please use the "sample.env" as a guide. Plug in the varables in ".env" file.

If you do not have the Docker engine or Docker desktop installed please install the right one for your OS.

<br>

Windows: <https://hub.docker.com/editions/community/docker-ce-desktop-windows>


<br>

macOS: <https://hub.docker.com/editions/community/docker-ce-desktop-mac>


<br>

Linux: <https://docs.docker.com/engine/install/ubuntu/>

<br>

# Running The Application

Open up the command-line on windows and terminal on macOS/Linux now navigate to the project directory. With these commands

<br>
Windows:

```
cd Deskstop\libStash-master\
```
<br>
macOS/Linux:

```
cd Deskstop/libStash-master/
```

<br>

Once in the project directory you can run the command below to confirm.
```
ls
```
Run the following command to build and create the services both containers and pull the necassary images.

```
docker-compose up
```

If all the commands worked fine without any errors then you should open your Docker desktop and you should be able to see the working project. All containers running.

The Next step is to create a superuser to enable you access the admin dashboard.

On your Docker desktop click on the libstash project and you will see a list of containers created. 

Amonsgt the containers you should see a container named "libstash_web_1" or "libstash_web" Click on the cli button ">_" and it should open a command-line interface.

Run the command:
```
cd libStas
python manage.py createsuperuser --settings=libStash.settings.development
```

Follow the prompt by providing your name email, first name, last name, password, and confirm your password.

If the prompt is completed without any error you can now access the admin dashboard at <http://localhost:8000/admin/>, using the email and password you just provided in registeration.


