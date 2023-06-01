# Run Linux Shell on Windows Using WSL: A Step-by-Step Guide

## Introduction:
Are you interested in harnessing the power of a Linux shell or command-line interface (CLI) but don't want to switch to a Linux operating system? Good news! With Windows Subsystem for Linux (WSL), you can run a Linux shell right on your Windows PC. In this step-by-step guide, we'll walk you through the process of installing and setting up WSL on your Windows computer, so you can experience the flexibility and versatility of Linux tools and utilities without leaving the Windows environment.

## Prerequisites:
Before we begin, make sure you meet the following requirements:
- A compatible version of Windows (e.g., Windows 10, Windows 11).
- Sufficient system resources (RAM, storage) to accommodate the Linux distribution.

## Installation:
To enable WSL on your Windows PC, follow these steps:

For Windows 10 and Windows 11:
1. Open your PowerShell and run the following command:
   `wsl --install`
   ### OR
   - Open the Windows search bar and search for "Turn Windows features on or off."
   - Find and enable the "Windows Subsystem for Linux" option.
   - Allow the features to install.
   - Your system might ask for a restart; accept that.

## Choosing a Linux Distribution:
WSL supports various Linux distributions. Here are a few popular choices:
- Ubuntu
- Debian
- Fedora e.t.c

If you're new to Linux, we recommend starting with Ubuntu for its user-friendly interface and extensive community support.

## Downloading and Installing a Linux Distribution:
To download and install a Linux distribution, follow these steps:

1. Go to the Microsoft Store and search for your desired Linux distro, or use the command line to download the Linux distribution of your choice.
   - To check for available distros, run the command: `wsl.exe -l -o`
   - To install your desired distro, run the following command: `wsl.exe --install -d <Distribution Name>`

2. Launch the Linux distribution and follow the setup instructions to create your user account and configure initial settings.

## Running the Linux Shell/CLI:
Once you have installed a Linux distribution through WSL, you can access the Linux shell in the following ways:

1. Using the dedicated Linux distribution application.
2. Launching the Linux shell directly from the Windows Command Prompt or PowerShell by running the command: `bash`
3. Using the "Windows logo + R" to open the Windows Run window, then insert "bash" as input and execute.

## Exploring Linux Tools and Utilities:
Now that you have access to the Linux shell, it's time to explore some of the powerful Linux tools and utilities. Here are a few basic commands to get you started:
- [Linux commands](https://www.google.com/search?q=linux+commands&rlz=1C1YTUH_enNG1015NG1015&oq=linux+commands&aqs=chrome..69i57j46i433i512j46i512j0i512l2j46i512j0i512j69i60.78161j0j9&sourceid=chrome&ie=UTF-8)

## Conclusion:
Congratulations! You've successfully set up WSL on your Windows PC and are now running a Linux shell alongside your Windows environment. Enjoy the best of both worlds by leveraging the vast array of Linux tools and utilities while retaining the familiarity of Windows. Feel free to explore further, experiment with different Linux distributions, and dive deeper into the world of Linux right from your Windows machine. Happy Linuxing!
