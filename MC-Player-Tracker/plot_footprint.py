"""
Copyright (c) 2024 by Your Name
All rights reserved.

MC-Player-Tracker
=====================:)

A simple Python script to track player movements in Minecraft.

Author: BG4JTS
GitHub: https://github.com/BG4JTS
Date: 2024-01-04

License: MIT License (see LICENSE file for details)

"""


import plotly.graph_objects as go
from datetime import datetime
import pandas as pd
from typing import List, Tuple
import numpy as np

def load_positions(filename: str) -> List[Tuple[float, float, float, datetime]]:
    """
    Load position data from file using pandas for better performance
    Returns: List of tuples containing (x, y, z, timestamp)
    """
    try:
        # Use pandas for efficient file reading
        df = pd.read_csv(filename, 
                        names=['x', 'y', 'z', 'timestamp'],
                        parse_dates=['timestamp'])
        return list(zip(df['x'], df['y'], df['z'], df['timestamp']))
    except Exception as e:
        print(f"Error loading position data: {e}")
        return []

def generate_footprint_map(positions: List[Tuple[float, float, float, datetime]]) -> None:
    """
    Generate interactive 3D visualization of player movement
    Args:
        positions: List of (x, y, z, timestamp) tuples
    """
    if not positions:
        print("No data to display")
        return

    try:
        # Convert to numpy arrays for better performance
        x = np.array([p[0] for p in positions])
        y = np.array([p[1] for p in positions])
        z = np.array([p[2] for p in positions])
        timestamps = np.array([p[3] for p in positions])

        # Calculate time differences for color gradient
        start_time = min(timestamps)
        time_diffs = [(t - start_time).total_seconds() for t in timestamps]

        # Create interactive 3D scatter plot
        fig = go.Figure(data=[go.Scatter3d(
            x=x,
            y=z,  # Swap y and z for better visualization
            z=y,
            mode='markers',
            marker=dict(
                size=5,
                color=time_diffs,
                colorscale='Viridis',
                colorbar=dict(
                    title='Time (seconds)',
                    thickness=20
                ),
                showscale=True,
                opacity=0.8
            ),
            hovertemplate=(
                'X: %{x:.2f}<br>'
                'Y: %{z:.2f}<br>'
                'Z: %{y:.2f}<br>'
                'Time: %{text}<br>'
                '<extra></extra>'
            ),
            text=[t.strftime('%Y-%m-%d %H:%M:%S') for t in timestamps]
        )])

        # Update layout with improved aesthetics
        total_time = (max(timestamps) - start_time).total_seconds()
        fig.update_layout(
            title=dict(
                text=f'Player Movement Map<br>Total Time: {total_time:.1f} seconds',
                x=0.5,
                y=0.95
            ),
            scene=dict(
                xaxis_title='X Coordinate',
                yaxis_title='Z Coordinate',
                zaxis_title='Y Coordinate',
                aspectmode='data',
                camera=dict(
                    up=dict(x=0, y=0, z=1),
                    center=dict(x=0, y=0, z=0),
                    eye=dict(x=1.5, y=1.5, z=1.5)
                )
            ),
            showlegend=False,
            margin=dict(l=0, r=0, t=30, b=0)
        )

        # Show the interactive plot
        fig.show()

    except Exception as e:
        print(f"Error generating footprint map: {e}")

def main() -> None:
    try:
        filename = "player_footprints.txt"
        positions = load_positions(filename)
        generate_footprint_map(positions)
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
