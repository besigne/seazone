# seazone
challenge

##Dependencies

- Python 3.9
- Docker

##How to configure the database

Open a terminal, verify if your docker has root privileges and run:
```
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_HOST='%' -e MYSQL_ROOT_PASSWORD='123' -d mysql/mysql-server:latest --restart=always
```
Second command:
```angular2html
docker start mysql
```
Third command:
```angular2html
docker exec -ti mysql bash
```
Fourth command:
```angular2html
mysql -u root -p 
```
The password is `123`.
```angular2html
CREATE DATABASE seazone;
```

##Running the Application

After successfully creating the database to the application run, you should download
clone the repository then run on root directory:

```
source venv/bin/activate
```
Verify on terminal if the `(venv)` indicator is showing, if so, run the following command:
```angular2html
pip install -r requirements.txt
```
This command shall install all dependencies for the project to run, next we create the models
on the database:
```angular2html
python manage.py migrate
```
now your database should be ready, I created a script to seed the minimal information
necessary to see results, you just need to run this: `python seeder.py`

##WEB

To se the result of the application, go to the root project and run:
```angular2html
./manage.py runserver
```
Click the link showing on terminal, you should see an object that shows the host,
the events that he have, and in which superstructure, for future development, endpoints
showing only the event between dates can be implemented quickly creating a new Serializer
and a new View, as well sort by host or building.