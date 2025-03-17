"""Discord integration for Model Context Protocol."""

import asyncio
import tracemalloc
import warnings

from . import server

__version__ = "0.1.0"

def main():
    """Main entry point for the package."""
    # Enable tracemalloc for better debugging
    tracemalloc.start()
    try:
        # Properly handle async execution
        asyncio.run(server.main())
    except KeyboardInterrupt:
        print("\nShutting down Snowflake MCP server...")
    except Exception as e:
        print(f"Error running Snowflake MCP server: {e}")
        raise

# Expose important items at package level
__all__ = ['main', 'server']