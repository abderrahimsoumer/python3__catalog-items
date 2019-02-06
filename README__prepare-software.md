
## Prepare the software
    *Copied from udacity Full Stack Web Developer Nanodegree*
+ ## Installing the Virtual Machine
   In the next part of this course, you'll use a virtual machine (VM) to run an SQL database server and a web app that uses it. The VM is a Linux server system that runs on top of your own computer. You can share files easily between your computer and the VM; and you'll be running a web service inside the VM which you'll be able to access from your regular browser.

   We're using tools called [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to install and manage the VM. You'll need to install these to do some of the exercises. The instructions on this page will help you do this.

  **Conceptual overview**
  
  [This video](https://www.youtube.com/watch?v=djnqoEO2rLc) offers a conceptual overview of virtual machines and Vagrant. You don't need to watch it to proceed, but you may find it informative.
  
  <hr />
  
  **Use a terminal**
  
   You'll be doing these exercises using a Unix-style terminal on your computer. If you are using a Mac or Linux system, your regular terminal program will do just fine. On Windows, we recommend using the Git Bash terminal that comes with the Git software. If you don't already have Git installed, download Git from [git-scm.com.](https://git-scm.com/downloads)

  For a refresher on using the Unix shell, look back at our [Shell Workshop.](https://www.udacity.com/course/ud206)

  If you'd like to learn more about Git, take a look at our [course about Git.](https://www.udacity.com/course/ud123)

   <hr />

   **Install VirtualBox**
   
  VirtualBox is the software that actually runs the virtual machine. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

  Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

  **Ubuntu users:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.
  
  <hr />
  
  **Install Vagrant**
  
  Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.

  **Windows users:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.
  
  ![vagrant version](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/584881ee_screen-shot-2016-12-07-at-13.40.43/screen-shot-2016-12-07-at-13.40.43.png "vagrant version")
  
  
+ ## Download the VM configuration

  There are a couple of different ways you can download the VM configuration.

  You can download and unzip this file:  [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)  This will give you a directory called  **FSND-Virtual-Machine**. It may be located inside your  **Downloads**  folder.

  Alternately, you can use Github to fork and clone the repository  [https://github.com/udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm).

  Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with  `cd`. Inside, you will find another directory called  **vagrant**. Change directory to the  **vagrant**  directory:


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Navigating to the FSND-Virtual-Machine directory and listing the files in it.](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58487f12_screen-shot-2016-12-07-at-13.28.31/screen-shot-2016-12-07-at-13.28.31.png)



+ ## Start the virtual machine

  From your terminal, inside the  **vagrant**  subdirectory, run the command  `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Starting the Ubuntu Linux installation with `vagrant up`](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488603_screen-shot-2016-12-07-at-13.57.50/screen-shot-2016-12-07-at-13.57.50.png)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;When  `vagrant up`  is finished running, you will get your shell prompt back. At this point, you can run  `vagrant ssh`  to log in to your newly installed Linux VM!


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![Logging into the Linux VM with `vagrant ssh`.](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488962_screen-shot-2016-12-07-at-14.12.29/screen-shot-2016-12-07-at-14.12.29.png)

+ ## Logged in!

  If you are now looking at a shell prompt that starts with the word  `vagrant`  (as in the above screenshot), congratulations — you've gotten logged into your Linux VM.

  If not, take a look at the  **Troubleshooting**  section below.


+ ## Troubleshooting

  + ### I'm not sure if it worked.

    If you can type  `vagrant ssh`  and log into your VM, then it worked! It's normal for the  `vagrant up`process to display a lot of text in many colors, including sometimes scary-looking messages in red, green, and purple. If you get your shell prompt back at the end, and you can log in, it should be OK.

  + ### `vagrant up`  is taking a long time. Why?

    Because it's downloading a whole Linux operating system from the Internet.

   + ### I'm on Windows, and when I run  `vagrant ssh`, I don't get a shell prompt.

     Some versions of Windows and Vagrant have a problem communicating the right settings for the terminal. There is a workaround: Instead of  `vagrant ssh`, run the command  `winpty vagrant ssh`  instead.

    + ### I'm on Windows and getting an error about virtualization.

      Sometimes other virtualization programs such as Docker or Hyper-V can interfere with VirtualBox. Try shutting these other programs down first.

      In addition, some Windows PCs have settings in the BIOS or UEFI (firmware) or in the operating system that disable the use of virtualization. To change this, you may need to reboot your computer and access the firmware settings.  [A web search](https://www.google.com/search?q=enable%20virtualization%20windows%2010)  can help you find the settings for your computer and operating system. Unfortunately there are so many different versions of Windows and PCs that we can't offer a simple guide to doing this.

     + ### Why are we using a VM? It seems complicated.

        It is complicated. In this case, the point of it is to be able to offer the same software (Linux and PostgreSQL) regardless of what kind of computer you're running on.

     + ### I got some other error message.

        If you're getting a specific textual error message, try looking it up on your favorite search engine. If that doesn't help, take a screenshot and post it to the discussion forums, along with as much detail as you can provide about the process you went through to get there.

     + ### If all else fails, try an older version.

        Udacity mentors have noticed that some newer versions of Vagrant don't work on all operating systems. Version 1.9.2 is reported to be stabler on some systems, and version 1.9.1 is the supported version on Ubuntu 17.04. You can download older versions of Vagrant from  [the Vagrant releases index](https://releases.hashicorp.com/vagrant/).
