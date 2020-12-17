+++
author="BIOLAB"
date= '2011-09-13 00:32:00+00:00'
draft= false
title="Debian packages support multiple Python versions now"
type="blog"
blog=["debian" ,"packaging" ,"python" ]
+++

We have created Debian packages for multiple Python versions. This means that they work now with both Python 2.6 and 2.7 out of the box, or if you compile them manually, with any (supported) version you have installed on your (Debian-based) system.

Practically, this means that now you can install them without manual compiling on current Debian and Ubuntu systems. Give it a try, [add our Debian package repository](/download/), apt-get install **python-orange** for Orange library/modules and/or **orange-canvas** for GUI. If you install the later package, type **orange** in the terminal and Orange canvas will pop-up.
