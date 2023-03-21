from wonda.tools.loop_wrapper import LoopWrapper
from src.initialization import setup_bot, setup_database


bot = setup_bot()
bot.loop_wrapper = LoopWrapper()
bot.loop_wrapper.on_startup.append(setup_database())
