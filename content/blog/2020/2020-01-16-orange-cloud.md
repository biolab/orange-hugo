+++
author = "Andrej Čopar"
date = "2020-01-16"
draft = false
title = "Orange in the Cloud"
type = "blog"
thumbImage = "/blog_img/2020/2020-01-16-orange-cloud.png"
frontPageImage = "/blog_img/2020/2020-01-16-orange-cloud.png"
blog = ["cloud", "server", "remote"]
shortExcerpt = "Use Orange remotely by running it on a remote server as a docker container."
longExcerpt = "Use Orange remotely by running it on a remote server as a docker container."
+++

Many problems are too big and require too much processing power to be efficiently processed on your laptop or PC. In such cases, the data is usually transferred to a remote server and processed using custom code, which is often time consuming. Now, there is a way to run Orange on a remote server so that you can keep using its interactive graphical interface. We will show you how to run Orange on the remote server so that you can use it through your web browser.

{{< figure src="/blog_img/2020/2020-01-16-weborange.png" >}}
\

In a nutshell, you browser opens a remote desktop connection to an Orange instance that runs inside a docker container on a remote server. Now let us go into more details.

In our configuration we used several different technologies such as [Docker](https://www.docker.com/) and [Apache Guacamole](https://guacamole.apache.org/), which are shown in the diagram. First, you need to set up [Nginx](https://nginx.org/en/) (or alternatively [Apache web server](https://httpd.apache.org/)), which is used to ensure that all communication to the server is SSL encrypted. This is very important, because remote desktop protocols such as [Remote Desktop protocol (RDP)](https://en.wikipedia.org/wiki/Remote_Desktop_Protocol) and [Virtual network computing (VNC)](https://en.wikipedia.org/wiki/Virtual_Network_Computing) are not encrypted. Failure to do so will expose your data to anyone listening on the network.

{{< figure src="/blog_img/2020/2020-01-16-stack.png" >}}
\

Nginx redirects you to the [Apache Guacamole](https://guacamole.apache.org/) web application. In Guacamole you can manage multiple users and specify which of your Orange instances each user has access to. Guacamole then connects you to a selected [Orange-docker](https://github.com/biolab/orange-docker) container through an RDP or VNC connection. Once it is connected, you can see the remote desktop in your browser. You can use Orange just like on a local computer (see the image above), although you may need a few minutes to get used to the Linux environment.

Dockers allow you to run many lightweight isolated Linux containers on the same machine. We prepared a [docker image](https://github.com/biolab/orange-docker) that comes pre-configured with graphical desktop environment, a remote desktop server, Orange application and a few convenience applications (Libre Office, web browsers). You can run many isolated Orange-docker containers, so each user can work on a different project. When users collaborate on a project, they can connect to the same instance and share the same screen (read-only or full access). You can upload and download your data to and from the remote server using drag & drop feature or the side menu. Alternatively you can transfer the data with one of the web browsers that are provided in the container.

There are many other benefits to running Orange on the server infrastructure. First, **Orange can stay open and continue to process the data** even when you are offline. Second, you can **access the same workflow from any computer**. Third, multiple users can **interactively collaborate on the same workflow**. Finally, you do not have to keep the data on a local computer and **you do not need to install Orange on a local computer**. Note that this is a self-hosted solution, which means that all your data remains on the servers under your control.

For a complete installation guide and more details see [orange-docker](https://github.com/biolab/orange-docker) Github repository.
