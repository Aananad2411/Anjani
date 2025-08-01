"""Bot entry"""
# Copyright (C) 2020 - 2023  UserbotIndo Team, <https://github.com/userbotindo.git>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging

from anjani.core.anjani_bot import AnjaniBot

# Logger setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
)
logger = logging.getLogger("Anjani")

def main():
    logger.info("🚀 Starting Anjani Userbot...")
    try:
        app = AnjaniBot()
        app.run()
    except Exception as e:
        logger.error(f"❌ Failed to start AnjaniBot: {e}", exc_info=True)

if __name__ == "__main__":
    main()
