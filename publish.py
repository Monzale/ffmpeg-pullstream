#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging as logger
import ffmpy
import mongoengine as mg,os
import requests
import json
import datetime

from models import Device
from urlparse import urlparse, ParseResult
import threading
import CommonDefine
import errno
import shlex
import subprocess
from ffmpy import FFExecutableNotFoundError
import time


class myffmpeg(ffmpy.FFmpeg):

    def sync_run(self, input_data=None, stdout=None, stderr=None):
        try:
            self.process = subprocess.Popen(
                self._cmd,
                stdin=subprocess.PIPE,
                stdout=stdout,
                stderr=stderr
            )
        except OSError as e:
            if e.errno == errno.ENOENT:
                raise FFExecutableNotFoundError("Executable '{0}' not found".format(self.executable))
            else:
                raise

    def killself(self):
        self.process.kill()

if __name__ == "__main__":
    try:
		url = "rtsp://xxxxxx"
		pushUrl = "rtmp://xxxxxx"
        ff = myffmpeg(
            inputs={url: None},
            outputs={pushUrl :'-hide_banner -loglevel panic -threads 2 -f flv -r 15 -s 1280x720 -an'}
        )
		ff.sync_run()
		time.sleep(600)
		ff.killself()
		
    except Exception as e:
        print e
