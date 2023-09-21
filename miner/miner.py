import requests
import capmonster_python
from discord.utils import get
import discord
from .variables import *
from .commands import Commands
from threading import Thread
from time import sleep
import asyncio
from .utils import log
from threading import Thread


class Oxerator:
    def __init__(self, token_id):
        self.minerno = token_id
        self.client = discord.Client()
        self.started = False
        self.token = data['authorization'][str(self.minerno)]
        self.miner = Commands(self.token)
        self.MiningChannelID = data['channel'][str(self.minerno)]
        self.owners = [int(i) for i in (data['data']['owners']).split(',')]
        self.on_ready = self.client.event(self.on_ready)
        self.on_message = self.client.event(self.on_message)

    def start_bot(self):
        self.started = True
        while self.started:
            for i in data['commands']:
                self.miner.send(self.MiningChannelID, self.miner.owo(OwoPrefix, i),
                                start=int(first_time_interval), end=int(second_time_interval), bool=self.started)

    def run_bot(self):
        thread = Thread(target=self.start_bot)
        thread.start()

    async def on_ready(self):
        log(info=f'Logged on as {self.client.user}')

    async def on_message(self, message: discord.Message):
        self.SLchannel = await self.client.fetch_channel(SolverChannelAndLogs)
        self.SRole = get(self.client.get_guild(
            int(data['data']['server_id'])).roles, id=solvers)
        self.SChannel = await self.client.fetch_channel(SolverChannel)
        self.MiningChannel = await self.client.fetch_channel(self.MiningChannelID)

        if message.author == self.client.user:
            return

        if message.content.startswith(OwnerCmd) and message.author.id in self.owners:
            try:
                cmd = str(message.content).split(OwnerCmd)[-1].strip()
                if cmd:
                    await self.MiningChannel.send(cmd)
                    log(info="Sent `{}` to #{} from @{} by {}".format(
                        cmd, self.MiningChannel.name, self.client.user, message.author))
                else:
                    await message.channel.send("Specify message to send")
                    log(error="Please specify message to send | MINER: {} | USER: {}".format(
                        self.client.user, message.author))
            except Exception as e:
                log(error="CODE:2001 | Failed to send message due to `%s`" % e)

        if self.client.user.mention+" use" in message.content and message.author.id in self.owners:
            try:
                cont = self.client.user.mention + " use"
                cmd = str(message.content).split(cont)[-1].strip()
                if cmd:
                    await self.MiningChannel.send(cmd)
                    log(info="Sent `{}` to #{} from @{} by {}".format(
                        cmd, self.MiningChannel.name, self.client.user, message.author))
                else:
                    await message.channel.send("Specify message to send")
                    log(error="Please specify message to send | MINER: {} | USER: {}".format(
                        self.client.user, message.author))
            except Exception as e:
                log(error="CODE:2002 | Failed to send message due to `%s` | Info: `%s` used by @%s" %
                    (e, message.content, message.author))

        if SeparateDm + " " + self.client.user.mention in message.content and message.author.id in self.owners:
            try:
                cont = SeparateDm + " " + self.client.user.mention
                cmd = str(message.content).split(cont)[-1].strip()
                if cmd:
                    Owo = await self.client.fetch_user(795531508148207646)
                    await Owo.send(cmd)
                    log(info="Sent `{}` to {} from @{} by {}".format(
                        cmd, Owo, self.client.user, message.author))
                else:
                    await message.channel.send("Specify message to send")
                    log(error="Please specify message to send | MINER: {} | USER: {}".format(
                        self.client.user, message.author))
            except Exception as e:
                log(error="CODE:2003 | Failed to send message due to `%s` | Info: `%s` used by @%s" %
                    (e, message.content, message.author))

        if message.content == StartCmd and message.author.id in self.owners:
            log(info=f"Starting miner {self.client.user} | ID {self.minerno}")
            try:
                if not self.started:
                    self.run_bot()
                    log(info=f"Started miner {self.client.user} | ID {self.minerno}")
                    await message.channel.send(f"Started miner {self.client.user.mention}")
            except Exception as e:
                log(error="CODE:2004 | Failed to start miner %s due to `%s` | Info: `%s` used by @%s" %
                    (self.client.user, e, message.content, message.author))

        if SeparateStart + " " + self.client.user.mention in message.content and message.author.id in self.owners:
            log(info=f"Starting miner {self.client.user} | ID {self.minerno}")
            try:
                if not self.started:
                    self.run_bot()
                    log(info=f"Started miner {self.client.user} | ID {self.minerno}")
                    await message.channel.send(f"Started miner {self.client.user.mention}")
            except Exception as e:
                log(error="CODE:2005 | Failed to start miner %s due to `%s` | Info: `%s` used by @%s" %
                    (self.client.user, e, message.content, message.author))

        if message.content == StopCmd and message.author.id in self.owners:
            try:
                if self.started:
                    self.started = False
                    log(info=f"Stopped miner {self.client.user} | ID {self.minerno}")
                    await message.channel.send(f"Stopped miner {self.client.user.mention}")
            except Exception as e:
                log(error="CODE:2006 | Failed to stop miner %s due to `%s` | Info: `%s` used by @%s" %
                    (self.client.user, e, message.content, message.author))

        if SeparateStop + " " + self.client.user.mention in message.content and message.author.id in self.owners:
            try:
                if self.started:
                    self.started = False
                    log(info=f"Stopped miner {self.client.user} | ID {self.minerno}")
                await message.channel.send(f"Stopped miner {self.client.user.mention}")
            except Exception as e:
                log(error="CODE:2007 | Failed to stop miner %s due to `%s` | Info: `%s` used by @%s" %
                    (self.client.user, e, message.content, message.author))

        if message.guild is None:
            try:
                if Verification_link_captcha in message.content and message.author.id == owoid:
                    await self.SLchannel.send(f"Logs => Captcha Link Recognized \nCaptcha Link from Miner {str(self.minerno)} \n{self.miner.getme()} \nMessage > {message.content}")
                    await self.SChannel.send(content=f'<@&{solvers}> Please Solve!' + f" Link Captcha from Miner {str(self.minerno)} \n{message.content} ")
                    log(warning="CAPTCHA LINK RECOGNIZED | Miner {} | ID {} | Link {} \n".format(
                        self.client.user, self.minerno, message.content))
            except Exception as e:
                log(error="CODE:2008 | Error Occured: %s" % e)

        if message.guild is None:
            if DM_captcha_text in message.content and message.author.id == owoid:
                if len(message.attachments) > 0:
                    global url
                    url = message.attachments[0].url
                    r = requests.get(url)
                    with open("./captcha.png", "wb") as f:
                        f.write(r.content)
                    try:
                        reply = await message.channel.send(self.miner.solve(apikey))
                        log(warning="CAPTCHA SOLVED USING CAPMONSTER | Captcha code {} | Miner {} | ID {}".format(
                            reply.content, self.client.user, self.minerno))
                        await self.SLchannel.send(f"Logs= > Captcha Recognized \nCaptcha from Miner {str(self.minerno)} \n{self.miner.getme()} \nMessage > {message.content} \nResponse Code = > {reply.content} \nPlease Verify if the response code is exact as image letters! if not please manually solve it\n {url}")
                    except capmonster_python.utils.CapmonsterException as e:
                        await self.SChannel.send(f"<@&{solvers}>" + f"{message.content} in {message.channel} \nMiner {self.minerno}  \nPlease solve! Reply with the code as soon as possible!\n{url}")
                        log(warning="Please Manually Solve Captcha! | Miner {} | ID {} | Url {} | Solver channel #{}".format(
                            self.client.user, self.minerno, url, self.SChannel.name))

                        def check(m):
                            return m.channel == self.SChannel and m.author in self.SRole.members and self.client.user.mention in m.content
                        msg = await self.client.wait_for('message', check=check)
                        x = str(msg.content).replace(
                            self.client.user.mention, ' ')
                        reply = await message.channel.send(x)
                        await self.SChannel.send(f"```{reply.content}``` to {message.channel}")
                        log(
                            info=f"Sent code {reply.content} to {message.channel} | Solved by {msg.author}")
                        sleep(time_to_sleep_before_response)
                        responsed = self.miner.getresponse(message.channel.id)
                        await self.SChannel.send(f"RESPONSE : {responsed}")
                    except discord.errors.HTTPException:
                        pass
                    except Exception as e:
                        log(error="CODE:2009 | Error Occured in solving captcha | Message: %s | Error: %s" % (
                            message.content, e))

        if message.author.id == owoid and message.guild is None:
            if DM_warning1 in message.content and message.author.id == owoid:
                try:
                    reply = await message.channel.send(self.miner.solve(apikey))
                    await self.SLchannel.send(f" Logs => {DM_warning1} \nCaptcha from Miner {str(self.minerno)} \n {self.miner.getme()} \nMessage => {message.content} \nResponse code: {reply.content}\n {url}")
                    log(warning="CAPTCHA SOLVED USING CAPMONSTER | Captcha code {} | Miner {} | ID {}".format(
                        reply.content, self.client.user, self.minerno))
                except capmonster_python.utils.CapmonsterException as e:
                    await self.SChannel.send(f"<@&{solvers}> ```{message.content}``` in {message.channel} \nMiner {self.minerno}  \nPlease solve! Reply with the code as soon as possible!{url}")
                    log(warning="Please Manually Solve Captcha! | Miner {} | ID {} | Url {} | Solver channel #{}".format(
                        self.client.user, self.minerno, url, self.SChannel.name))

                    def check(m):
                        return m.channel == self.SChannel and m.author in self.SRole.members and self.client.user.mention in m.content
                    msg = await self.client.wait_for('message', check=check)
                    x = str(msg.content).replace(self.client.user.mention, ' ')
                    reply = await message.channel.send(x)
                    await self.SChannel.send(f"```{reply.content}``` to {message.channel}")
                    log(
                        info=f"Sent code {reply.content} to {message.channel} | Solved by {msg.author}")
                    sleep(time_to_sleep_before_response)
                    responsed = self.miner.getresponse(message.channel.id)
                    await self.SChannel.send(f"RESPONSE : {responsed}")
                except discord.errors.HTTPException:
                    pass
                except Exception as e:
                    log(error="CODE:2010 | Error Occured in solving captcha | Message: %s | Error: %s" % (
                        message.content, e))

            elif DM_warning2 in message.content and message.author.id == owoid:
                try:
                    reply = await message.channel.send(self.miner.solve(apikey))
                    log(warning="CAPTCHA SOLVED USING CAPMONSTER | Captcha code {} | Miner {} | ID {}".format(
                        reply.content, self.client.user, self.minerno))
                    await self.SLchannel.send(f" Logs= > {DM_warning2} \nCaptcha from Miner {str(self.minerno)} \n {self.miner.getme()} \nMessage = > {message.content} \nResponse code: {reply.content}\n {url}")
                except capmonster_python.utils.CapmonsterException as e:
                    await self.SChannel.send(f"<@&{solvers}> ```{message.content}``` in {message.channel} \nMiner {self.minerno}  \nPlease solve! Reply with the code as soon as possible!{url}")
                    log(warning="Please Manually Solve Captcha! | Miner {} | ID {} | Url {} | Solver channel #{}".format(
                        self.client.user, self.minerno, url, self.SChannel.name))

                    def check(m):
                        return m.channel == self.SChannel and m.author in self.SRole.members and self.client.user.mention in m.content
                    msg = await self.client.wait_for('message', check=check)
                    x = str(msg.content).replace(self.client.user.mention, ' ')
                    reply = await message.channel.send(x)
                    await self.SChannel.send(f"```{reply.content}``` to {message.channel}")
                    log(
                        info=f"Sent code {reply.content} to {message.channel} | Solved by {msg.author}")
                    sleep(time_to_sleep_before_response)
                    responsed = self.miner.getresponse(message.channel.id)
                    await self.SChannel.send(f"RESPONSE : {responsed}")
                except discord.errors.HTTPException:
                    pass
                except Exception as e:
                    log(error="CODE:2011 | Error Occured in solving captcha | Message: %s | Error: %s" % (
                        message.content, e))

            elif DM_warning3 in message.content and message.author.id == owoid:
                try:
                    await self.SLchannel.send(f" Logs => {DM_warning3} \nCaptcha from Miner {str(self.minerno)} \n {self.miner.getme()} \nMessage => {message.content} \n {url}")
                    await self.SChannel.send(content=f"<@&{solvers}> \nSolve Captcha {message.content} \n Please Entercode: <XXXXX> \n{url} ")
                    log(warning="Please Manually Solve Captcha! | Miner {} | ID {} | Url {} | Solver channel #{}".format(
                        self.client.user, self.minerno, url, self.SChannel.name))

                    def check(m):
                        return m.channel == self.SChannel and m.author in self.SRole.members and self.client.user.mention in m.content
                    msg = await self.client.wait_for('message', check=check)
                    x = str(msg.content).replace(self.client.user.mention, ' ')
                    reply = await message.channel.send(x)
                    await self.SChannel.send(f"```{reply.content}``` to {message.channel}")
                    log(
                        info=f"Sent code {reply.content} to {message.channel} | Solved by {msg.author}")
                    sleep(time_to_sleep_before_response)
                    responsed = self.miner.getresponse(message.channel.id)
                    await self.SChannel.send(f"RESPONSE : {responsed}")
                except Exception as e:
                    log(error="CODE:2012 | Error Occured in solving captcha | Message: %s | Error: %s" % (
                        message.content, e))

            elif verified_text in message.content and message.author.id == owoid:
                try:
                    log(info="Verified Successfully")
                    dchannel = self.client.get_channel(
                        SolvedCommandsMiningChannelID)
                    await dchannel.send('!unlock '+str(self.MiningChannelID) + ' miner-'+str(self.minerno))
                    await self.SLchannel.send("Verified Miner "+str(self.minerno) + "\n" + message.content)
                except Exception as e:
                    log(error="CODE:2013 | Error Occured in solving captcha | Message: %s | Error: %s" % (
                        message.content, e))

        if message.guild is not None and message.channel.id == self.MiningChannelID:
            if guild_captcha_text in message.content and message.author.id == owoid:
                if len(message.attachments) > 0:
                    self.attachment = message.attachments[0]
                    self.image = self.attachment.url
                    url1 = self.image
                    r = requests.get(url1)
                    with open("./captcha.png", "wb") as f:
                        f.write(r.content)
                    owodm = await self.fetch_user(owoid)
                    try:
                        reply = await owodm.send(self.miner.solve(apikey))
                        await self.SLchannel.send(f"Logs => Captcha Recognized \nCaptcha from Miner {str(self.minerno)} \n{self.miner.getme()} \nMessage > {message.content} \nResponse Code => {reply.content} \nPlease Verify if the response code is exact as image letters! if not please manually solve it \n{url1}")
                        log(warning="CAPTCHA SOLVED USING CAPMONSTER | Captcha code {} | Miner {} | ID {}".format(
                            reply.content, self.client.user, self.minerno))
                    except capmonster_python.utils.CapmonsterException as e:
                        await self.SChannel.send(f"<@&{solvers}>" + f"{message.content} in {message.channel} \nMiner {self.minerno}  \nPlease solve! Reply with the code as soon as possible!{url1}")
                        log(warning="Please Manually Solve Captcha! | Miner {} | ID {} | Url {} | Solver channel #{}".format(
                            self.client.user, self.minerno, url1, self.SChannel.name))

                        def check(m):
                            return m.channel == self.SChannel and m.author in self.SRole.members and self.client.user.mention in m.content
                        msg = await self.client.wait_for('message', check=check)
                        x = str(msg.content).replace(
                            self.client.user.mention, ' ')
                        reply = await owodm.send(x)
                        await self.SChannel.send(f"```{reply.content}``` to {message.channel}")
                        log(
                            info=f"Sent code {reply.content} to {message.channel} | Solved by {msg.author}")
                    except discord.errors.HTTPException:
                        pass
                    except Exception as e:
                        log(error="CODE:2014 | Error Occured in solving captcha | Message %s | Error: %s" % (
                            message.content, e))


class StartMiners():
    def __init__(self):
        self.loop = asyncio.new_event_loop()
        self.minernos = 0

    def start_client(self, ranges):
        asyncio.set_event_loop(self.loop)
        for i in list(range(0, 1+ranges)):
            self.loop.create_task(
                Oxerator(str(i)).client.start(Oxerator(str(i)).token))
        self.minernos += ranges

    def run_forever(self):
        if not self.loop.is_running():
            thread = Thread(target=self.loop.run_forever)
            thread.start()
            thread.join()
