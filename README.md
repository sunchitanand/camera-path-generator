# [Camera Trail Generator (Indoor Trajectory Mapping)](https://youtu.be/d8Xpbr7Rzg8)

### Get the path your camera has traveled using Monocular Visual Odometry

- Can be used in supermarkets to track most vistsed shelves by attaching this technology to carts
- Can be used to make 2D line floorplans and self operate indoor navigation system using OCR

## Walkthroughs

[2D Path Tracking - Indoors](https://www.youtube.com/watch?v=hDP-BkamJuo&feature=youtu.be)

[2D Path Tracking - Cars](https://www.youtube.com/watch?v=LbZa1C9mGwQ&t=30s)


## How to Use

- Open termninal and run the command `python camera-path-generator.py`
- Select the desired option

### Requirements
- Python
- OpenCV

## How To Use With Your Own Videos

 1. After downloading/ cloning the project, save your input video in the project root folder.
 
 2. Open video2images.m and replace filename by your video name to convert your video into frames 
 
 3. Save those output frames in a separate folder and name it input_frames
 
 4. Open camera-path-generator.py and follow instructions in the file to configure 
 
 5. Open Terminal and run the command:
       `python camera-path-generator.py`
 
 6. Select your video number and watch the path get generated 
