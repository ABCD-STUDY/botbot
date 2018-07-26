from disco.bot import Bot, Plugin
import json, re
from datetime import datetime, timedelta

# start this by:
#    python -m disco.cli --token=<YOUR TOKEN> --run-bot --plugin botbot2

class SimplePlugin(Plugin):

    known_channels = []
    site_numbers = []

    # Plugins provide an easy interface for listening to Discord events
    @Plugin.listen('ChannelCreate')
    def on_channel_create(self, event):
        channel_name = event.id
        if not (channel_name in self.known_channels):
            self.known_channels.append(channel_name)
            event.channel.send_message('Woah, a new channel huh! ' + str(channel_name))

    @Plugin.listen('MessageCreate')
    def on_message_create(self, event):
        authorid = str(event.message.author)
        author,_ = str(event.message.author).split('#')
        #self.log.debug('Got message: %s', event.message)
        #self.log.info('Got message: %s', event.message.content)
        pattern = re.compile('hi[ ]*[!]*$',re.I)
        if pattern.match(event.message.content):
           #self.log.info('Got message: %s', event.message.content)
           event.channel.send_message('Hello ' + author + ', what can I do for you?')

        pattern2 = re.compile(':[-]*[\(\)\{\}]')
        #self.log.info('Got message: %s', event.message.content)
        if pattern2.match(event.message.content):
           event.channel.send_message('EMOJI ALARM!')

        got_new_request = False
        pattern3 = re.compile('what[\']*[ i]*s the number?',re.I)
        if pattern3.match(event.message.content):
           event.channel.send_message('Hi ' + author + ', which site would you like the number of?')
           self.site_numbers.append( [author, datetime.now() ] )
           got_new_request = True
           #event.channel.send_message(json.dumps(self.site_numbers))
        current_date = datetime.now()
        current_author = author
        # loop through the list of site_numbers
        if not got_new_request:
            surviving_requests = []
            for request in self.site_numbers:
                #   calculate the time difference in seconds between current date and site_numbers date (see datetime.timedelta)
                old_date = request[1]
                old_author = request[0]
                difference = (current_date - old_date).total_seconds()
                #   define short_enough (10sec)
                short_enough = 10
                keep = True

                if (current_author == old_author) and (difference <= short_enough):
                    event.channel.send_message("[site name] currently has 00000 participants. \"" + str(difference) + "\"")
                    keep = False
                if (current_author == old_author) and (difference > short_enough):
                    event.channel.send_message("Sorry, I didn't get a response in time. Please try again. \"" + str(difference) + "\"")
                    keep = False
                if keep:
                    surviving_requests.append(request)

            self.site_numbers = surviving_requests

        
            #   if the author of the current message is the same as the current author
            #      and if the time difference between old message and new is short enough
            #          print result
            #          remove message from site_numbers


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
