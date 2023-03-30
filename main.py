from bot import Bot

bot: Bot = Bot()

if __name__ == '__main__':
    try:
        bot.start_serve()
    except KeyboardInterrupt:
        import sys
        sys.exit(1)
