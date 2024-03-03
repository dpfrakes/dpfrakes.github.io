---
title: "Customizing Your Setup"
date: 2021-09-29T00:00:00-04:00
draft: true
tags: [tech]
---

## Binaries

### Node Version Manager

NVM

### ZSH

oh-my-zsh and its benefits

```sh
~/.zsh_aliases
```

### Homebrew (Mac)

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

### Python 3

Python 2 is dead, but Mac can't let it go yet.

Cut in line by adding a symlink to python3:

```sh
brew install python
ln -s /usr/local/bin/python3 /usr/local/bin/python
```

`python2` is already an alias for you, so on the off-chance you actually want to run python 2 for something, you can still access it

## Custom Scripts

custom bash and python scripts in `/usr/local/bin` or `~/.scripts`

verify whichever of the above is on `$PATH`

```py
#!/usr/local/bin/python3

print('hello world!')
```

