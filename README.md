# Odoo 10 Docker Configured with External Addons

To add apps and modules as external addons:

1. Copy all apps and modules you wish to add to "external_apps" folder.
2. Update "requirements.txt" inside the "external_apps" folder and add all python libraries needed by your apps and modules then save.


To run Odoo on Docker
1. Install docker to your host.
2. Open your local directory for this repository.
3. Run the command "docker-compose build" (add sudo if your running on a Linux machine).
4. Docker will build the images and container for Odoo.
5. After the build is complete, run the command "docker-compose up".
6. This will start the container build earlier.
7. Open your browser and access 'localhost:82'
8. Done. Odoo is now running on docker.

