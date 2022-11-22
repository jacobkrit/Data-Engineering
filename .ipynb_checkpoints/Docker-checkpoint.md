# DevOps

DevOps is a natural evolution of software development. DevOps is not just a tool, a framework, or just automation. It is a combination of all these. 

DevOps aimed to align the Developement and Dictionary team with shared goals.

![DevOps-1](img/DevOps-1.jpg "DevOps-1")

# Docker

A developer builds an application and sends it to the tester. But, the environments of development and testing systems are different; thus, the code does not work. There are two solutions to this: Docker and Virtual Machines, but Docker is far better in terms of performance, scaling, and efficiency.   

Docker is a platform that has eased application development for both developers and system managers. Dockers have been used widely in many DevOps toolchains. Docker provides flexibility for the operational team thereby reducing the risk overhead. Dockers platform provides numerous features include application isolation, portable, security management, Ease of software delivery, scalability, etc.    

Docker is a platform that enables creating, deploying, and running applications with the help of containers. A Container is a unit of software that packages the code and all its dependencies together such that the application becomes runnable irrespective of the environment.   

Container isolates the application and its dependencies into a self-contained unit that can run anywhere. Container removes the need for physical hardware allowing for more efficient use of computing resources. Containers provides operating-system-level virtualization. Moreover, developers can collaborate faster without worrying about which software dependency they need to install.    

A container is a runnable instance of an image. An image is a read-only template with instructions for creating a Docker container. You can create, start, stop, move, or delete a container using the Docker API or CLI. One can connect a single container to one or more networks and can also attach storage to it. A new image can also be created based on the current state of the container. Containers can be shared thereby ensuring that everyone who communicates with it will get the same container and that works in the same way.    



## Basic Docker Commands

- `docker --version [OPTIONS]`
    - This command is used to get the current version of the docker.
- `docker images`
    - Prints all the current images installed locally.
- `docker pull [OPTIONS] [IMAGE_NAME]`
    - Pull an image or a repository from a registry, To download an image or set of images (i.e. A Repository) , Once can use docker pull command.
- `docker run [OPTIONS] [IMAGE_NAME]`
    - This command is used to create a container from an image 
- `docker ps`
    - This command is used to list all the containers plotting their IDs, Ports etc
- `docker stop [OPTIONS] [Container_ID]`
    - This command is used to stop one or more running containers. 
- `docker restart [OPTIONS] [Container_ID]`
    - This command is used to restart one or more containers. 
- `docker kill [OPTIONS] [Container_Name]`
    - This command is used to kill one or more containers. 
- `docker logs [Container_ID]`
    - Commands that helps debugging
- `docker exec -it Container_ID COMMAND`
    - This command is used to run a command in a running container, example: `docker exec -it Container_ID /bin/bash` we get the bash as vm
- `docker commit` 
    - This command is used to create a new image from the container image. 
- `docker push`
    - This command is used to push an image or repository to a registry. 

[OPTIONS] 
`-d`
- detached mode : run the container without the terminal: `docker run -d [IMAGE_NAME]`

`-a`
- Print container that are running and not running 

`- p[Host Port Number]:[Binding Port Number]`
- Bind port of your host (port of the host <-- port which you exernaly send requests) to the container (port of tha you are binding this). **Port**: specifies on which port the container is listening to the incomming request. example: `docker run -p6000:6379 [IMAGE_NAME]`



# References
- https://www.knowledgehut.com/blog/devops/basic-docker-commands#basic-docker-commands
- https://www.youtube.com/watch?v=3c-iBn73dDE

