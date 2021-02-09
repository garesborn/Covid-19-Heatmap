import glob
import imageio
import moviepy.editor as mp

frames = []

# create file list from files ending in '_US.png' in directory 
file_list = glob.glob('*_US.png') # Get all the pngs in the current directory

# c is used to skip every other frame to keep gif under 10 MB github limit
c = 0
for i in file_list:
    if c == 0:
        print(i)
        frames.append(imageio.imread(i))
        c = 1
    else:
        c = 0
        pass

#save gif
imageio.mimsave('C:/Users/Gar/OneDrive/Covid-19/US_Data/American_Covid_cases.gif', frames)

#create additional mp4 from gif
clip = mp.VideoFileClip("American_Covid_cases.gif")
clip.write_videofile("US_Covid_cases.mp4")
