# servirlabsite
**Pre-requisites:**

1. Django has to be installed.
2. Anaconda or Miniconda has to be installed as we set the environment of the project using conda commands.
3. Make sure the python version is correct.
4. Virtual Environment is needed here.

**Steps :**

1. Make sure the project is running on your local by following the steps here : https://pypi.org/project/SERVIR-Template-CLI/
2. We can now upload this project to a github repository from which we will be deploying on AWS.
3. Now login to AWS console and create an EC2 instance.
4. Create a security key pair for that instance and download it and keep it somewhere safe as we might have to refer this later.
5. Add the necessary inbound rules for security groups for that instance.
6. Now go to the location where the key pair was downloaded and start the git bash there.
7. Connect with the provided ip address for that EC2 instance. Example : ssh -i "servir.pem" [ubuntu@3.143.255.8](mailto:ubuntu@3.143.255.8)
8. After the connection is established successfully, create a folder.
9. Now clone the repository from github into that folder.
10. Create a virtual environment and install the requirements file using this command "pip install -r requirements.txt".
11. Now try to run the server by using python [manage.py](http://manage.py/) runserver using the settings of the project app name.
12. Go to the EC2 instance and open the public ip address of it.
13. If it is a secured connection it may not work so change it to http from https in the url.

**Configuring or Setting up the project with Gunicorn and Nginx.**

1. We need to create a gunicorn.socket file using this sudo nano/etc/systemd/system/gunicorn.socket
2. In this file we will be describing the socket.
  [Unit]
  Description=gunicorn socket

        [Socket]
        ListenStream=/run/gunicorn.sock

        [Install]
        WantedBy=sockets.target

1. Save it and close it. And now open a service file using sudo nano /etc/systemd/system/gunicorn.service
2. This is to specify all the dependancies related to our project and all the meta information.
3. Now we need to start and enable the gunicorn service using these commands
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
4. Check the status and create a sym link : sudo systemctl status gunicorn.socket, file /run/gunicorn.sock
5. Now that Gunicorn is setup, we need to configure Nginx to allow traffic to pass.
6. We need to define a server block by mentioning via which port we want to listen to.
7. Also use the location directives to mention all the static files and root.
8. Start Nginx and open up firewall to traffic to pass through on that port.

*You can also follow the below reference if in case you face any difficulty for a more detailed guide depending on the version of ubuntu you have.*

**References** :
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-22-04

**Checking the host now:**

1. **Use the ip address and check if your project is appearing exactly as how it is appearing on the local.**
2. **There will be one obvious difference which is your static files or images.**
3. **Since we are hosting our application on AWS, the static files present on our disk will be no longer of use.**

**Configuring an S3 bucket.**

1. Create a s3 bucket and attach policies to it.
2. Attach amazon full access policy to the bucket.
3. Create it by giving a name and let the settings be default.
4. Now come back to the project and add AWS access keys, secret and signature, region etc.
5. You will get these details when you create your bucket.
6. Paste the key value pair at the bottom of your [settings.py](http://settings.py/) file.
7. We know want to define where we want to look at the location by default for static files.
8. So for this we need to install 2 things : storages, and boto3.
9. Make sure you add storages in INSTALLED_APPS.
10. pip install django-storages.
11. pip install boto3
12. After successfully installing them now add the s3 location at the default_static_file storage.
13. We also need to add a key value pair for staticfile_storage.
14. Now come back to the bucket and upload the static folder there which has all the images, js and css files along with webfonts.
15. Save your [settings.py](http://settings.py/) file and run your server now.
16. When you open your website and inspect the webpage you will notice that the static files are now being read from s3 and not from the path it used to refer earlier.
