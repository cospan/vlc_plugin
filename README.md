Generic VLC Video Output Plugin
=====================

A geneic VLC 'out of tree' code base that can be used to write a VLC Video Output Plugin.

To get started (Assuming this will be built on an Ubuntu platform):

1. If you don't have scons install it: sudo apt-get install scons
2. Follow the instructions for 'Installing the development files' from this page: https://wiki.videolan.org/OutOfTreeCompile/
2. Clone this repo
3. Go in the newly created vlc_plugin directory
4. build using scons: (type 'scons')
5. install (assuming VLC video output plugins are in /usr/lib/vlc/plugins/video_output) by typing ('sudo scons install')
6. run vlc (type 'vlc')
7. Go to preferences (either 'ctrl+p' or tools->preferences) select 'video' from the left and then from the 'output' combox select 'My Video Output'
8. Play a video and bask in the debug output (if you ran vlc from the command line)
