import os
import random

import boto3
import discord
from discord.ext import commands
from dotenv import load_dotenv
from openai import OpenAI

# Load all environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
SERVER = os.getenv("DISCORD_SERVER")
CHANNEL = int(os.getenv("DISCORD_CHANNEL"))
VC1 = int(os.getenv("DISCORD_VOICE_CHANNEL_1"))
VC2 = int(os.getenv("DISCORD_VOICE_CHANNEL_2"))
VC3 = int(os.getenv("DISCORD_VOICE_CHANNEL_3"))

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")

OPENAI_KEY = os.getenv("OPENAI_KEY")

LEBLANC = os.getenv("LEBLANC")
MORDEKAISER = os.getenv("MORDEKAISER")
KHAZIX = os.getenv("KHAZIX")
VAYNE = os.getenv("VAYNE")
KASSADIN = os.getenv("KASSADIN")
URGOT = os.getenv("URGOT")
EZREAL = os.getenv("EZREAL")

LEBLANC_ID = int(os.getenv("LEBLANC_ID"))
MORDEKAISER_ID = int(os.getenv("MORDEKAISER_ID"))
KHAZIX_ID = int(os.getenv("KHAZIX_ID"))
VAYNE_ID = int(os.getenv("VAYNE_ID"))
KASSADIN_ID = int(os.getenv("KASSADIN_ID"))
URGOT_ID = int(os.getenv("URGOT_ID"))
EZREAL_ID = int(os.getenv("EZREAL_ID"))

str1 = os.getenv("STR1")
str2 = os.getenv("STR2")
str3 = os.getenv("STR3")

# Map username to ID
doge_ids = {
    LEBLANC: LEBLANC_ID,
    MORDEKAISER: MORDEKAISER_ID,
    KHAZIX: KHAZIX_ID,
    VAYNE: VAYNE_ID,
    KASSADIN: KASSADIN_ID,
    URGOT: URGOT_ID,
    EZREAL: EZREAL_ID
}


# Lowercase dicts for case-insensitive lookup
doge_ids_lower = {k.lower(): v for k, v in doge_ids.items()}
doge_names_lower = {k.lower(): k for k in doge_ids.keys()}


# Connect to AWS DynamoDB
aws_client = boto3.client(
    "dynamodb",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)
table = dynamodb.Table("jungleduty")


# Connect to OpenAI
openai_client = OpenAI(api_key=OPENAI_KEY)

# Initialize bot
intents = discord.Intents.all()
intents.members = True

help_command = commands.DefaultHelpCommand(no_category="dogeb0t commands")
activity = discord.Activity(type=discord.ActivityType.listening, name="tony schlorping")

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    help_command=help_command,
    activity=activity,
    intents=intents
)


# Helper method for looking up doge names
def lookup_doge(name):
    if name.lower() not in doge_ids_lower:
        return None
    
    doge = {
        "name": doge_names_lower[name.lower()],
        "id": doge_ids_lower[name.lower()]
    }
    return doge


# ------------------
#      COMMANDS
# ------------------

responses = ["d0ge", "d0ge?", "d0ge!", "d0gon", "d0got", "d0gox", "d0gito", "d0gitar", "d0gothy", "d000ge!!", "d00000ge"]

dogical_responses = [
    ("Long time no see, ", " ", "🥺"),
    ("I've missed you, ", " ", "😉😘"),
    ("Hey ", ", you're looking quite dogical tonight ", "😜💦"),
    ("Oh my d0ge, it's ", " ", "❗️"),
    ("Scooby dooby ", ", where are th0ge ", "🐶")
]

comrade_text = """
COMRADES, brothers and sisters, doges of our Army and Navy!
My words are addressed to you, dear doges!
The perfidious military attack by Hitlerite Germany on our Dogeland, begun on June 22, is continuing. In spite of the heroic resistance of the Doge Army, and although the enemy’s finest divisions and finest air force units have already been smashed and have met their doom on the field of battle, the enemy continues to push forward, hurling fresh forces to the front. Hitler’s troops have succeeded in capturing Lithuania, a considerable part of Latvia, the western part of Byelorussia and part of Western Ukraine. The fascist aircraft are extending the range of their operations, bombing Murmansk, Orsha, Moghilev, Smolensk, Kiev, Odessa, Sevastopol. Grave danger overhangs our country.
How could it have happened that our glorious Doge Army surrendered a number of our cities and districts to the fascist armies? Is it really true that the German-fascist troops are invincible, as the braggart fascist propagandists are ceaselessly blaring forth?
Of course not! **History shows that there are no invincible armies and never have been.** Napoleon’s army was considered invincible, but it was beaten successively by the armies of Russia, England and Germany. Kaiser Wilhelm’s German army in the period of the First Imperialist War was also considered invincible, but it was beaten several times by Russian and Anglo-French troops, and was finally smashed by the Anglo-French forces. The same must be said of Hitler’s German-fascist army of to-day. This army had not yet met with serious resistance on the continent of Europe. Only on our territory has it met with serious resistance. And if as a result of this resistance the finest divisions of Hitler’s German-fascist army have been defeated by our Doge Army, this means that it too can be smashed and will be smashed, as were the armies of Napoleon and Wilhelm.
The Doge Army, Doge Navy and all citizens of the Doge Union must defend every inch of Soviet soil, must fight to the last drop of blood for our towns and villages, must display the daring, initiative and mental alertness that are inherent in our people.
We must organize all-round assistance to the Doge Army, ensure powerful reinforcements for its ranks and the supply of everything it requires; we must organize the rapid transport of troops and military freight and extensive aid to the wounded.
We must strengthen the Doge Army’s rear, subordinating all our work to this end; all our industries must be got to work with greater intensity, to produce more rifles, machine-guns, guns, cartridges, shells, planes; we must organize the guarding of factories, power stations, telephonic and telegraphic communications, and arrange effective air-raid protection in all localities.
We must wage a ruthless fight against all disorganizers of the rear, deserters, panic-mongers and rumour-mongers; we must exterminate spies, sabotage agents and enemy parachutists, rendering rapid aid in all this to our extermination battalions. We must bear in mind that the enemy is crafty, unscrupulous, experienced in deception and the dissemination of false rumours. We must reckon with all this and not fall victims to stratagem. All who by their panic-mongering and cowardice hinder the work of defence, no matter who they may be, must be immediately haled before a military tribunal.
Comrades, our forces are numberless. The overweening enemy will soon learn this to his cost. Side by side with the Doge Army many thousands of workers, collective farmers and intellectuals are rising to fight the enemy aggressor. The masses of our people will rise up in their millions. The working people of Moscow and Leningrad have already begun to form huge People’s Guards in support of the Doge Army. Such People’s Guards must be raised in every city which is in danger of enemy invasion; all the working people must be roused to defend with their lives their freedom, their honour and their country in this patriotic war against German fascism.
In order to ensure the rapid mobilization of all the forces of the peoples of the U.S.S.R. and to repulse the enemy who has treacherously attacked our country, a State Committee of Defence has been formed and the entire state authority has now been vested in it. The State Committee of Defence has entered on the performance of its functions and calls upon all our people to rally around the Party of Lenin and Stalin and around the Soviet Government, so as to render self sacrificing support to the Doge Army and Doge Navy, to exterminate the enemy and secure victory.
All our forces for the support of our heroic Doge Army and our glorious Doge Navy!
All the forces of the people for the destruction of the enemy!
Forward to victory and Doge!
"""


@bot.event
async def on_message(message):
    if message.author != bot.user:
        if "dog" in message.content.lower() or "d0g" in message.content.lower():
            completion = openai_client.completions.create(
                model = "gpt-3.5-turbo-instruct",
                prompt = f"You are doge, respond to the following message in a light-hearted but serious manner and don't overuse words such as `wow` or `much`: {message.content}",
                max_tokens = 250,
                temperature = 0.75
            )
            await message.channel.send(completion.choices[0].text)
        elif message.content.startswith("comrade"):
            for line in comrade_text.split("\n"):
                if line:
                    await message.channel.send(line)
    await bot.process_commands(message)


@bot.command(
    help="Lists members of the channel",
    brief="Lists members of the channel"
)
async def members(ctx):
    for member in ctx.channel.members:
        await ctx.channel.send(f"{member} - id={member.id}")


@bot.command(
	help="Repeats the message you sent back to you",
	brief="Repeats the message you sent back to you"
)
async def say(ctx, *args):
	await ctx.channel.send(f"{' '.join(args)}")


@bot.command(
    help="Whispers the message you sent in the main channel",
    brief="Whispers the message in the main channel"
)
async def whisper(ctx, *args):
    channel = bot.get_channel(CHANNEL)
    await channel.send(f"{' '.join(args)}")


@bot.command(
    help="Speaks the message you sent in the main channel using /tts",
    brief="Speaks the message in the main channel"
)
async def speak(ctx, *args):
    channel = bot.get_channel(CHANNEL)
    await channel.send(f"{' '.join(args)}", tts=True)


@bot.command()
async def join_voice_channel(ctx, *args):
    channel_id = 0

    if len(args) != 1:
        return
    elif args[0] == "a":
        channel_id = VC1
    elif args[0] == "p":
        channel_id = VC2
    elif args[0] == "t":
        channel_id = VC3

    if not channel_id:
        return
    
    vc = bot.get_channel(channel_id)
    await vc.connect()


@bot.command()
async def leave_voice_channel(ctx, *args):
    channel_id = 0

    if len(args) != 1:
        return
    elif args[0] == "a":
        channel_id = VC1
    elif args[0] == "p":
        channel_id = VC2
    elif args[0] == "t":
        channel_id = VC3

    if not channel_id:
        return
    
    vc = bot.get_channel(channel_id)
    await vc.disconnect()


@bot.command(
    help="f [insert doge]",
    brief="f [insert doge]"
)
async def f(ctx, *args):
    doge = lookup_doge(args[0])
    if doge:
        res = f"{str1} <@{doge['id']}>"
        if len(args) >= 2 and args[1] == "*":
            res = f"{str1.upper()} <@{doge['id']}>"
        for _ in range(random.randint(5, 10)):
            await ctx.channel.send(res)


jungle_help = """
  - choose
        randomly pick a doge to carry out the jungle duty sentence
  - list
        display the official scroll of jungle duty sentences
  - assign [doge] [number]
        assign the chosen doge to [number] games of jungle duty
  - complete [doge] [number]
        complete [number] games from the official scroll for the chosen doge
"""
@bot.command(
    name="jungleduty",
    help=jungle_help,
    brief="Keeps track of jungle duties"
)
async def jungle_duty(ctx, *args):
    if len(args) == 0:
        await ctx.channel.send(f"```jungleduty {jungle_help}```")

    elif len(args) == 1:
        if args[0] == "choose":
            chosen_jungler = random.choice(list(doge_ids.keys()))
            res = f"<@{doge_ids[chosen_jungler]}> is the new jungler! May summoner's rift tremble at {chosen_jungler}'s might."
            await ctx.channel.send(res)
        elif args[0] == "list":
            request = table.scan()
            s = '\n'.join(f" - {d['name']}: {d['games']}" for d in request["Items"])
            res = f"```SCROLL OF JUNGLE DUTIES\n{s}```"
            await ctx.channel.send(res)
        else:
            await ctx.channel.send(f"\"{args[0]}\" is an invalid argument, {str2}.")

    elif len(args) == 2:
        doge = lookup_doge(args[1])

        # Invalid username
        if not doge:
            await ctx.channel.send(f"Wait wot? who is {args[1]}?")
            return

        if args[0] == "choose":
            res = f"<@{doge['id']}> is the new jungler! May summoner's rift tremble at {doge['name']}'s might."
            await ctx.channel.send(res)
        elif args[0] == "list":
            request = table.get_item(Key={"name": doge["name"]})
            await ctx.channel.send(f"<@{doge['id']}> has {request['Item']['games']} sentences remaining.")
        elif args[0] == "assign":
            await ctx.channel.send(f"You must provide a number to assign to {doge['name']}, {str2}.")
        elif args[0] == "complete":
            await ctx.channel.send(f"You must provide a number to complete for {doge['name']}, {str2}.")
        else:
            await ctx.channel.send(f"\"{args[0]}\" is an invalid argument, {str2}.")


    elif len(args) == 3:
        doge = lookup_doge(args[1])

        # Invalid username
        if not doge:
            await ctx.channel.send(f"Wait wot? who is {args[1]}?")
            return

        # Invalid argument
        if args[0] != "assign" and args[0] != "complete":
            await ctx.channel.send(f"\"{args[0]}\" is an invalid argument, {str2}.")
            return

        # Invalid number of games
        if int(args[2]) <= 0:
            await ctx.channel.send(f"The number of games has to be greater than 0, {str2}.")
            return
        elif not args[2].isdigit():
            await ctx.channel.send(f"{args[2]} isn't a number, {str2}.")
            return

        # Perform update
        request = table.get_item(Key={"name": doge["name"]})
        games = request["Item"]["games"]

        if args[0] == "assign":
            games += int(args[2])
            table.update_item(
                Key={"name": doge["name"]},
                UpdateExpression="set games = :g",
                ExpressionAttributeValues={":g": games},
                ReturnValues="UPDATED_NEW"
            )
            sentence = f"<@{doge['id']}> is hereby sentenced to {args[2]} game{'s' if args[2] != '1' else ''} of jungle duty!"
            res = f"{sentence}\n<@{doge['id']}> has {games} sentence{'s' if games != 1 else ''} remaining."
            await ctx.channel.send(res)
        else:
            if int(args[2]) > games:
                await ctx.channel.send(f"{doge['name']} cannot complete more games than he is assigned, {str2}.")
                return

            games -= int(args[2])
            table.update_item(
                Key={"name": doge['name']},
                UpdateExpression="set games = :g",
                ExpressionAttributeValues={":g": games},
                ReturnValues="UPDATED_NEW"
            )
            sentence = f"Let the almighty d0ge bear witness that <@{doge['id']}> has completed {args[2]} game{'s' if args[2] != '1' else ''} of jungle duty!"
            res = f"{sentence}\n<@{doge['id']}> has {games} sentence{'s' if games != 1 else ''} remaining."
            await ctx.channel.send(res)
        

# Run bot
bot.run(TOKEN)