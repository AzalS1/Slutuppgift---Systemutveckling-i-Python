# Hantera övervakning (CPU, RAM , disk)

import psutil
import os

class Watcher:
    def __init__(self):
        self.active = False

    def start(self):
        self.acitve = True
        print("Övervakning startad.")

    def stop(self):
        self.active = False
        print("Övervakning stoppad")

    def status(self):
        if not self.active:
            print("Övervakaren är inaktiv")
            return None

        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        root = ps.path.abspath(os.sep)
        disk = psutil.disk_usage(root)

        print(f"CPU-anvädning: {cpu}%")
        print(f"Minnesanvädning: {mem.percent}% ({mem.used / (1024 ** 3):.2f} GB av {mem.total / (1024 ** 3):.2f} GB)")
        print(f"Diskanvändning: {disk.percent}% ({disk.used / (1024 ** 3):.2f} GB av {disk.total / (1024 ** 3):.2f} GB)")
        return cpu, mem.percent, disk.percent