### A Simple FAST API server handling all the REST endpoints for user management

We use static data for our example..in real time, we would be integrating a SQL or a noSQL database and use appropriate connectors to have our FastAPI backend connect with our database

## To execute this

make sure you do a pip install fastapi..this package allows us to use fastapi and its associated classes in our API and also do a pip install uvicorn
Frameworks like Flask and Django have inbuilt functionality to have it running on a local server..but since fastapi is incredibly light weight we need to use uvicorn package. uvicorn provisions a local server
that enables us to run in this webserver


To run our application we need to run the uvicorn server as ### uvicorn myapi:app --reload
Where uvicorn is the library
myapi is the name of the file
app is the instance of the FastAPI() class
--reload reloads the server whenever changes are detected

This is usually hosted on localhost:8000. But FastAPI allows us to interact with our endpoints by provisioning a swaager documentation which is hosted on http://localhost:8000/docs
This is essentially a playground we can use to test our API's.
