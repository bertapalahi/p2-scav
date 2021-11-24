
import subprocess

#exercise 1
def cut_N_seconds(name, N):
    cmd = ["ffmpeg", "-i", name, "-ss", "00:00:00", "-to", N, "-c", "copy", "output_video.mp4"]
    subprocess.check_output(cmd)

#exercise 2
def extract_spectogram(video):
    cmd = ["ffplay", video, "-vf", "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay"]
    subprocess.check_output(cmd)

#exercise 3: resize the video into 4 differents video outputs
def resize_video(video, factor):
    cmd = "ffmpeg -i {video} -vf scale={factor} resized_video.mp4".format(video=video, factor=factor)
    subprocess.call(cmd, shell=True)

#exercise 4: audio -> mono output, different audio codec
def mono_converter(video):
    cmd = "ffmpeg -i '{video}' -map_channel 0.1.0 -c:v copy mono.mp4".format(video=video)
    subprocess.call(cmd, shell=True)

def ogg_converter(video):
    cmd = "ffmpeg -i '{video}' video_in_wav.wav video_in_ogg.ogg".format(video=video)
    subprocess.call(cmd, shell=True)

def wav_converter(video):
    cmd = "ffmpeg -i '{video}' video_in_wav.wav".format(video=video)
    subprocess.call(cmd, shell=True)

def mp3_converter(video):
    cmd = "ffmpeg -i '{video}' BBB__mp3.mp3".format(video=video)
    subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    input_video = "BBB.mp4"

    ####### ex1 #######
    #N = input("Type seconds(00:00:xx): \n")
    #cut_N_seconds(input_video, N)

    ####### ex2 #######
    #extract_spectogram(input_video)

    ####### ex3 #######
    scale_factor = ['1280:720', '854:480', '360:240', '160:120']
    resize_video(input_video, scale_factor[2])

    ####### ex4 #######
    #ogg_converter(input_video)
    #mp3_converter(input_video)
    #wav_converter(input_video)
    #mono_converter(input_video)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
