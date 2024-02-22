# Storing Credentials

You might have complained about this before - entering your username and password each time you access the repository can be a hassle and can interrupt your workflow if it takes too long. But it doesn't need to be that way.

We will be covering one of the methods available to us - [git credential cache](https://git-scm.com/docs/git-credential-cache).

**Note:** Please follow the security policies of your place of work/study.

## Caching

We can use git credential cache to store our username and password.

**Attention:** This method saves the credentials in *plaintext* on your PC's disk. Everyone on your computer can access it, e.g. malicious NPM modules.

### Global Credential Cache

If we wish to, we can store the credentials for every repository we are working with using one simple command:

```
$ git config --global credential.helper cache
```

**Reminder:** Please follow the security policies of your place of work/study.

### Repository Credential Cache

We can store the credentials for the repository we are working with using one simple command, similar to before: 

```
$ git config credential.helper cache
```

**Reminder:** Please follow the security policies of your place of work/study.

### Cache Timeout

If we do not specify a length of time to store our credentials, they can potentially be stored forever. However, we can determine how long they will be kept in memory using this command:

```
git config credential.helper 'cache --timeout=<timeout>'
```

Using the helper, the credentials will never touch the disk and will be erased after the specified timeout. The default value is 900 seconds (15 minutes).

#### References
[Stack Overflow](https://stackoverflow.com/questions/35942754/how-can-i-save-username-and-password-in-git)

### [Additional Material](additional-material.md)