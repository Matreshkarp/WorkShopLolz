# - *- coding: utf- 8 - *-
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
BOT_TOKEN = config["settings"]["token"]
main_admin = config["settings"]["main_admin"]

bot_version = "2.9"
bot_description = f"<b>♻ Bot created by @GhostRiver</b>\n" \
                  f"<b>👑 Admin-panel by @GhostRiver</b>\n" \
                  f"<b>⚜ Bot Version:</b> <code>{bot_version}</code>\n" \
                  f"<b>🔗 Topic Link:</b> <a href='https://lolz.guru/JaysonStethem'><b>Click me</b></a>\n" \
                  f"<b>🍩 Donate to the author:</b> <a href='https://qiwi.com/+79885664132'><b>Click me</b></a>"
