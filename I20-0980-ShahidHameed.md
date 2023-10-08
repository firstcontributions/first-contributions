# Assignment 2 - I20-0980 - Shahid Hameed

# Docker vs VMs
Docker Containers:
Isolation: Lightweight, process-level isolation on the host system.
Resource Efficiency: Efficient resource sharing via the host OS kernel.
Speed: Rapid start-up within seconds, minimal resource usage.
Image-based: Construction from lightweight, standalone images.

Virtual Machines (VMs):
Isolation: Hardware-level isolation, each VM with its OS.
Resource Overhead: Heavier due to a full OS and virtualized hardware.
Start-up Time: Longer start-up time, akin to booting a complete OS.
Hypervisor: Relies on a hypervisor, adding overhead and complexity.

Comparison:
Resource Efficiency: Containers excel with shared OS kernel.
Isolation Level: VMs offer stronger isolation with independent OS.
Portability: Containers, more portable due to lightweight design.
Scaling: Containers scale easily with quick start-up and low resource usage.

# Docker Commands

docker run -d --name assignment-2-I20-0980 -p 9090:80 --network assignment-2 nginx:1.24.0
