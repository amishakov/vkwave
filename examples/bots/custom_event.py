from vkwave.bots import SimpleBotEvent, SimpleLongPollBot, simple_bot_message_handler


class MyEvent(SimpleBotEvent):
    def my_custom_method(self):
        return 'It\'s custom method!'


bot = SimpleLongPollBot(
    tokens="",
    group_id=123,
    event=MyEvent
)


@bot.message_handler(bot.text_filter('my_event'))
async def handler(event: MyEvent):
    result = event.my_custom_method()
    return result


@simple_bot_message_handler(
    bot.router,
    bot.text_filter('my_event_router'),
    event=MyEvent
)
async def handler_from_router(event: MyEvent):
    result = event.my_custom_method()
    return result


bot.run_forever()
