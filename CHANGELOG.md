# Changelog for MC-Player-Tracker

## [1.0.0.0-beta] - 2024-01-21
### Overview
Initial beta release of MC-Player-Tracker, a tool for tracking player movements in Minecraft and visualizing them in charts.**This version uses AIGC.**

### Features
- **Tracking**: Ability to record player coordinates in the game.
- **Visualization**: Display recorded coordinates in a chart format.
- **Detail on Hover**: Show detailed information when the cursor is placed over a record point.

### Dependencies
- Requires Python 3.x.x.
- Depends on the MCPI and plotly libraries.
- Consists of two main files: `plot_footprint.py` and `record.py`.

### Setup Instructions
1. Download the MC-Player-Tracker files.
2. Modify `record.py` to include the correct server IP and port number. If the server is local, use `170.0.0.1`. The default port number, indicated by the plugin, is `4711`.
3. Adjust the recording interval by changing the value of `time.sleep(1)` within the `main` function.

### Usage Guide
1. Connect to the Minecraft server and run `record.py`.
2. Start recording by typing `record start` in the game chat.
3. Stop recording by typing `record stop`.
4. The tracks will be saved to `player_footprints.txt`. Run `plot_footprint.py` to generate the chart, which will automatically open in your browser for preview.

### Known Issues
- The initial release may have minor bugs and is intended for testing and feedback purposes.

### Contact
For more information or to report issues, please submit an issue on the [GitHub repository](https://github.com/yourusername/mc-player-tracker/issues).

### License
This project is released under the AIGC (Academic Integrity and General Conduct) license, which emphasizes the importance of academic honesty and responsible software development practices.

Please see the LICENSE file for the full text of the license.