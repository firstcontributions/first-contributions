# Storing Credentials

Dealing with username and password prompts every time you interact with a Git repository can be inconvenient and disrupt your workflow. However, there are methods available to store your credentials securely and avoid repetitive authentication.

One approach is to use the Git Credential Cache, which allows you to cache your credentials locally so you don't have to enter them repeatedly. It's important to note that while this method provides convenience, it stores the credentials in plaintext on your local disk. This means that anyone with access to your computer could potentially access these credentials, including malicious actors.

## Global Credential Cache

To enable the credential cache globally, which applies to all repositories you interact with, you can use the following command:

```bash
$ git config --global credential.helper cache
```

This command configures Git to use the credential cache helper for all repositories on your system. However, be cautious and follow the security policies of your organization or place of study, as storing credentials in plaintext could pose a security risk.

## Repository-Specific Credential Cache

If you prefer to store credentials for a specific repository, you can use the following command within that repository's directory:

```bash
$ git config credential.helper cache
```

This command configures the credential cache helper for the current repository only.

## Setting Cache Timeout

By default, if you don't specify a cache timeout, the credentials will be stored indefinitely, which might not be secure. You can set a specific timeout for how long credentials should be cached in memory using the following command:

```bash
$ git config credential.helper 'cache --timeout=<timeout>'
```

For example, to set a timeout of 30 minutes:

```bash
$ git config credential.helper 'cache --timeout=1800'
```

With the credential cache helper, credentials are stored in memory and will be automatically erased after the specified timeout. This can be a more secure option compared to storing them on disk.

Remember to consider the security implications and follow best practices when storing credentials, especially in shared or public environments.

## References

- [Stack Overflow Discussion](https://stackoverflow.com/questions/35942754/how-can-i-save-username-and-password-in-git)

For more information and additional material, please refer to the [provided link](additional-material.md).