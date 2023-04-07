sudo apt-get --assume-yes install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
sudo apt --assume-yes update
sudo apt --assume-yes install ffmpeg
sudo apt --assume-yes install python3-pip
sudo pip install --upgrade dvr-scan[opencv]
sudo apt-get --assume-yes install unzip
sudo apt-get --assume-yes install awscli
mkdir raw_files
aws s3 cp --recursive s3://test-s3-33434/ ~/raw_files/


# sudo apt --assume-yes  upgrade

# scp -i ~/Documents/ec2/encode.cer -r ~/Documents/temp/MIJIA_RECORD_VIDEO2.zip   ubuntu@ec2-43-204-107-228.ap-south-1.compute.amazonaws.com:~/

# scp -i ~/Documents/ec2/encode.cer -r ubuntu@ec2-43-204-107-228.ap-south-1.compute.amazonaws.com:~/temp/ ~/Documents/temp/encoded


