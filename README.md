# AUV-BUZZ-MUSIC
[![AUV logo](https://telegra.ph/file/d74e196d579e35ed1976c.jpg)](https://t.me/auvbuzzbot)


Ini adalah bot obrolan suara. Untuk memutar lagu disaat OS dimulai
Dibuat Oleh Ridwansy

## Requirements

- FFmpeg
- NodeJS [nodesource.com](https://nodesource.com/)
- Python 3.7+
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)

## Deployment

### Config

Copy `example.env` to `.env` and fill it with your credentials.

### Without Docker

1. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```

### Using Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```
## Cara mudah untuk deploy Bot ini
### HEROKU
<a href="https://heroku.com/deploy?template=https://github.com/justteen/auvbuzzbotNEW"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-red?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>

### StringSession

[![GenerateString](https://img.shields.io/badge/repl.it-generateString-yellowgreen)](https://replit.com/@justteen/String-Session) 


### Mandatory Vars.

- Some Of The Mandatory Vars Are :-
   - `API_ID` :  Give API_ID of your Alternate Telegram Account. also get from here [@APIInfoBot](https://t.me/APIinfoBot)
   - `API_HASH` :  Give API_HASH of your Alternate Telegram Account. also get from here [@APIInfoBot](https://t.me/APIinfoBot)
   - `STRING_NAME` :  Make a string session from [here](https://replit.com/@QueenArzoo/VCPlayBot)
   - `BOT_TOKEN` :  Make a Bot from [@Botfather](https://t.me/botfather) and fill it's bot token.
   - `SUDO_USERS` :  Fill Userid of yhe users whom you want to be able to control the bot. You can add multiple id by giving a space in b/w each id.


### Commands 🛠
#### For all in group
- `/play <song name>` - play song you requested
- `/dplay <song name>` - play song you requested via deezer
- `/splay <song name>` - play song you requested via jio saavn
- `/playlist` - Show now playing list
- `/current` - Show now playing
- `/song <song name>` - download songs you want quickly
- `/search <query>` - search videos on youtube with details
- `/deezer <song name>` - download songs you want quickly via deezer
- `/saavn <song name>` - download songs you want quickly via saavn
- `/video <song name>` - download videos you want quickly

#### Admins only
- `/player` - open music player settings panel
- `/pause` - pause song play
- `/resume` - resume song play
- `/skip` - play next song
- `/end` - stop music play
- `/userbotjoin` - invite assistant to your chat
- `/userbotleave` - remove assistant from your chat
- `/admincache` - Refresh admin list
## For Channel
- /cplay <song name> - play lagu yang direquest
- /cdplay <song name> - play lagu yang direquest via deezer
- /csplay <song name> - play lagu yang direquest via jio saavn
- /cplaylist - Menampilkan lagu yang akan diputar
- /ccurrent - Menampilkan yang sedang diputar
- /csong <song name> - download lagu
- /csearch <query> - mencari lagu melalui youtube
- /cdeezer <song name> - download lagu via deezer
- /csaavn <song name> - download lagu via saavn
- /cvideo <song name> - download video

Admins only
- /cplayer - membuka pengaturan musik
- /cpause - menjeda pemutaran
- /cresume - memainkan ulang
- /cskip - skip lagu berikutnya
- /cend - stop pemutaran
- /userbotjoin - mengundang asisten bot musik
- /userbotleave - mengeluarkan asisten musik bot
- /admincache - Refresh admin"""

### Commands for Sudo Users 
- /userbotleaveall - remove assistant from all chats
- /gcast <reply to message> - globally brodcast replied message to all chats
- /pmpermit [on/off] - enable/disable pmpermit message

#### Pmpermit
- .a - approove someone to pm you
- .da - disapproove someone to pm you
+ Sudo Users can execute any command in any groups

## Support
- [Channel](https://t.me/ossuport3)
- [Group](https://t.me/ossuport)

## Credits
- [AUV-MUSIC](RIDWAN S)
