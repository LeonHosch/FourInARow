"""
This module contains the configuration settings for the game engine."""

import os
import sys

# Add the module's directory to the system path
module_path = os.path.dirname(os.path.abspath(__file__))
if module_path not in sys.path:
    sys.path.append(module_path)

AI_DIFFICULTY = "medium"  # Options: "easy", "medium", "master"
