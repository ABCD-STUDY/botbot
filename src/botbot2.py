from disco.bot import Bot, Plugin
import json

# start this by:
#    python -m disco.cli --token=<YOUR TOKEN> --run-bot --plugin botbot2

class SimplePlugin(Plugin):
    # Plugins provide an easy interface for listening to Discord events
    @Plugin.listen('ChannelCreate')
    def on_channel_create(self, event):
        channel_name = ""

        event.channel.send_message('Woah, a new channel huh! ' + json.dumps(list(event)))

    # Serious Commands
    @Plugin.command('number')
    def on_number_command(self, event):
        event.msg.reply('There are currently 00000 participants.')

    @Plugin.command('percentage')
    def on_percentage_command(self, event):
        event.msg.reply('The number of participants is 0\% of the target number')

    @Plugin.command('time')
    def on_time_command(self, event):
        event.msg.reply('It will take approximately 000 days to reach the target number. \nThis is on mm/dd/yyyy.')
    
    # Fun Extras
    @Plugin.command('ping')
    def on_ping_command(self, event):
        event.msg.reply('Pong!')

    @Plugin.command('good bot')
    def on_good_bot_command(self, event):
        event.msg.reply('Thank you! Glad to help!')

    @Plugin.command('give_cookie')
    def on_give_cookie_command(self, event):
        event.msg.reply('Wow a cookie! Thank you!')

    @Plugin.command('echo', '<content:str...>')
    def on_echo_command(self, event, content):
        event.msg.reply(content)
