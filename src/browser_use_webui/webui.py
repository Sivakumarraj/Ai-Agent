"""Main WebUI application module."""

import argparse
import asyncio
import logging
import os
from pathlib import Path

import gradio as gr
from dotenv import load_dotenv

from browser_use_webui.utils.config import default_config
from browser_use_webui.utils.ui import create_ui

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def main():
    """Main entry point for the WebUI application."""
    parser = argparse.ArgumentParser(description="Browser Use WebUI")
    parser.add_argument("--ip", type=str, default="127.0.0.1", help="IP address to bind to")
    parser.add_argument("--port", type=int, default=7788, help="Port to listen on")
    args = parser.parse_args()

    # Ensure required directories exist
    Path("tmp/record_videos").mkdir(parents=True, exist_ok=True)
    Path("tmp/traces").mkdir(parents=True, exist_ok=True)
    Path("tmp/agent_history").mkdir(parents=True, exist_ok=True)

    # Create and launch UI
    config = default_config()
    demo = create_ui(config)
    demo.launch(server_name=args.ip, server_port=args.port)

if __name__ == "__main__":
    main()