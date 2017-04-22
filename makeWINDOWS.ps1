echo "hello world!"
echo "making folders..."
mkdir roboclaw
echo "now entering roboclaw..."
cd .\roboclaw
echo "now retrieving file..."
curl -outf roboclaw.zip http://downloads.ionmc.com/code/roboclaw_python.zip
echo "now extracting..."
7z e .\roboclaw.zip
echo "returning to root dir.."
cd ..
echo "done!"