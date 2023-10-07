Question 1) Docker Containers vs VMs
A virtual machine relies on the system’s physical hardware to emulate the exact same environment on which you install your applications 
whereas Docker containers  a lightweight, stand-alone, executable package of a piece of software that includes everything needed to run it and they are platform-independent
1. The tools associated with a virtual machine are easier to access and simpler to work with. Docker has a more complicated tooling ecosystem, that consists of both Docker-managed and third-party tools.
2. Once you have a virtual machine up and running, you can start a Docker instance within that VM, and run docker container within the VM (which is the predominant method of running containers at present). This way, containers and virtual machines are not mutually exclusive and can co-exist alongside each other.
3. Docker containers are process-isolated and don’t require a hardware hypervisor. This means Docker containers are much smaller and require far fewer resources than a VM.
4. Docker is fast. While a VM can take an at least a few minutes to boot and be dev-ready, it takes anywhere from a few milliseconds to a few seconds to start a Docker container from a container image.
5. Containers can be shared across multiple team members, bringing much-needed portability across the development pipeline. This reduces ‘works on my machine’ errors that plague DevOps teams.
In conclusion, docker containers prove to be a better choice for developers as compared to VMs. 

Question 2) Write command to create a docker container in detached mode with name assignment-2-<ROLL_NUMBER> running on host port 9090 and container port 80 using image nginx with version 1.24.0 on a custom network named assignment-2

COMMAND: docker run -d --name assignment-2-I20-0813 -p 9090:80 --network assignment-2 nginx:1.24.0
EXPLANATION:

docker run -d                                //Runs docker container in detatched mode 
  --name assignment-2-I20-0813              //the name of my docker container
  -p 9090:80                                //this maps port 9090 on the host to port 80 in the container.
  --network assignment-2                    //connecting the container to a custom docker network 
  nginx:1.24.0                              //stating the docker image to use for the container, which is "nginx" with version "1.24.0."

Question 3) 
Unable to attatch image here so will be uploading it in the repo as well as the submission tab on google classroom.


