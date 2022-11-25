# CRUD-API

![image](https://user-images.githubusercontent.com/65334844/204044863-710c40bd-6b14-487c-8135-865fdb13a9f6.png)
```
An API returns a JSON which is a common format. You can see all of the information surrounded with quotation marks, {},[], and descriptive titles of each bit of code.

Inorder to create a django project for CRUD_API make sure you have installed al of the following packages:

1.pip install django
2.pip install djangorestframework





-------------------------------------------------------------------------------------------------

Run the project using --python manage.py runserver

To check the Databse (admin) ,the credentials are:
 username:django
 password:django
 
 
-------------------------------------------------------------------------------------------------




After successfully running django project, put the following url to access the API:

* http://127.0.0.1:8000/api/employee/ 


We can do all the CRUD operations using this API, like, GET,PUT,POST,DELETE.




-------------------------------------------------------------------------------------------------

I would like to add some screenshots of CRUD operation of this API performed using ** POSTMAN **


```
#1.POST method - Creating an object
#http://127.0.0.1:8000/api/employee/ 

![image](https://user-images.githubusercontent.com/65334844/204043512-b663c477-9271-483d-98a1-4762a4febab6.png)

#2. PUT - Update
#http://127.0.0.1:8000/api/employee/3/
# Do add the ID num of the object you need to update with forwardslash '/'

![image](https://user-images.githubusercontent.com/65334844/204043854-17450190-8a74-4a21-8454-15147e892aa3.png)

#3. GET - Retrieve 
#http://127.0.0.1:8000/api/employee/3/
# Do add the ID num of the object you need to retrieve with forwardslash '/'

#To retrieve all the objects simply use--http://127.0.0.1:8000/api/employee/

![image](https://user-images.githubusercontent.com/65334844/204044459-813fce6d-7291-4f0a-ae80-f7733b6bb614.png)


#4. DELETE - To delete an object 
#http://127.0.0.1:8000/api/employee/3/
# Do add the ID num of the object you need to delete with forwardslash '/'
![image](https://user-images.githubusercontent.com/65334844/204045262-a526eb90-6b11-49ea-bc60-cbf8fc0c6a73.png)


