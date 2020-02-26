# NSFW-image-classifiacation-cpu-mode-witout-Docker-
This project uses Yahoo Open NSFW (Not Safe For Work) to detect images that contain pornographic content. OpenNSFW uses Caffe pretrained neural network models and has a very big success rate.

I have come across this problem on multiple projects, especially when there is user generated content, or content from an unreliable source that cannot be easily monitored. My solutions were not that good so I thought I'd give it a go.

Since I found Caffe difficult to install, I modified the Caffe cpu only mode to create this project to run Yahoo Open NSFW. I have also modified the Yahoo script to accept remote urls instead of only local images.

You can use it command line or start the build in server. The output is a float number from 0-1. Scores above 0.8 are NSFW. Everything below 0.2 is completely clean.
There are 2 ways to run nsfw-docker:

    Command Line:

      sudo python ./classify_nsfw.py [url|localfile]

    For Example:

      sudo python ./classify_nsfw.py http://www.personal.psu.edu/jul229/mini.jpg

    As a web service (./run_server.sh as root):

      sudo python server.py 7981

Then to use the service:

Visit: http://127.0.0.1:7981/[url] (Image link after final /)

For example: http://127.0.0.1:7981/http://www.personal.psu.edu/jul229/mini.jpg


Sample Scores:


