Installing Git Ubuntu OS
===

Git by default is likely already installed in your Ubuntu OS . You can confirm this by launching your terminal and entering following command in to your terminal:

```shell
$ git --version
```

If you receive output similar to the following, then Voila! you have readily installed Git on your machine.
```shell
Output
$ git version 2.34.1
```

If this applies to you, proceed to [set up git](#set-up-git) below.

If a Git version number was not on the output as shown above, you can still install it using Ubuntu's APT default package manager.

Update your local package index first by using the apt package management tools. Head back to your terminal and enter the following command.

```shell
$ sudo apt update
```
Once this is completed, then enter the following command to install in Git:
```shell
$ sudo apt install git
```
You can confirm that you have installed Git correctly by running the following command and checking that you receive relevant output.
```shell
$ git --version
```
```shell
Output
$ git version 2.34.1
```
With Git successfully installed, you can now proceed below by setting it up.

# Set up Git

Coming soon...