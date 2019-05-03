# -*- coding: utf-8 -*-
import imageio

imageio.plugins.ffmpeg.download()

import wave
import os
import moviepy.editor as mpy
import datetime
from imageio import imwrite


class Shot:

  def __init__(self, data):
    self.data = data

  def save_screenshot(self, name='generated_img.jpg'):
    imwrite(name, self.data)


class Clip:
  def __init__(self, path=None, clipdata=None):
    if path:
      self.clip = mpy.VideoFileClip(path)
    elif clipdata:
      self.clip = clipdata

  def gif(self, starting_time='00:00:00', ending_time='00:00:03'):
    return Clip(clipdata=self.clip.subclip(starting_time, ending_time))

  def save_gif(self, name='generated_video.gif'):
    self.clip.resize(0.2).write_gif(name, fps=60, fuzz=2)

  def screenshot(self, time='00:00:00', file_name='generated_img.jpg'):
    return Shot(self.clip.get_frame(time))
