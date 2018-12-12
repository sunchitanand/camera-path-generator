 vid=VideoReader('education-science-sample.mp4');
 numFrames = vid.NumberOfFrames;
 n=numFrames;
 x = 0
 for i = 1:3:n
     frames = read(vid,i);
     frames = rgb2gray(frames);
     imwrite(frames,[num2str(x,'%06.f'), '.jpg']);
     im(i)=image(frames);
     x = x+1;
 end