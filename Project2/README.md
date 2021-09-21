# Project 2

## Setup

Steps to setup the project:

1. Get a Discord Bot API Token

    1. Sign up for a Discord account at [Discord.com](https://discord.com)
    2. Go to Applications section of the [developer portal](https://discord.com/developers/applications).
    3. Click the "New Application" button in the top-right and give it a name.
    4. Click on your application and go to Bot settings and click "Add Bot".
    5. Give your bot a name
    6. Click the button to copy the bot token, you'll need this in the next step
    7. To add your button to a server/guild, click Oauth2 and select "bot" for scope and "Administrator" for bot permissions. Paste the generated link into your browser and follow the steps to add the bot to a Discord server/guild.

2. Install the project

    1. Clone the repo to your machine
    2. Make sure python3 and pip are installed, the instructions differ by OS, if you're unsure check [python.org](https://python.org).
    3. Install the following dependencies: discord.py, python-dotenv (note you may need to use `pip3` instead of `pip`).

        1. `pip install -U discord.py`
        2. `pip install -U python-dotenv`

    4. Make a file named .env
    5. In your .env file paste the following line `DISCORD_TOKEN=token` where token is the token you copied from the Discord developer bot page in step 1.6.
    6. Run the command `python bot.py` (on some systems you may need to type `python3` in place of `python`)

## Usage

The changes I made to this project were to add a command that displays a random Rick and Morty quote to the Discord server.

Discord commands:

* `towel!` Displays a random Hitchhiker's Guide to the Galaxy quote.
* `!pickle` Displays a random Rick and Morty quote.

## Run the bot 24/7

Assuming you have access to a machine or cloud VM that's always on, you can clone your project there and run it there with `python bot.py &`. Adding the ampersand makes the process continue running in the background, although on some systems this will close when the terminal is closed.

If you want the process to persist even when you close your terminal, you can do the following:

1. `chmod +x bot.py`
2. `nohup python bot.py &`

There is no (easy) way to bring this back to the foreground on most systems, you can however exit the task.
If you wish to kill the task without restarting your system you can do the following

1. Find the PID with `ps ax | grep bot.py`
2. Kill the process with `kill pid` where PID you found with the command above.

Both of these methods are fairly straightforward and are built into most Linux distros.
