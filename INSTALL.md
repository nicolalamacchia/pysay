 pysay installation
====================
_this file is part of pysay v2.0.0_

In any case you need python: the latest Python (2 or 3) version should work.
Please consider to install the standard cowsay: you might want to enjoy the
other fun *cows* that are bundled with that software.

* To install this script on a Unix-like OS:

   - cd into the package root folder
   - `# python setup.py install`

* Under a Win OS just execute the script from a shell (MSDOS emulator):

   - copy the cows folder into your %APPDATA% folder (if you want to use the
     .cow files that come with cowsay, put them into the same folder)
   - cd into the script directory (or put it into a folder in the system path)
   - you need to call Python to execute the script, so:

             python pysay [...]

     or (the *geeky* way) add the .PY extension to the PATHEXT environment
     variable (and renaming pysay to pysay.py). This allow you to call directly
     the script:

             pysay [...]

   - (optional) create a symlink to pysay called pythink in the same folder of
     pysay

