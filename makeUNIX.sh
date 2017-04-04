echo "hello world!"
echo "making folders..."
mkdir prometheus/roboclaw
echo "now entering roboclaw..."
cd ./prometheus/roboclaw
echo "now retrieving file..."
wget "http://downloads.ionmc.com/code/roboclaw_python.zip"
echo "now extracting..."
7z e roboclaw_python.zip
rm roboclaw_python.zip
echo "touching __init__.py"
touch __init__.py
echo "returning to root dir.."
cd ../..
echo "done!"
