+++
author="BIOLAB"
date= '2010-03-04 01:56:00+00:00'
draft= false
title="Debian repository lives!"
type="blog"
categories=["debian" ,"distribution" ,"download" ,"packaging" ]
tags=["debian" ,"distribution" ,"download" ,"packaging" ]

+++

We have made still-experimental-but-probably-working Debian repository with daily built Orange packages. Currently without add-ons.

To get access to those packages just add those two lines to your /etc/apt/sources.list (this file contains a list of repositories with packages):

    
    deb http://orange.biolab.si/debian lenny main
    deb-src http://orange.biolab.si/debian lenny main


And then you can install Orange with this command:

    
    aptitude update
    aptitude install orange-svn


Packages are not signed as they are made automatically so you will probably be warned about this.

Those packages will probably work also on other Debian-based Linux distributions like Ubuntu, but have not yet been tested there. Please test it and report how it goes.

You can also get source of those packages with this command:
    
    apt-get source python-orange-svn


And then build package by yourself in extracted source directory with:

    
    dpkg-buildpackage


For example this will be useful on amd64 platform for which we currently do not yet provide binary packages. (Edit: now we provide binary packages also for amd64 platform.) But we will once we see how well this system works.
