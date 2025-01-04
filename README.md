# MC-Player-Tracker
# MC玩家追踪器

#### Example
#### 示例
Record coordinates in the game, and then display them in the form of a chart:
在游戏中记录坐标，然后以图表形式展示：

![Example](/assets/img/2025/01-04/a.png)


Hover over a record point to see detailed information.
将鼠标悬停在记录点上查看详细信息。

![Example 2](/assets/img/2025/01-04/b.png)


#### Dependencies
#### 依赖
There are two files: `plot_footprint.py` and `record.py`.
包含两个文件：`plot_footprint.py` 和 `record.py`。

Ensure you are using Python version 3.x.x.
确保你使用的是 Python 3.x.x 版本。

Make sure the `mcpi` and `plotly` libraries are installed.
确保已经安装了 `mcpi` 和 `plotly` 库。

Both files should be in the same directory.
两个文件应该位于同一目录下。

Ensure you have entered the correct server IP address and port number in `record.py`.
确保在 `record.py` 中正确输入了服务器的 IP 地址和端口号。

#### Deployment
#### 部署
1. Download the files from [MC-Player-Tracker](https://github.com/BG4JTS/BG4JTS-MC-Player-Tracker).
1. 从 [MC-Player-Tracker](https://github.com/BG4JTS/BG4JTS-MC-Player-Tracker) 下载文件。

2. Open `record.py` to modify the IP and port number. If the server is local, use `localhost` or `127.0.0.1`. The port number is indicated by the plugin when the server starts, with the default being `4711`.
2. 打开 `record.py` 以修改 IP 地址和端口号。如果服务器在本地，使用 `localhost` 或 `127.0.0.1`。端口号由插件在服务器启动时提示，默认为 `4711`。

3. To change the recording interval, find `def main` and adjust the value of `time.sleep()`, e.g., `time.sleep(5)` for a 5-second interval.
3. 要改变记录间隔，找到 `def main` 并调整 `time.sleep()` 的值，例如 `time.sleep(5)` 表示 5 秒的间隔。

#### Usage Guide
#### 使用指南
1. Connect to the server in the game and run `record.py`.
1. 在游戏中连接到服务器并运行 `record.py`。

2. In the game, type `/record start` in the chat to begin recording.
2. 在游戏中，在聊天栏输入 `/record start` 开始记录。

3. To stop recording, type `/record stop`.
3. 要停止记录，输入 `/record stop`。

4. The tracks will be saved to `player_footprints.txt`. Run `plot_footprint.py` to generate the chart, which will automatically open in your browser for preview.
4. 足迹将被保存到 `player_footprints.txt`。运行 `plot_footprint.py` 来生成图表，它将自动在浏览器中打开以供预览。