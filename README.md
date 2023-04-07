# Extract-events-from-security-camera
Extract movement events from security camera footage and merges them for each date


# Steps to run 

## Compress files on disk
1. `tar -czvf vid4.tar.gz  dir  --remove-files`


## Prepare on aws
2. Request a spot instance (using 4x large or 2x large , compute optimized instances)
3. Add security group to enable ssh. 
4. SSH and clone the repo.
5. Run `./command.sh` 
6. [Increase volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.html#:~:text=To%20modify%20an%20EBS%20volume%20using%20the%20console) of ec2 instance and then [extend](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html) the volume.
   1. sudo lsblk
   2. sudo growpart /dev/nvme0n1 1
   3. sudo resize2fs /dev/nvme0n1p1 
7. Follow [instructions](https://kloudle.com/academy/how-to-transfer-files-between-aws-s3-and-aws-ec2/) to copy data from s3 to ec2 . Need to create IAM role first time we are doing this. 
   1. Attach role and then copy from s3 using cli. (cli is installed earlier) `aws s3 cp --recursive s3://test-s3-33434/ ~/`
8. Unzip the file 
   1. `for f in *.tar; do tar xzvf "$f"; done` 


## Prepare directory structure. 
1. Place everything in a single directory. This folder can have any  strcuture (i.e nested directories are allowed). We use root direcotry and run the script over it. 
2. Make sure all files for a single day are within one directory. we use the directory name as the final file name. 


Run 
1. python3 get_files.py