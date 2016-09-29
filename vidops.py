import subprocess as sp
import os

def extractFrames(movie_file, start_time = "00:00:00.0", end_time = None, fps = 1, crop = 'in_w:in_h'):
    '''
    Uses ffmpeg to extract frames from a video file and saves them as png files in a folder named "[movie_file] Frames" in the same directory as the video file.
    
    Parameters
    -----
    movie_file : string
        "path/to/movie.ext"
    start_time : string, optional
        "hh:mm:ss.0" format; defaults to start of video
    end_time : string, optional
        "hh:mm:ss.0" format; defaults to end of video
    fps : numeric, optional
        number of frames to grab per second; defaults to 1 frame/sec
    crop : string, optional
        "out_w:out_h:x:y" format; see ffmpeg's crop filter documentation for details'''

    movie_file_list = movie_file.replace('\\','/').split('/')
    movie_name = movie_file_list[-1]
    movie_dir = movie_file_list[:-1]
    frames_dir = movie_dir + '/' + movie_name + ' Frames'
    if not os.path.isdir(frames_dir):
        os.mkdir(frames_dir)

    # ffmpeg options
    input = '-i "' + movie_file + '"'
    start_time = '-ss' + start_time
    if end_time is not None:
        end_time = '-t ' + end_time + ' -copyts'
    stream_copy = '-c copy'
    output = frames_dir + '/out%05d.png'
    
    # filters
    fps = 'fps = ' + str(fps)
    crop = 'crop = ' + crop
    filters = '-vf "' + '; '.join([fps, crop]) + '"'

    ffmpeg_call = ['ffmpeg', start_time, input, end_time, stream_copy, filters, output]
    
    # Get rid of None arguments
    ffmpeg_call = [arg for arg in ffmpeg_call if arg is not None]
    
    sp.call(ffmpeg_call)