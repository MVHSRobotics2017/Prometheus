#Following tutorial @ https://diyhacking.com/raspberry-pi-webcam-robot/
sudo apt-get install ffmpeg
sudo apt-get install libv4l-dev
sudo apt-get install libjpeg8-dev
sudo apt-get install subversion
sudo apt-get install imagemagick
svn co https://svn.code.sf.net/p/mjpg-streamer/code/
cd /home/pi/code/mjpg-streamer/
make USE_LIBV4L2=true clean all
sudo make DESTDIR=/usr install

