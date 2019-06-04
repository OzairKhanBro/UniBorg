import sys
from telethon import events, functions, __version__
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="helpme ?(.*)", allow_sudo=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    splugin_name = event.pattern_match.group(1)
    if splugin_name in borg._plugins:
        s_help_string = borg._plugins[splugin_name].__doc__
    else:
        s_help_string = ""
    help_string = """
Python {}
Telethon {}
message=commands available in @UniBorg 🌝
👉 `.unload <PLUGIN NAME>` Remove plugin from running
👉 `.load <PLUGIN NAME>` Reload plugin into the UserBot
👉 `.send plugin <Plugin Name>`
👉 `.install plugin` As reply to any valid @UniBorg plugin
👉 `.afk [Optional Reason]` Marks yourself as Away From Keyboard
👉 `.calendar 2019-03-04` returns the Malayalam calendar for the date specified
👉 `@admin` Call ADMINs in the current chat
👉 `.kangsticker [Optional Emoji]` Reply to a sticker to add it your personal Telegram sticker pack
👉 `.getsticker` Uploads the sticker pack as an archive file
👉 `.packinfo` Check the sticker pack info of the replied sticker
👉 `.lock <type>` Lock the given type in the current chat
👉 `.unlock <type>` Unlocks the given type in the current chat
👉 `.dblocks` Check the active locks in the current chat
👉 `.coinflip [Optional Choice]` Flips a coin and tells whether Heads or Tails
👉 `.count` Counts the Numbe rof Dialogs you have in your Telegram
👉 `.color <Color Code>` Sends the Color to the current chat
👉 `.currency 1 USD INR` Gets the current currency conversion rate
👉 `.dns HOST` Get Domain Naming System Records of a Host on the Internet
👉 `.url http://example.com` Shorten a long URL to a short URL
👉 `.decide` Get Yes or No decisions, at any time in any chat
👉 `.download` Reply to a Telegram media to download to local UserBot server
👉 `.emoji` Four emoji animations (Read The Code to know how to use these)
👉 `.eval` <Python Code>
👉 `.exec` <BASH command>
👉 `.filext <extension>` Get information about an extension
👉 `.fwd` Get view counter on any post. Credits: @ManueI15
👉 `!!gban [Optional Reason]` Globally Ban an user from the entire network of Group Administration bots managed by you
👉 `.get_admin [Optional Argument]` Gets Administrators in a Channel
👉 `.get_bot [Optional Argument]` Gets Bots in a Channel
👉 `.get_id` Get ID of a Telegram chat
👉 `.github <username>` Get info about a GitHub user
👉 `.google search <Search Query>`
👉 `.google image <Search Query>`""".format(
        sys.version,
        __version__
    )

    
message2="""👉 `.google reverse search` As a reply to an image
👉 `.dc`
👉 `.config` <won't tell What this does>
👉 `.helpme` no one gonna help you 🤣🤣🤣🤣
👉 `.ifsc rp <IFSC CODE>` Get information about a bank knowing it's IFSC code
👉 `.json` Get Telegram metadata of any message
👉 `.ocrlanguages` Get available language codes in ocr.space API
👉 `.ocr <LangCode>` Convert Image to Text using ocr.space API
👉 `.weather <Location>` Gets the weather of a specified Location
👉 `.paste <Optional Argument>`
👉 `.cpin` Pins a message in a channel
👉 `.ping`
👉 `.get_poll` Displays the replied Poll as text
👉 `.promote <Optional ID>`
👉 `.purge [Optional "me"]` Reply to a message to clear all message starting from the replied message
👉 `.makeqr [Optional Argument]`
👉 `.getqr` Gets the information contained in a Quick Response image
👉 `.sca [Optional Argument]` Sends the relevant Chat Action to the target chat.
👉 `.schd <time_in_seconds> ;=; <message to send>`
👉 `.screencapture URL`
👉 `.speedtest`
👉 `.stt <Lang Code>` Convert Speech To Text
👉 `.tagall` @tagall in the target chat
👉 `.telegraph <Positional Argument>`
👉 `.getime [Optional Argument]` Displays the current system time
👉 `.torrentz <Search Engine To Use> <Search Query>` Searches the Torrent Search Engine for Search Query
👉 `.torrent <INFO HASH>` Converts the Info Hash to Magnetic Link and Torrent File
👉 `.tr <Lang Code>` Google Translate
👉 `.tts <Lang Code>` Google Text to Speech
👉 `.unbanall` Removes all user Restrictions in the current channel
👉 `.kick <Optional Argument>` @ukinti\_bot PRO Feature
👉`.(ban|unban|mute) [Optional ID]`
👉 `.savethumbnail`
👉 `.clearthumbnail`
👉 `.getthumbnail`
👉 `.uploadasstream <Path to File>`
👉 `.uploadasvn <Path to File>`
👉 `.upload <Path to File>`
👉 `.uploadir <Path to Directory>`
👉 `.ud <Word>` Checks word in UrbanDictionary.com
👉 `.meaning <Word>` Checks meaning of word with pronounciation
👉 `.whois [Optional ID]` 
👉 `.wikimedia <Search Query>`
👉 `.wikipedia <Search Query>`
👉 `.savewelcome <Welcome Message>`
👉 `.clearwelcome`
👉 `.pbio <Your Telegram About>`
👉 `.pname <First Name> \n [Last Name]`
👉 `.ppic`
👉 `.create <b|g> <Group Name>`
😞 I do not know what the below commands do / How to write it here 🤦‍♀️
markdown
antiflood
SED
snips
filters
xtools"""
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER  # pylint:disable=E0602
    if tgbotusername is not None:
        results = await borg.inline_query(  # pylint:disable=E0602
            tgbotusername,
            help_string + "\n\n" + s_help_string
        )
        await results[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
        await event.delete()
    else:
        await event.reply(help_string)
        await event.reply(message2)
        await event.reply(s_help_string)
        await event.delete()


@borg.on(admin_cmd(pattern="dc"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await event.edit(result.stringify())


@borg.on(admin_cmd(pattern="config"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.edit("""Telethon UserBot powered by @UniBorg""")
