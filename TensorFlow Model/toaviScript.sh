#!/bin/bash

for file in *.mp4; do
    # Get encoded frame rate of the input video file
    fps=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of default=noprint_wrappers=1:nokey=1 "$file")

    # Use ffmpeg to convert with the encoded frame rate
    ffmpeg -i "$file" -r "$fps" "${file%.mp4}.avi"
done
