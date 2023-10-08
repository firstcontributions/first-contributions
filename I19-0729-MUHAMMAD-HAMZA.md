# Assignment 2 - I19-0729 - MUHAMMAD-HAMZA

## Q1) Explain Docker Containers vs VMs

Docker containers and virtual machines (VMs) serve similar purposes, but they differ in their architectural approach and resource usage:

### Docker Containers:
- Containers are lightweight and share the host OS's kernel, which makes them highly efficient in terms of resource usage.
- They use a layered file system (images) and package all dependencies with the application, ensuring consistency across environments.
- Containers can start and stop quickly, making them suitable for microservices architecture and scaling applications.
- Docker uses a Dockerfile to define the container's configuration and dependencies.

### Virtual Machines (VMs):
- VMs are more heavyweight as they include a full OS stack, which consumes more resources.
- Each VM runs its own OS, leading to greater isolation but higher resource overhead.
- VMs typically take longer to start and stop compared to containers.
- Virtualization software, such as VMware or VirtualBox, manages VMs.

In summary, Docker containers are lightweight, share the host OS, and are highly portable, making them a preferred choice for modern applications. VMs, on the other hand, provide stronger isolation but come with higher resource overhead.

## Q2) Write command to create a docker container in detached mode with name assignment-2-I19-01729 running on host port 9090 and container port 80 using image nginx with version 1.24.0 on a custom network named assignment-2

To create a Docker container with the specified parameters, use the following command:

```bash
docker run -d --name assignment-2-I19-0729 -p 9090:80 --network assignment-2 nginx:1.24.0
