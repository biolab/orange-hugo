+++
author="BIOLAB"
date= '2011-06-30 00:44:00+00:00'
draft= false
title="Debian packages for Squeeze"
type="blog"
blog=["debian" ,"distribution" ,"download" ,"packaging" ]
+++

We have updated our daily Debian packages to Squeeze (current Debian stable). You just have to reconfigure our package repository in your **/etc/apt/sources.list** to:

    
    deb http://orange.biolab.si/debian squeeze main
    deb-src http://orange.biolab.si/debian squeeze main


Those packages are compiled for Python 2.6.

You can read more about Debian packages in our old [blog post](/blog/2010/03/04/debian-repository-lives/).
