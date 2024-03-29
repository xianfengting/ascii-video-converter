# -*- coding:utf-8 -*-

import os
from PIL import Image, ImageFont, ImageDraw
from src import ascii_tools
import progressbar as pbar
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import shutil

RAW_PICTURES_DIR = "./tmp/pictures"
ASCII_PICTURES_DIR = "./tmp/ascii-pictures"
BGM_FILE_PATH = "./tmp/bgm.mp3"
MAX_THREAD_COUNT = 16

thread_lock = threading.Lock()

def convert_picture_to_ascii(picture_path, output_path):
    #print("Converting \"{}\" to \"{}\"".format(picture_path, output_path))
    im = Image.open(picture_path)
    WIDTH = int(im.width/6)  # 高度比例为原图的1/6较好，由于字体宽度
    HEIGHT = int(im.height/15)  # 高度比例为原图的1/15较好，由于字体高度
    im_txt = Image.new("RGB", (im.width, im.height), (255, 255, 255))
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt = ""
    colors = []
    for i in range(HEIGHT):
        for j in range(WIDTH):
            pixel = im.getpixel((j, i))
            colors.append((pixel[0], pixel[1], pixel[2]))  # 记录像素颜色信息
            if(len(pixel) == 4):
                txt += ascii_tools.get_char_by_ARGB(pixel[0], pixel[1], pixel[2], pixel[3])
            else:
                txt += ascii_tools.get_char_by_ARGB(pixel[0], pixel[1], pixel[2])
        txt += '\n'
        colors.append((255, 255, 255))
    dr = ImageDraw.Draw(im_txt)
    font = ImageFont.load_default().font  # 获取字体
    x = y = 0
    # 获取字体的宽高
    font_w, font_h = font.getsize(txt[1])
    font_h *= 1.37  # 调整后更佳
    # ImageDraw为每个ascii码进行上色
    for i in range(len(txt)):
        if(txt[i] == '\n'):
            x += font_h
            y = -font_w
        dr.text([y, x], txt[i], colors[i])
        y += font_w
    # 输出
    im_txt.save(output_path)

def convert_video_to_pictures(video, output_path):
    check_for_dirs(output_path)
    os.system("ffmpeg -i {} -r 25 {}/%05d.png".format(video, output_path))

def convert_video_to_BGM(video, output_file_path):
    os.system("ffmpeg -i {} -r 25 {}".format(video, output_file_path))

def convert_pictures_to_ascii_pictures(raw_pictures_path, output_path):
    check_for_dirs(output_path)
    widgets = [pbar.Percentage(), " (", pbar.SimpleProgress('/'), ") ", pbar.Bar('#'), ' ', pbar.Timer(),
            ' ', pbar.ETA(), ' ', pbar.FileTransferSpeed()]
    progress_bar = pbar.ProgressBar(widgets=widgets, maxval=len(os.listdir(raw_pictures_path)))
    progress_bar.start()
    current_progress = 0
    with ThreadPoolExecutor(MAX_THREAD_COUNT) as executor:
        task_list = []
        for raw_picture_name in os.listdir(raw_pictures_path):
            raw_picture_path = os.path.join(raw_pictures_path, raw_picture_name)
            if os.path.isfile(raw_picture_path):
                output_picture_path = os.path.join(output_path, raw_picture_name)
                #convert_picture_to_ascii(raw_picture_path, output_picture_path)
                task_list.append(executor.submit(convert_picture_to_ascii,\
                        picture_path=raw_picture_path, output_path=output_picture_path))
        for task in as_completed(task_list):
            current_progress += 1
            progress_bar.update(current_progress)
    progress_bar.finish()

def convert_pictures_and_BGM_to_video(pictures_path_template, bgm_path, output_file_path):
    #os.system("ffmpeg -i {} -r 30 -strict -2 {}".format(pictures_path_template, "./tmp/video-no-bgm.mp4"))
    #os.system("ffmpeg -i {} -i {} -r 30 -strict -2 {}".format("./tmp/video-no-bgm.mp4",\
    #        bgm_path, output_file_path))
    os.system("ffmpeg -i {} -i {} -r 25 -strict -2 -vcodec mpeg4 {}".format(pictures_path_template, bgm_path, output_file_path))

def check_for_dirs(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def delete_temp_dirs():
    shutil.rmtree("./tmp")

def main(input_file, output_file):
    convert_video_to_pictures(input_file, RAW_PICTURES_DIR)
    convert_video_to_BGM(input_file, BGM_FILE_PATH)
    convert_pictures_to_ascii_pictures(RAW_PICTURES_DIR, ASCII_PICTURES_DIR)
    convert_pictures_and_BGM_to_video("{}/%05d.png".format(ASCII_PICTURES_DIR),\
            BGM_FILE_PATH, output_file)
    delete_temp_dirs()
