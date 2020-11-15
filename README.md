# flask-postgres-app

This is a naive implementation of a backend app developped in flask. We will be using Postgresql as a database.

# STEPS to run the project

First step is to connect to the database. Open your command line and run "psql -U postgres" then enter the password. 

Next step is to set our postges database. I created a database called lin_flask using this commande : 

CREATE DATABASE lin_flask;

Once our DB is created, we create two tables:
* "users" where we will store users' credentials :

             CREATE TABLE users(
          

                id SERIAL PRIMARY KEY,
             
                username VARCHAR(255),
             
                pwd VARCHAR(255)
             
              );
             

* "cv" where we will store users' resumees

             CREATE TABLE resumee( 


                id SERIAL PRIMARY KEY,
             
                first_name VARCHAR(30) NOT NULL,
             
                last_name VARCHAR(30) NOT NULL,
            
                email VARCHAR(200) NOT NULL UNIQUE,    
             
                birth_date DATE ,
             
                num_tel NUMERIC(8),
             
                disp NUMERIC,
             
                nb_exp NUMERIC,
             
                message VARCHAR(255)
       
             );
             
 Next step is to change the app.config['SQLALCHEMY_DATABASE_URI']. For my case, the URI (under app/__init__.py) is postgresql://postgres:123456789@localhost/lin_flask
 because the user is postgres, the password is 123456789 and the database is lin_flask. 
 
 You should adapt these parameteres to what you have.
 
 The final step is to run the flask project by running "python run.py"
