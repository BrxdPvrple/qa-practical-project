# Song Generator
This is a song generator deployed via GCP utilising python, flask, docker, ansible, nginx and jenkins.

## Contents:

- [Project Brief](#Project-Brief)
- [App Design](#App-Design)
- [Pipeline/Teck Stack](#CPipeline/Teck-Stack)
- [Testing](#Testing)
- [Future Development](#Future-Development)


## Project Brief
The brief for this project was to create a microservice flask application written in Python, deployed via Docker, which utilises Jenkins for continuous integration. 

## App Design
- Service One:

    The first service is a front end flask application that displays data from the other three services. It makes GET requests to service two and three, as well as a POST request to service four.

    ![App](https://github.com/BrxdPvrple/qa-practical-project/blob/dev/images/App.png)

- Service Two:

    Service two is a random genre generator. There are five genres to choose from and one is selected completely at random and returned in response to an API call.

- Service Three:

    Service three is a random instrument generator. There are four instruments to choose from and one is selected completely at random and returned in response to an API call.

- Service Four:

    When service one makes a post request to this service it recieves the genre and instrument generated by services two and three, and then uses some back end logic to find and return a video of song that incorporates both the recieved genre and instrument.


## Pipeline/Teck Stack
The tech stack for this project was as follows:

- Jira for project planning and agile development.
- Git & Github for source control management.
- Ansible as a configuration tool.
- Google Cloud Platform was my cloud server of choice.
- Docker for containerisation and orchestration as well as Docker Hub as an image repository.
- Jenkins for CI/CD
- NGINX reverse proxy


#### Jira Sprint

![Sprint](https://github.com/BrxdPvrple/qa-practical-project/blob/dev/images/Jira_Sprint.png)

#### Burndown Chart

![BDC](https://github.com/BrxdPvrple/qa-practical-project/blob/dev/images/Burndown_Chart.png)


#### Docker Hub

![DockerHub](https://github.com/BrxdPvrple/qa-practical-project/blob/dev/images/Docker_Hub.png)


## Testing
Pytest and unittest modules were used to test the app before and during build phases, shell scripting was utilised to ensure this can be done automatically. I was able to get 100% coverage on all tests as seen in the snippet below from the Jenkins post-build console log.

![Tests](https://github.com/BrxdPvrple/qa-practical-project/blob/dev/images/Tests.png)


## Future Development
- Incorporate a SQL Database
- Add CRUD functionality, allow users to save favourite songs
- Use NGINX to configure another VM as a load balancer
