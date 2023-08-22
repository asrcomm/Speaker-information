#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 21:59:40 2023

@author: barshadeka
"""

import moviepy.editor
video = moviepy.editor.VideoFileClip("video2.mp4")
video.audio.write_audiofile("audio3.wav")