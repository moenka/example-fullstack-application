Example Fullstack Application
=============================

WIP

## Getting started

1. Run `docker-compose up -d` from the root directory of this repository.
1. Run `curl --header 'Host:hello.docker.local' 'http://localhost:8000/'` to connect to the backend.

## Example Application Constraints

Design & implement a highly-available infrastructure using Docker and Docker Compose, _similar_
to the sketch below.


```
                             +----------+                    +----------+
                             |          |                    |          |
                             |    FE    |                    |    BE    |
                            /|          |\                  /|          |\
                           / +----------+ \                / +----------+ \
             +----------+ /                \ +----------+ /                \ +----------+
 http/https  |          |/                  \|          |/                  \|          |
>------------|    LB    |                    |    LB    |                    |    DB    |
             |          |\                  /|          |\                  /|          |
             +----------+ \                / +----------+ \                / +----------+
                           \ +----------+ /                \ +----------+ /
                            \|          |/                  \|          |/
                             |    FE    |                    |    BE    |
                             |          |                    |          |
                             +----------+                    +----------+
```


### Required functionality:

* You need to have at least two FEs
* You need to have at least two BEs
* Database must have persistent storage
* Host OS must be able to access the application via http or https


### Technical constraints:

* You can use public Docker images and/or provide your own
* Provide a working `docker-compose.yml` and instructions on how to get the setup running
* Provide a way to show container metrics
* Have separate networks with least required access
* Tests are provided
* Include auto-discovery and service registration

