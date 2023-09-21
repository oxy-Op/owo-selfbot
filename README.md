# Oxerator - Discord Owo Bot Automation Tool


**Oxerator** is a powerful automation tool designed to streamline your interactions with the Discord Owo Bot. It enables you to automate commands and mine items offered by Owo Bot, all with the goal of making your Discord experience more efficient.

## Why Oxerator?

Oxerator simplifies the process of automating Owo Bot commands and offers the following features:

- **Automatic Captcha Solver**: Effortlessly solve captchas using an integrated automatic solver.
- **Manual Captcha Solver**: In cases where automatic solving fails, you can manually solve captchas.
- **Captcha Logger**: Keep track of captcha solving attempts.
- **Logs Interface**: View logs directly within the application.
- **Custom Delay**: Define delays between commands to mimic human-like behavior.
- **Full Control**: Take complete control over your miners and their functions.

## How Does Oxerator Work?

Oxerator acts as a mediator between your Discord server and the Owo Bot. It commands miners to send requests to Owo Bot, automating actions based on your configurations.

## Running Oxerator on Your System

Oxerator runs on your local system, utilizing your system's resources. It acts as a bridge between the server and the web interface.

## Usage

1. `git clone https://github.com/oxy-Op/owo-selfbot.git`
2. `cd owo-selfbot`
3. `pip install -r requirements.txt`
4. `python app.py`
5. Open your browser and navigate to `http://127.0.0.1:5000`. You will be prompted for an API key (which is `oxy-Op`)
6. After logging in, you'll land on the miner webpage, where you can configure your miners.

## Configuring Oxerator

When you reach the miner webpage, you'll find several categories for configuration:

### Config
Configures Accounts, Channels, and Commands. Contains the following options:

- **Tokens**: Token Authorization of Discord accounts in a text file.
- **Channels**: Requires Discord Server Channel IDs.
- **Commands**: Owo Bot Commands.

### Authorization
Configures options relating to authorization. Contains the following options:

- **Miners to Start**: Type a number to specify how many miners you want to start (0 for 1 and so on, maximum 99).
- **Captcha Key**: Captcha API key provided by your vendor.
- **Owners**: Discord User IDs of owners. Owners have full access to miner commands.

### General
Configures General Information. Contains the following options:

- **Server ID**: Server ID of the mining server.
- **Solver Role ID**: Role ID of the solvers who manually solve captchas.
- **Log Channel ID**: Channel ID for sending logs.
- **Unlock Commands Channel ID**: Channel ID for sending unlock commands.
- **Manual Captcha Solving Channel ID**: Channel ID for users with solver roles to send commands for manual captcha solving.
- **Delay**: Define the delay range between sending messages.

### Commands Configuration
Configures In-Built Commands Information. Contains the following options:

- **Start command**: Define the in-built start command.
- **Stop command**: Define the in-built stop command.
- **Start command for single miner**: Define the in-built start command for a single miner.
- **Stop command for single miner**: Define the in-built stop command for a single miner.
- **Owo DM Command**: Define the in-built command to Direct Message OwO Bot.
- **Invoke Command**: Define the in-built command to use custom commands.

## In-Built Commands

The In-Built Commands section covers the most useful set of commands that allow you to command the miners, similar to how you interact with Discord bots.

- **Start:** To start miners on a Discord server, use the command configured in the Commands Configuration section in any text channel. Your Discord user ID must be in the Owners list to use this command. For example: `start`

- **Start Specific Miner:** To start any specific miner, use the command configured in the Commands Configuration section in any text channel. Your Discord user ID must be in the Owners list to use this command. Argument: `start <@userid>`. For example: `startseparate`

- **Stop Miner:** To stop miners, use the command configured in the Commands Configuration section in any text channel. Your Discord user ID must be in the Owners list to use this command. For example: `stop`

- **Stop Specific Miner:** To stop any running miner, use the command configured in the Commands Configuration section in any text channel. Your Discord user ID must be in the Owners list to use this command. Argument: `stop <@userid>`. For example: `stopseparate`

- **Invoke:** One of the most useful commands, `invoke` allows you to send any message from miners to their respective channels. Argument: `>invoke (or your custom command) <message>`. Usage: `>invoke owo give <@userid>`, `>invoke cookie <@userid>`

- **Separate Invoke:** Just like `Invoke`, `separate invoke` allows you to send any message from a specific miner to their specific channel. Argument: `<@minerid> <message>`. Usage: `<@minerid> owo give <@userid>`, `<@minerid> cookie <@userid>`

- **Dm uwu:** `DM uwu` command allows you to direct message owo in case of a failed captcha solve. Argument: `>dmuwu (or custom command) <message>`. Usage: `<@minerid> owo give <@userid>`, `<@minerid> cookie <@userid>`

- **Manual Captcha Solver:** Whenever captcha is recognized, it will be sent to the specified Manual Captcha Solver Channel. Users who have been assigned the @solvers role can use commands to solve captcha manually. Argument: `<@mineruserid> <code>`. For more information about how captchas are solved, please refer to "How are captchas solved?" below.

### How are captchas solved?

Captchas are solved in two ways:

- **Automatic:** Whenever captchas are identified by the program, a cloud API service (currently: capmonster) is used to solve captchas automatically. In order to use it, you must provide a captcha key. Note: Sometimes captcha solving services fail, so owo allows three attempts to solve captcha if the auto-captcha solver fails to solve it twice. After that, manual solving is required.

- **Manual:** If the captcha key is not provided or doesn't have enough balance, manual captcha solving comes into action. You will be notified by a message whenever a captcha is recognized by [Miners]. It will be sent to the Manual Captcha Solving Channel for you to access it. The message will contain information about Miner Name, ID, and Captcha Image. You have to identify the captcha code and send the following message in the same channel: `<@miner> <code>`. You are allowed three chances to solve the captcha; if all three captcha codes are incorrect, you will be banned for macro-botting for 10 minutes (if it's the first time). Each time you solve a captcha, you will be notified if it's correct or incorrect.

## Disclaimer

Please use Oxerator responsibly and in compliance with Discord's Terms of Service. Respect Discord's rules and guidelines when automating actions with this tool. Note that automating Owo Bot is against Discord's Terms of Service, and Oxerator is intended for educational purposes only.

## Precautions

To avoid detection and issues with Owo Bot, consider the following precautions:

- Do not mine continuously for extended periods.
- Use long intervals between each command.
- Be cautious with solving captchas very quickly.
- Do not invite suspicious individuals to your mining server.
- Avoid transferring items to your main account directly.

## Recommendations

Here are some recommendations:

- Create a separate server for mining.
- Use long durations between each command (e.g., 5-12 seconds).
- Consider using powerful servers to handle resource-intensive tasks when running multiple accounts.

---

© 2023 Oxerator. All rights reserved. Unauthorized copying or use of our content without permission is not allowed.

This tool is created for educational purposes only, to understand how programs can interact with resources. Use it at your own risk; we are not responsible for any loss or misuse.
