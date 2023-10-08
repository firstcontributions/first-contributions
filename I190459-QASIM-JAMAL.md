Q1) Explain Docker Containers vs VMs.

There are two distinct methods for building isolated environments for running applications: Docker containers and virtual machines (VMs). I'll outline their primary distinctions in this blog post, along with advice on how to pick the one that best suits your requirements.

A virtual machine (VM) is a software representation of a physical computer that has its own operating system (OS), hardware, and software resources. A hypervisor, a layer of software that controls how many virtual machines are run on a single host machine, can be run on top of a VM. A virtual machine (VM) offers a high level of protection and isolation, but it also uses up a lot of resources and takes a while to boot up.

Contrarily, a docker container is a small, portable software package that includes all of the code, libraries, dependencies, and configuration necessary to run an application. A docker engine, a platform that controls the construction and execution of containers on a host machine, runs on top of a docker container. Although a docker container uses the host machine's OS kernel, it has its own file system and network stack. Compared to a VM, a docker container offers less isolation, but it also uses fewer resources and starts up more quickly.

Q2) Write command to create a docker container in detached mode with name assignment-2-<ROLL_NUMBER> running on host port 9090 and container port 80 using image nginx with version 1.24.0 on a custom network named assignment-2

docker run -d --name assignment-2-I190459 -p 9090:80 --network assignment-2 nginx:1.24.0
