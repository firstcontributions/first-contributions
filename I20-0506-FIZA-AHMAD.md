1. Docker containers vs VMs
~ Docker container                                   ~ VM's (virtual machine)
--> Virtualization is OS-based                      --> Virtualization is hardware-based 
--> Lightweight, share the host OS kernel           --> Heavier, emulate entire operating systems
--> Use fewer resources                             --> Consume more resources
--> Start almost instantly                          --> Have longer startup times
-->Smaller image sizes due to sharing the OS kernel --> Larger image sizes due to containing a full OS

2. docker run -d --name assignment-2-I20-0506 -p 9090:80 --network assignment-2 nginx:1.24.0
   
3. ScreenShot:
   ![Screenshot](docker command.png) 
