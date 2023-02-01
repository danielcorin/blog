---
categories: code
date: "2016-02-08T06:19:00Z"
title: Automatic Python virtual environments
aliases:
    - /code/2016/02/08/automatic-python-virtualenvs.html
tags:
    - code
    - python
---

Automatic Python virtual environments
=====================================

Python virtual environments are great for seperating your development environments for each project. You can start with a fresh install and dependencies for each project, which helps keep your project dependency list short and your Python path clean. I use `virtualenvwrapper` and [this setup](http://mkelsey.com/2013/04/30/how-i-setup-virtualenv-and-virtualenvwrapper-on-my-mac/) to make new environment creation easy, but I find myself constantly running a project only to realize that I haven't activated the proper environment.

The standard package manager in Python is `pip`. When you run `pip install <package_name>`, `pip` looks up your package and downloads it to your `site-packages` folder. This folder changes based on your system `$PYTHONPATH`. You can check this by running `python -m site`. You'll notice the results differ when a virtual environment is active. When you create a new environment via the virtualenvwrapper `mkvirtualenv` command, the directory to which `pip` installs your packages changes to `~/Envs/<env_name>/lib/python2.7/site-packages`. There are tradeoffs to this design: all environments are located in one place but no specific project directory is associated with any given environment. This design choice may be especially odd if you are familar with `node` and `npm`. `npm` installs all packages and their dependencies into a `node_modules` folder inside the given project directory unless instructed otherwise. `pip` does the opposite, installing globally (to the `site-packages` folder) by default. Virtual environments help give us some notion of namespacing, but typically an environment is made for a specific project. If you follow this pattern in your development, it can become especially repetitive to type

    workon <your_hopefully_autocompletable_env_name>

What I want is for a particular virtual environement to automatically activate itself when I change to the project directory that uses it, and stay active in all project subdirectories. In each project folder for which I have a virtual environement, I add a `.venv` file containing the name of the project's environment. Literally just:

`.venv`
{{< highlight bash >}}
my-simple-env
{{< / highlight >}}

Next, I add some code to my `.bash_aliases` file, adding a hook to the `cd` command by overriding it with a function. You may really hate this idea, but stick with me for now to see why this is worth it.

Some helpful code snippets used to build this can be found here:

[Stackoverflow post on searching parent directories](http://unix.stackexchange.com/questions/6463/find-searching-in-parent-directories-instead-of-subdirectories)

[Virtualenvwrapper source code](https://bitbucket.org/virtualenvwrapper/virtualenvwrapper/src/3ca89a29ab6c12fa6974f4f31d1520aaed921808/virtualenvwrapper.sh?fileviewer=file-view-default#virtualenvwrapper.sh-750)



{{< highlight bash >}}
search_up () {
    proj_root=$(pwd -P 2>/dev/null || command pwd)
    while [ ! -e "$proj_root/$1" ]; do
      proj_root=${proj_root%/*}
      if [ -z "$proj_root" ]; then echo ""; return; fi
    done
    echo "$proj_root/$1"
}

virtualenv_check () {
    VENV_DIR=$(search_up .venv);
    # .venv file is in the dir or a parent dir
    if [ ! -z $VENV_DIR ]; then
        # if an env is already active, check if we need to call `workon` at all
        if [ ! -z "$VIRTUAL_ENV" ]; then
            CUR_VENV=$(basename $VIRTUAL_ENV);
            VENV=$(cat $VENV_DIR);
            # if the active env if different from the .venv file, switch to the latter
            if [ "$VENV" != "$CUR_VENV" ]; then
                workon $VENV;
            fi
        # no env active
        else
            workon `cat $VENV_DIR`;
        fi
    else
        # code from virtualenvwrapper to deactivate an env
        type deactivate > /dev/null 2>&1
        if [ $? -eq 0 ]
        then
            deactivate
            unset -f deactivate > /dev/null 2>&1
        fi
    fi
}

cd_hooks () {
    virtualenv_check
}

cd () {
    builtin cd "$@" && cd_hooks
}

{{< / highlight >}}

First, look at the `search_up` function. We check up the directory tree starting in the current folder to find a `.venv` file. Now look at the `virtualenv_check` function. If the file exists, we check to see if that environment is currently active and, if not, activate it the with the `workon` command. In the `else` outer clause, we check to see if an environment is active even though our directory doesn't have a `.venv` file. If one is active, we `deactivate` it. If you don't like this feature, you can safely remove the `else` clause with no other side effects. This behavior ensures an environment is automatically isolated. Without it, the activated virtual environment persists after you `cd` out of its project. Finally, the `cd_hooks` function is used as place to put other hooks to the `cd` command. We then override the `cd` command with a function which calls `builtin cd` and then all of our hooks. Now when we `cd` to a directory with a `.venv` file (or whose parent has one), it is automatically activated.

Hopefully this adds a nice new feature to your Python workflow that you'll soon take for granted.
