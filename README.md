# Alien Invasion

Inspired by Space Invaders, Alien Invasion is an arcade game where the user has to use a ship to destroy all the aliens in the screen to
reach the next level. As the levels increase, the aliens and the ship's bullets both move faster, the user has to steer the ship dexterously
to create a new high score. The game ends when either the aliens collide with the ship or they reach the bottom of the screen.

## Learned

Testing my new abilities with python I decide to make the space invaders, with the help of the book, Python crash course by Eric Matthes. In this
Project I learned how to detect mouse movements, display information in textual and nontextual ways, how to use python libraries, how to use nested loops
to create a grid of elements, how to track the statistics in a game and use flags to determine when the game is over.


## Demo:
![web app](https://cloud.githubusercontent.com/assets/20157000/22623388/5a742aac-eb27-11e6-8f59-870eed6ab8da.png)

### Prerequisities

Since this game is created using Pygame modules. You will need to install Pygame and its dependencies.

**On Linux:**
Install the dependencies first using the packet manager.
```
$ sudo apt-get install python3-dev mercurial
$ sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev
```
If you want to add sounds to the game, install the following libraries as well:
```
$ sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
$ sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcode-dev
$ sudo apt-get install python-numpy
```
Then finally install Pygame using pip:
```
$ pip install --user hg+http://bitbucket.org/pygame/pygame
```

**On OSX:**
Install the dependencies using [Homebrew](brew.sh).
```
$ brew install hg sdl sdl_image sdl_ttf
```
*see [Troubleshooting](#troubleshooting) for OSX's SDL bug*

And for sound libraries:
```
$ brew install sdl_mixer portmidi
```

Ending by installing Pygame using pip:
```
$ pip3 install --user hg+http://bitbucket.org/pygame/pygame
```

**On Windows**

Find a [windows installer](https://bitbucket.org/pygame/pygame/downloads/) that matches your version of Python.
Run the installer if it is an exe and if there is an .whl file copy it to the project directory.
Open a command window and navigate to the folder your copied your installer and install using pip.
```
> python -m pip install --user pygame-1.9.2a0-cp35-none-win32.whl
```

### Installing

No installation is needed! To play the game, run the *[alien_invasion.py](alien_invasion.py)* file using Python3 and enjoy!

### Controls

* Press the Return key(⏎) or click the 'Play' button to start
* Steer the ship using arrow keys(←↑↓→)
* Press 'q' to quit anytime.
* Press 'p' to pause the game.

##Troubleshooting

###1. Is this game compatible with Python 2.7 ?
    No, I am sorry, this game can only be run using Python3.

###2. The game images aren't loading properly on my OSX. What do I do?
    This is the OSX's SDL image glitch I was talking about. You probably have a relatively newer version of SDL.
    This is what is making the images load incorrectly. You can solve this problem by degrading the SDL version down to 1.2.10.
    There are several ways to do this, I found this method the best. Run this on your Terminal:
```
brew edit sdl_image
```
    This will open a ruby file. Update the URL and has as follows:
```
url "https://www.libsdl.org/projects/SDL_image/release/SDL_image-1.2.10.tar.gz"
sha256 "75e05d1e95f6277b44797157d9e25a908ba8d08a393216ffb019b0d74de11876"
```
    Comment out the newer version's URL and Hash for backup if you want. Now run:
```
brew reinstall sdl_image
```


## License

The MIT License (MIT)
=====================

Copyright (c) 2015

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
