# # from moviepy.editor import VideoFileClip, concatenate_videoclips
# import os
# import subprocess


# # def merge_mp4_files(root_dir):
# #     # Get a list of all subdirectories in the root directory
# #     subdirectories = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]

# #     # Merge all MP4 files in each subdirectory
# #     for subdir in subdirectories:
# #         mp4_files = [f for f in os.listdir(os.path.join(root_dir, subdir)) if f.endswith('.mp4')]

# #         # Create a list of VideoFileClip objects for each MP4 file
# #         video_clips = [VideoFileClip(os.path.join(root_dir, subdir, f)) for f in mp4_files]

# #         # Concatenate all the clips into a single clip
# #         final_clip = concatenate_videoclips(video_clips)

# #         # Write the final clip to a file named "output.mp4" in the subdirectory
# #         output_filename = os.path.join(root_dir, subdir, 'output.mp4')
# #         final_clip.write_videofile(output_filename)

# #         # Delete the original MP4 files
# #         for f in mp4_files:
# #             os.remove(os.path.join(root_dir, subdir, f))

# #         print(f"Merged {len(mp4_files)} MP4 files in {subdir} into {output_filename}")

# # # Merge all MP4 files in each subdirectory of the root directory recursively
# # merge_mp4_files('/Users/prashantkhurana/Documents/temp/')

# # import os
# # import ffmpeg

# # input_dir = '/Users/prashantkhurana/Documents/temp/2022110714'
# # output_file = 'output.mp4'

# # input_args = []
# # for file in os.listdir(input_dir):
# #     if file.endswith('.mp4'):
# #         input_args.extend(['-i', os.path.join(input_dir, file)])

# # output_args = ['-filter_complex', f'concat=n={len(input_args) // 2}:v=1:a=1', '-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental', output_file]
# # print(input_args)
# # ffmpeg.concat(*input_args, *output_args).run()

# root_dir = "/Users/prashantkhurana/Documents/temp"
# subdirectories = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]
# for subdir in subdirectories:
#         subdir_path = os.path.join(root_dir, subdir)
#         print(os.path.join(root_dir, subdir))
#         p = subprocess.Popen(["find *.mp4 | sed 's:\ :\\\ :g'| sed 's/^/file /' > fl.txt; ffmpeg -f concat -i fl.txt -c copy output.mkv; rm fl.txt"], shell=True,cwd=subdir_path)
#         p.wait()
#         old_files = [f for f in os.listdir(os.path.join(root_dir, subdir))]
#         p = subprocess.Popen(["ffmpeg -i output.mkv -vf 'scale=trunc(iw/4)*2:trunc(ih/4)*2' -c:v libx265 -crf 28 half_the_frame_size2.mkv"], shell=True,cwd=subdir_path)
#         p.wait()
#         for f in old_files:
#             os.remove(os.path.join(subdir_path, f))


# from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import subprocess
# from pathlib import Path



# def merge_mp4_files(root_dir):
#     # Get a list of all subdirectories in the root directory
#     subdirectories = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]

#     # Merge all MP4 files in each subdirectory
#     for subdir in subdirectories:
#         mp4_files = [f for f in os.listdir(os.path.join(root_dir, subdir)) if f.endswith('.mp4')]

#         # Create a list of VideoFileClip objects for each MP4 file
#         video_clips = [VideoFileClip(os.path.join(root_dir, subdir, f)) for f in mp4_files]

#         # Concatenate all the clips into a single clip
#         final_clip = concatenate_videoclips(video_clips)

#         # Write the final clip to a file named "output.mp4" in the subdirectory
#         output_filename = os.path.join(root_dir, subdir, 'output.mp4')
#         final_clip.write_videofile(output_filename)

#         # Delete the original MP4 files
#         for f in mp4_files:
#             os.remove(os.path.join(root_dir, subdir, f))

#         print(f"Merged {len(mp4_files)} MP4 files in {subdir} into {output_filename}")

# # Merge all MP4 files in each subdirectory of the root directory recursively
# merge_mp4_files('/Users/prashantkhurana/Documents/temp/')

# import os
# import ffmpeg

# input_dir = '/Users/prashantkhurana/Documents/temp/2022110714'
# output_file = 'output.mp4'

# input_args = []
# for file in os.listdir(input_dir):
#     if file.endswith('.mp4'):
#         input_args.extend(['-i', os.path.join(input_dir, file)])

# output_args = ['-filter_complex', f'concat=n={len(input_args) // 2}:v=1:a=1', '-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental', output_file]
# print(input_args)
# ffmpeg.concat(*input_args, *output_args).run()
from datetime import datetime

root_dir = "/home/ubuntu/temp/"
#root_dir = "/Users/prashantkhurana/Documents/temp"
for (root, dirs, files) in os.walk(root_dir, topdown=True):
    for name in dirs:
        dir_path = os.path.join(root, name)
        print("prashant processing folder " + dir_path)
        try :
            datetime_object = datetime.strptime(name, '%Y%m%d%H')
            if datetime_object.hour >= 23 or datetime_object.hour <= 5 :
                for f in os.listdir(dir_path) :
                    os.remove(os.path.join(dir_path, f))
                print('prashant deleted folder ' + dir_path)    
                continue
        except ValueError as e :
            print ('prashant Folder not of format datetime')
            continue    
        has_mp4_file = False
        for file in os.listdir(dir_path):
            #print(file)
            if (file.endswith('.mp4')):
                has_mp4_file = True
                # print(name)
                # datetime_object = datetime.strptime(name, '%Y%m%d%H')
                # print(datetime_object)
                # if datetime_object.hour < 23 and datetime_object.hour > 5 :
                #     has_mp4_file = True
        print("prashant processing folder " + dir_path + "with mp4 files " + str(has_mp4_file))
        if has_mp4_file == True:
            print("prashant merging files")
            p = subprocess.Popen(
                ["find *.mp4 | sed 's:\ :\\\ :g'| sed 's/^/file /' > fl.txt; ffmpeg -f concat -i fl.txt -c copy output.mkv; rm fl.txt"], shell=True, cwd=dir_path)
            p.wait()
            print("prashant detecting events files")
            # p = subprocess.Popen(
            # ["dvr-scan -i output.mkv -so -c ~/Documents/code/extract-events/dvr-scan.cfg"], shell=True, cwd=dir_path)
            # print("ddddddddd")
            # out, err = p.communicate();
            # print("dddddd" + str(out))
            p = subprocess.Popen(
            ["dvr-scan -i output.mkv -m ffmpeg -c /home/ubuntu/extract-events/dvr-scan.cfg"], shell=True, cwd=dir_path)
            p.wait()
            old_files = [f for f in os.listdir(dir_path)]
            print("prashant merging events files")
            p = subprocess.Popen(
                ["find output.DSME*.mp4 | sed 's:\ :\\\ :g'| sed 's/^/file /' > fl.txt; ffmpeg -f concat -i fl.txt -c copy final.mp4; rm fl.txt"], shell=True, cwd=dir_path)
            p.wait()
                # p = subprocess.Popen(
                # ["ffmpeg -i output.mkv -vf 'scale=trunc(iw/4)*2:trunc(ih/4)*2' -c:v libx265 -crf 28 half_the_frame_size2.mkv"], shell=True, cwd=dir_path)
                # p.wait()
            print("prashant removing files")
            for f in old_files:
                os.remove(os.path.join(dir_path, f))
            if os.path.isfile(dir_path +'/final.mp4') :
                print("prashant renaming files")
                os.rename(dir_path +'/final.mp4', dir_path + '/' + name + '.mp4')
            else :
                print("prashant no event_detected")
        else :
            for f in os.listdir(dir_path) :
                os.remove(os.path.join(dir_path, f))
            print('deleted folder with no mp4 files' + dir_path)

# subdirectories = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]
# for subdir in subdirectories:
#         subdir_path = os.path.join(root_dir, subdir)
#         print(os.path.join(root_dir, subdir))
#         p = subprocess.Popen(["find *.mp4 | sed 's:\ :\\\ :g'| sed 's/^/file /' > fl.txt; ffmpeg -f concat -i fl.txt -c copy output.mkv; rm fl.txt"], shell=True,cwd=subdir_path)
#         p.wait()
#         old_files = [f for f in os.listdir(os.path.join(root_dir, subdir))]
#         p = subprocess.Popen(["ffmpeg -i output.mkv -vf 'scale=trunc(iw/4)*2:trunc(ih/4)*2' -c:v libx265 -crf 28 half_the_frame_size2.mkv"], shell=True,cwd=subdir_path)
#         p.wait()
#         for f in old_files:
#             os.remove(os.path.join(subdir_path, f))
