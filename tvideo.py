"""TimelapsePy utility for creating mp4 from time-lapse photos using ffmpeg"""
__version__ = "0.0.5"
__author__ = "Ben Fisher"

print(f"tvideo.py <version {__version__}> imported.")

import glob
import os

import tlogger as log
import tutilities as utils
import usersettings as users

img_folder = os.path.join(users.absolute_path_for_images)
work_folder = os.path.join(users.absolute_path_for_images + "/workdir")
output_path = os.path.join(users.absolute_path_for_videos, f'{users.video_name}.mp4')

imgs_in_folder = img_folder + '/*.' + utils.get_file_format(users.image_file_format)
imgs_in_work_folder = work_folder + '/*.' + utils.get_file_format(users.image_file_format)

video_resolution = utils.get_resolution_multiplication(users.resolution)

# For command line documentation refer to https://ffmpeg.org/ffmpeg.html
try:
    log.logger.info(log.message['video_render'])
    log.logger.info(log.message['mv_files'])
    mvResult = os.system(f'mv {imgs_in_folder} {work_folder}')
    if mvResult == 0:
        log.logger.info(log.message['mv_files_end'])
    else:
        log.logger.info(log.message['no_files'])
        log.logger.info(log.message['mv_files_end'])

    log.logger.info(log.message['render_start'])
    ffResult = os.system(f'ffmpeg -r {users.frame_rate} -pattern_type glob -i "{imgs_in_work_folder}" ' +
                         f'-s:v {video_resolution} -c:v libx264 -pix_fmt yuvj420p -y {output_path}')
    if ffResult == 0:
        log.logger.info(log.message['render_end'])

        if users.delete_after_creation:
            log.logger.info(log.message['delete_stills'])
            files = glob.glob(work_folder + '/*')
            for f in files:
                os.remove(f)
    else:
        log.logger.info(log.message['render_failed'])

except Exception as e:
    log.logger.error(log.message['error'], 'division', exc_info=e)
    print("An error occurred in rendering. Exiting tvideo.py.")
