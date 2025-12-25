# Dependancy confusion

- https://socket.dev/blog/elves-on-npmhhh
- https://panther.com/blog/a-data-driven-analysis-of-the-sha1-hulud-2-0-campaign


The goal is to call `/fetch` function in the source code, in order to trigger the build of a malicious npm packet on npmjs.

One of the problem was to get a shell on the right machine, due to CI/CD integration, using `preinstall`.


## Creating the packet

```bash
cd elf*
npm version patch
npm publish
```

This triggered a reverse shell.

