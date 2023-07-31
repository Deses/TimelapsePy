"""User input values for TimelapsePy"""
__version__ = "0.0.1"
__author__ = "Ben Fisher"
# DO NOT EDIT ABOVE THIS LINE

# ======================================================================
#                      Settings for save locations
# ======================================================================

absolute_path_for_images = '/home/pi/timelapses/tmp'
absolute_path_for_videos = '/home/pi/timelapses'
unique_directory_name = False  # Recommend keeping this default = False
# Whether save the microseconds in the filename (%Y%m%d_%H%M%S_%f) or
# just save a date and time (%Y%m%d_%H%M%S).
ms_in_the_filename = True

# ======================================================================
#                 Basic settings for capturing images
# ======================================================================

# Available file formats: 'jpg', 'png', 'bmp'.
# Default is 'jpg'.
image_file_format = 'jpg'

interval_in_seconds_between_capture = 10
capture_continuously = True

# To capture images daily between the following hours, set
# capture_continuously = False, otherwise the following values
# are ignored. Use 24-hour format.
capture_start_hour = 4  # Inclusive
capture_end_hour = 18  # Exclusive

# ======================================================================
#                    Camera configuration settings
# ======================================================================

# Available resolutions:
#     'vga':   (640, 480)
#     'svga':  (800, 600)
#     'xga':   (1024, 768)
#     'hd':    (1280, 720)
#     'hd+':   (1600, 900)
#     'fhd':   (1920, 1080)
#     'qhd':   (2560, 1440)
#     '4k':    (3840, 2160)
#     'max':   (4608, 2592)
# Default is 'max'.
resolution = 'max'

# Available image formats: 'bgr888', 'rgb888', 'xbgr8888', 'xrgb8888'.
# Default is 'bgr888'.
image_format = 'bgr888'
image_quality = 90

flip_horizontal = False
flip_vertical = False

override_default_focus_settings = False

# Focal modes are 'manual', 'auto' and 'continuous'. Default is 'auto'.
# Focal distance ranges from 0.1 cm (10) to infinity (0)
user_focus_mode = 'auto'
user_focal_distance = 0


# ======================================================================
#                        Render to mp4 video
# ======================================================================

create_mp4 = False
video_name = "video"
frame_rate = 24

# DO NOT EDIT BELOW THIS LINE
print(f"usersettings.py <version {__version__}> imported.")
