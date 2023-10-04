Q1) Explain Docker Containers vs VMs?

Solution:

1. Docker Containers
* They are light weight as compared to VMs.
* They use host OS kernel.
* They are more efficient in terms of resource utilization as they does not requires full OS.
* Containers are highly resource efficient and start up quickly.
* Each container has its own file sytem.
* Containers are highly portable.

2. VMs
* VMs would run on full OS stack including the kernel which makes the heavier.
* VMs are more resource intensive.
* Vms provide stronger isolation because they emulte separate hardware.
* Every VM has its own kernel and resources making it more secure and suitable for running.
* Vms are less portable as compared to conainers.

Q2) Write command to create a docker container in detached mode with name assignment-2-<ROLL_NUMBER> running on host port 9090 and container port 80 using image nginx with version 1.24.0 on a custom network named assignment-2

Solution:

docker run -d --name assignment-2-19F_0257
-p 9090:80
--network assignemnt_02
nginx:1.24.0

Q3) Run the above command and add screenshot of it and share the logs

Solution:

2023-10-04 23:37:26 /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
2023-10-04 23:37:26 /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
2023-10-04 23:37:26 /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
2023-10-04 23:37:26 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
2023-10-04 23:37:26 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
2023-10-04 23:37:26 /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
2023-10-04 23:37:26 /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
2023-10-04 23:37:26 /docker-entrypoint.sh: Configuration complete; ready for start up
2023-10-04 23:37:26 2023/10/04 18:37:26 [notice] 1#1: using the "epoll" event method
2023-10-04 23:37:26 2023/10/04 18:37:26 [notice] 1#1: nginx/1.24.0
2023-10-04 23:37:26 2023/10/04 18:37:26 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) 
2023-10-04 23:37:26 2023/10/04 18:37:26 [notice] 1#1: OS: Linux 5.10.102.1-microsoft-standard-WSL2
2023-10-04 23:37:26 2023/10/04 18:37:26 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023-10-04 23:37:26 2023/10/04 18:37:26 [notice] 1#1: start worker processes
2023-10-04 23:37:26 2023/10/04 18:37:26 [notice] 1#1: start worker process 29
2023-10-04 23:37:26 2023/10/04 18:37:26 [notice] 1#1: start worker process 30
2023-10-04 23:37:26 2023/10/04 18:37:26 [notice] 1#1: start worker process 31
2023-10-04 23:37:26 2023/10/04 18:37:26 [notice] 1#1: start worker process 32
2023-10-04 23:37:26 2023/10/04 18:37:26 [notice] 1#1: start worker process 33
2023-10-04 23:37:26 2023/10/04 18:37:26 [notice] 1#1: start worker process 34
2023-10-04 23:37:26 2023/10/04 18:37:26 [notice] 1#1: start worker process 35
2023-10-04 23:37:26 2023/10/04 18:37:26 [notice] 1#1: start worker process 36



