![copr build](https://copr.fedorainfracloud.org/coprs/eduardocerqueira/cd2cloud/package/cd2cloud/status_image/last_build.png)

<a href="https://copr.fedorainfracloud.org/coprs/eduardocerqueira/cd2cloud/package/cd2cloud/"><img src="https://copr.fedorainfracloud.org/coprs/eduardocerqueira/cd2cloud/package/cd2cloud/status_image/last_build.png" /></a>

# cd2cloud

MOTIVATION:

My wife has a large collection of audio CDs. She loves to listening music and since she saw some CDs are getting old and some others scratches she keep asking me
if I could convert all of them to our own home private cloud and make easy to listening the musics. It is the main motivation for this project as we are talking
more then 200 CDs and even with the great work Folks have done in Audio CD rippers like **abcde** [1] I was missing few things. So this small bunch of scripts is here
to solve my issues converting my wife's CDs to digital music and moving to our internal private Cloud and ready to be listened.

for more info:

[1] www.andrews-corner.org/linux/abcde/index.html


WHAT IS THIS?

It is a Linux tool to automatically recognize a CD audio inserted into CD drive and start converting all audio tracks to digital format depending of your configuration
file and as soon the convertion is complete it move all digital files to your own internal private Cloud.

USAGE:

Basic execution::

	cd2cloud --conf /home/eduardo/cd2cloud.conf &


The command above will start cd2cloud in background and it will be listening for all events filtered by CDROM directly in your kernel from uDev layer.
Whenever a Audio CD is inserted and CDROM drive is closed cd2cloud starts ripping the CD based in your abcde configuration and eject CDROM automatically.
The program keeps running and only thing you need to do is insert the next audio CD into CDROM drive and close it.

The image below is the alpha test for **cd2cloud** in an afternon my wife ripped **more than 25 audio CDs** with a simple task just to remove
the previous CD and insert a new one.

![Preview](https://github.com/eduardocerqueira/cd2cloud/raw/master/docs/source/_static/cd2cloud_stack_cds_ripped_1.jpg)

Also cd2cloud logs all information to a file and you can::

	tail -f /tmp/cd2cloud.log

to see all details what is going on behind the scene, like image showing below

![Preview](https://github.com/eduardocerqueira/cd2cloud/raw/master/docs/source/_static/cd2cloud_console.png)


## LINKS

**abcde**
http://www.andrews-corner.org/linux/abcde
https://abcde.einval.com/wiki/

**abcde mp3**
http://www.andrews-corner.org/linux/abcde/abcde_mp3.html#lame


**CD event auto-start**
https://somewideopenspace.wordpress.com/yet-another-headless-cd-ripper-and-mpd-on-raspberry-pi-installation-guide-yahcdramorpig/start-ripping-when-cd-is-inserted/
http://www.mischiefblog.com/2015/03/24/capturing-cd-rom-insert-events-in-linux/



# For developer and contributers

This section describes how to build a new RPM for cd2cloud;
I use make so it requires basic packages in your machine I recommend: python-setuptools, python-sphinx, python-devel and gcc

## RPM / Build

	$ make

	Usage: make <target> where <target> is one of

	clean     clean temp files from local workspace
	doc       generate sphinx documentation and man pages
	test      run unit tests locally
	tarball   generate tarball of project
	rpm       build source codes and generate rpm file
	srpm      generate SRPM file
	all       clean test doc rpm
	flake8    check Python style based on flake8

Running from your local machine, you can generate your own RPM running:

	$ make rpm

and if your environment is setup properly you should have your RPM at: /home/user/git/cd2cloud/rpmbuild/RPMS/x86_64/cd2cloud-0.0.1-1.x86_64.rpm

cd2cloud is being built on Fedora Copr: https://copr.fedorainfracloud.org/coprs/eduardocerqueira/cd2cloud/builds/

running a new build:

	$ copr-cli build cd2cloud https://github.com/eduardocerqueira/cd2cloud/raw/master/copr/cd2cloud-0.0.1-1.src.rpm


## install

Installing from your local machine, after you build your own RPM just run:

for Fedora:

	$ sudo dnf install /home/user/git/cd2cloud/rpmbuild/RPMS/x86_64/cd2cloud-0.0.1-1.x86_64.rpm

for RHEL and CentOS:

	$ sudo yum install /home/user/git/cd2cloud/rpmbuild/RPMS/x86_64/cd2cloud-0.0.1-1.x86_64.rpm

To install from latest RPM:

**repo:** https://copr.fedorainfracloud.org/coprs/eduardocerqueira/cd2cloud/

	$ sudo yum install https://copr-be.cloud.fedoraproject.org/results/eduardocerqueira/cd2cloud/epel-7-x86_64/00489346-cd2cloud/cd2cloud-0.0.1-1.x86_64.rpm
	$ sudo dnf install https://copr-be.cloud.fedoraproject.org/results/eduardocerqueira/cd2cloud/fedora-24-x86_64/00474191-cd2cloud/cd2cloud-0.0.1-1.x86_64.rpm


## MORE INFO

For others topics listed below, please generate the sphinx doc in your local machine running the command:

	$ make doc

and from a browser access: file:///home/user/git/cd2cloud/docs/build/html/index.html

* Install:
* Guide:
* Build:
* Development:


 ## How to contribute

 Feel free to fork and send me pacthes or messages if you think this tool can be helpful for any other scenario.

