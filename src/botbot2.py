from disco.bot import Bot, Plugin
import json, re

# start this by:
#    python -m disco.cli --token=<YOUR TOKEN> --run-bot --plugin botbot2

class SimplePlugin(Plugin):

    known_channels = []

    # Plugins provide an easy interface for listening to Discord events
    @Plugin.listen('ChannelCreate')
    def on_channel_create(self, event):
        channel_name = event.id
        if not (channel_name in known_channels):
            known_channels.push(channel_name)
            event.channel.send_message('Woah, a new channel huh! ' + str(channel_name))

    @Plugin.listen('MessageCreate')
    def on_message_create(self, event):
        #self.log.debug('Got message: %s', event.message)
        #self.log.info('Got message: %s', event.message.content)
        pattern = re.compile('hi[ ]*[!]*$',re.I)
        if pattern.match(event.message.content):
           #self.log.info('Got message: %s', event.message.content)
           event.channel.send_message('Yes? What do you want??')
        pattern2 = re.compile(':[-]*[\(\)\{\}]')
        #self.log.info('Got message: %s', event.message.content)
        if pattern2.match(event.message.content):
           event.channel.send_message('EMOJI ALARM!')
        pattern3 = re.compile('what[\']*[ i]*s the number?',re.I)
        if pattern3.match(event.message.content):
           event.channel.send_message('Which site would you like the number of?')


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

    @Plugin.command('give cookie')
    def on_give_cookie_command(self, event):
        event.msg.reply('Wow a cookie! Thank you!')

    @Plugin.command('echo', '<content:str...>')
    def on_echo_command(self, event, content):
        event.msg.reply(content)
