
# # Movie Bot

Movie Bot is a Telegram Bot designed to help you find movies quickly and easily. It allows you to search for movies by name, and provides you with links to download them.

## Features

Movie Bot has a variety of features to help you find the perfect movie for you: 

- **Search**: Easily search for movies by name.
- **Download**: Download movies directly from the bot.
- **Validity**: Set a validity period for the movies you download, so that you can always keep them up to date.
- **Auto-Delete**: Automatically delete movies after a set amount of time to keep your downloads organized.
- **Shortener**: Shorten long download links for easy sharing.
- **Help**: Get help from the bot with instructions on how to use it.

## Commands
```
/start - Used to start the bot.
/help - get help regarding the bot.
/about - get information about the bot.
/fsub - check the status of fsub in a group.
/set_fsub - set the force sub channel in a group. 
/index - set a channel to index in a group.
/auto_delete - check the status of auto delete in a group.
/set_auto_delete - set the auto delete time in a group.
/request - request access from the bot owner.
/info - get information about a group.
/set_api - set the API in a group.
/api - get the API from a group.
/remove_api - remove the API from a group.
```
## Setup

To get started, you'll need to set up some environment variables. These can be found in the following file:

Mandatory environment

 - `BOT_USERNAME`
 - `API_ID`
 - `API_HASH`
 - `BOT_TOKEN`
 - `DATABASE_URL`
 - `OWNER_ID`
 - `LOG_CHANNEL`
 - `DATABASE_CHANNEL`
 - `SESSION_STRING`
 - `VALIDITY`

Optional environment

 - `DATABASE_NAME`
 - `UPDATE_CHANNEL`
 - `ADMINS`
 - `BROADCAST_AS_COPY`
 - `WEB_SERVER`
 - `USERNAME`
 - `AUTO_DELETE`
 - `AUTO_DELETE_TIME`
 - `SHORTENER_API`
 - `SHORTENER_SITE`
 - `FILE_HOW_TO_DOWNLOAD_LINK`
 - `RESULTS_HOW_TO_DOWNLOAD_LINK`
 - `REQUEST_MOVIE_URL`


Once these environment variables are set, you can start using Movie Bot.

## Usage

To use Movie Bot, simply type in the name of the movie you're looking for and the bot will search for it. It will provide you with links to download the movie, and you can also use the Shortener feature to shorten long download links.

You can also use the bot to set a validity