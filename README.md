# NSFW-image-classifiacation-CpuOnly-mode-without-Docker-
This project uses Yahoo Open NSFW (Not Safe For Work) to detect images that contain pornographic content. OpenNSFW uses Caffe pretrained neural network models and has a very big success rate.

I have come across this problem on multiple projects, especially when there is user generated content, or content from an unreliable source that cannot be easily monitored. My solutions were not that good so I thought I'd give it a go.

Since I found Caffe difficult to install, I modified the Caffe cpu only mode to create this project to run Yahoo Open NSFW. I have also modified the Yahoo script to accept remote urls instead of only local images.

You can use it command line or start the build in server. The output is a float number from 0-1. Scores above 0.8 are NSFW. Everything below 0.2 is completely clean.
There are 2 ways to run nsfw-docker:

    Command Line:

      sudo python ./classify_nsfw.py [url|localfile]

    For Example:

      sudo python ./classify_nsfw.py http://www.personal.psu.edu/jul229/mini.jpg

    As a web service (using port as root):

      sudo python server.py 7981

Then to use the service:

Visit: http://127.0.0.1:7981/[url] (Image link after final /)

For example: http://127.0.0.1:7981/http://www.personal.psu.edu/jul229/mini.jpg


Sample Scores:

0.004822054877877235

![sample image](https://camo.githubusercontent.com/e08639c72acfff7b4dbf8374abd22893f004ac1a/687474703a2f2f692e6461696c796d61696c2e636f2e756b2f692f7069782f323031362f30322f30392f31382f333130374238363030303030303537382d302d52756e6e696e675f69735f6e6f745f6f6e6c795f676f6f645f666f725f796f75725f626f64795f69745f69735f62656e6566696369616c5f746f5f7468655f622d612d31355f313435353034333834333932392e6a7067)

Usually something like:

192.168.99.100

So the service can be accessed from:

http://192.168.99.100:7981
