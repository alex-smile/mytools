# -*- coding: utf-8 -*-
"""
适配器模式

结构型模式

将一个类的接口转换成客户希望的另外一个接口。适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。

使用场景：有动机地修改一个正常运行的系统的接口，这时应该考虑使用适配器模式
"""
from abc import ABCMeta, abstractmethod


class MediaPlayer(metaclass=ABCMeta):

    @abstractmethod
    def play(self, audio_type, filename):
        pass


class AdvancedMediaPlayer(metaclass=ABCMeta):
    @abstractmethod
    def play_vlc(self, filename):
        pass

    @abstractmethod
    def play_mp4(self, filename):
        pass


class VLCPlayer(AdvancedMediaPlayer):
    def play_vlc(self, filename):
        print(f"Playing vlc filename: {filename}")

    def play_mp4(self, filename):
        pass


class MP4Player(AdvancedMediaPlayer):
    def play_vlc(self, filename):
        pass

    def play_mp4(self, filename):
        print(f"Playing mp4 filename: {filename}")


class MediaAdapter(MediaPlayer):

    advanced_media_player = None

    def __init__(self, audio_type):
        if audio_type == "vlc":
            self.advanced_media_player = VLCPlayer()
        elif audio_type == "mp4":
            self.advanced_media_player = MP4Player()

    def play(self, audio_type, filename):
        if audio_type == "vlc":
            self.advanced_media_player.play_vlc(filename)
        elif audio_type == "mp4":
            self.advanced_media_player.play_mp4(filename)


class AudioPlayer(MediaPlayer):

    media_adapter = None

    def play(self, audio_type, filename):
        if audio_type == "mp3":
            print(f"Playing mp3 filename: {filename}")
        elif audio_type in ("vlc", "mp4"):
            self.media_adapter = MediaAdapter(audio_type)
            self.media_adapter.play(audio_type, filename)
        else:
            print(f"Invalid media. {audio_type} format not supported")


if __name__ == "__main__":
    audio_player = AudioPlayer()
    audio_player.play("mp3", "beyond the horizon.mp3")
    audio_player.play("mp4", "alone.mp4")
    audio_player.play("vlc", "far far way.vlc")
    audio_player.play("avi", "mind me.avi")
