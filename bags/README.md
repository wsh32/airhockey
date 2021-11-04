# Bag files

Bag files! Bags should not be uploaded to github because of the size of the 
file. Instead, they should be uploaded to Google Drive and linked here.

To capture a bag file, use

```
rosbag record message
```

To play back a bag file, use

```
rosbag play bag_file.bag
```

When testing vision code, it is recommended to loop the bag file. This can be
done with the `--loop` or `-l` parameter

```
rosbag play -l bag_file.bag
```

### Links to bags:
Google drive link to the bag files:
[link](https://drive.google.com/drive/folders/10HDHJiK4U-v9Z81reNJGUbBSWGFEeh10?usp=sharing)

