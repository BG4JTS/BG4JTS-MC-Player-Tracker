"""
Copyright (c) 2024 by BG4JTS
All rights reserved.

MC-Player-Tracker
record.py
Version: 1.0.0-beta
=====================:)

A simple Python script to track player movements in Minecraft.

Author: BG4JTS
GitHub: https://github.com/BG4JTS
Date: 2024-01-04

License: MIT License (see LICENSE file for details)

"""



from mcpi.minecraft import Minecraft
from mcpi import block
import time
from datetime import datetime

# 初始化 Minecraft 对象
# Initialize the Minecraft object
mc = Minecraft.create()

# 记录状态
# Recording status
recording = False
# 存储位置数据的列表
# List to store position data
positions = []

def start_recording():
    global recording
    recording = True
    print("开始记录...")  # Start recording...
    print("Starting recording...")

def stop_recording():
    global recording
    recording = False
    save_positions_to_file()
    print("停止记录并已保存数据。")  # Stop recording and data has been saved.
    print("Stopped recording and data has been saved.")

def log_position():
    global positions
    if recording:
        position = mc.player.getTilePos()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        positions.append((position.x, position.y, position.z, timestamp))
        print(f"记录位置: {position} at {timestamp}")  # Record position: {position} at {timestamp}
        print(f"Recording position: {position} at {timestamp}")

def save_positions_to_file(filename="player_footprints.txt"):
    with open(filename, "w") as file:
        for pos in positions:
            file.write(f"{pos[0]},{pos[1]},{pos[2]},{pos[3]}\n")

def main():
    while True:
        # 检查玩家聊天命令
        # Check for player chat commands
        for event in mc.events.pollChatPosts():
            if event.message.lower() == "record start":
                start_recording()
            elif event.message.lower() == "record stop":
                stop_recording()
        
        if recording:
            log_position()
        time.sleep(1)  # 每秒检查一次
        # Check once per second

if __name__ == "__main__":
    main()