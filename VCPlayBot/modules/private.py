import os
from VCPlayBot.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = """
❁═════════════════════❁
HELLO ! [{}](tg://user?id={})!!**
      🎼 𝐁𝐔𝐙𝐙 𝐌𝐔𝐒𝐈𝐂 🎼
Bot untuk memutar musik dalam obrolan suara group chat anda.

🎧 Jangan lupa untuk menambahkan asisten musik juga, agar dapat memutar musiknya. 🎧
BUZZ TEAM [𝐁𝐔𝐙𝐙](https://telegra.ph/file/c5ac64ba0d35133e4411c.jpg)
OWNER : [𝐑𝐈𝐃𝐖𝐀𝐍](https://t.me/psycho_syridwan)
MODERATOR : [𝐉𝐄𝐒𝐘](https://t.me/OJssyy)

/help untuk mengetahui perintah
❁═════════════════════❁
"""
      HELP_MSG = [
        ".",
f"""
**YOW! 👋 Bantuan Perintah untuk {PROJECT_NAME}

⚪️ {PROJECT_NAME} Dapat memutar musik dalam VCG, mendownload lagu & video di group

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nklik next untuk mengetahui perintah**
""",

f"""
**Setting dulu**

1) Jadikan bot admin (Group dan channel kalau mengggunakan cplay)
2) Mulai voice chat
3) Coba /play [Lagu] untuk pertama kali mencoba dengan admin
*) kalau asisten join, enjoy music. kalau tidak, add @{ASSISTANT_NAME} di group dan coba lagi

**Untuk Channel Music Play**
1) Jadikan BOT admin dulu 
2) kirim /userbotjoinchannel dalam group
3) Lalu silahkan perintahkan dalam group

**Perintah**

**=>> Memutar 🎧**

- `/play <song name>` - play lagu yang direquest
- `/dplay <song name>` - play lagu yang direquest via deezer
- `/splay <song name>` - play lagu yang direquest via jio saavn
- `/playlist` - Menampilkan lagu yang akan diputar
- `/current` - Menampilkan yang sedang diputar
- `/song <song name>` - download lagu
- `/search <query>` - mencari lagu melalui youtube
- `/deezer <song name>` - download lagu via deezer
- `/saavn <song name>` - download lagu via saavn
- `/video <song name>` - download video

**=>> Tombol Menu ⏯**

- `/player` - membuka pengaturan musik
- `/pause` - menjeda pemutaran
- `/resume` - memainkan ulang
- `/skip` - skip lagu berikutnya
- `/end` - stop pemutaran
- `/userbotjoin` - mengundang asisten bot musik
- `/userbotleave` - mengeluarkan asisten musik bot
- `/admincache` - Refresh admin

***tombol menu pengaturan /player /curent /playlist hanya untuk admin**
""",
        
f"""
**=>> Channel Music Play 🛠**

⚪️ For linked group admins only:

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
- /userbotjoinchannel - mengundang asisten bot musik
- /userbotleave - mengeluarkan asisten musik bot
- /admincache - Refresh admin

channel hanya sedikit menambah perintah c ( /cplay = /channelplay )

⚪️ Kalau kamu suka untuk memutar dalam group sendiri:

1) Buat Group anda sendiri.
2) Add bot di GC dengan full setting admin
3) Add @{ASSISTANT_NAME} di channel sebagai admin.
4) Simpel perintah dalam group.
""",

f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Nyala/Mati Music player
- /admincache: Update / refresh admin dalam group
- /userbotjoin: Invite @{ASSISTANT_NAME} dalam group chat

**=>> Commands untuk developer**

 - /userbotleaveall - hapus assistant dari all chat
 - /gcast <reply to message> - global brodcast pesan reply
 - /pmpermit [on/off] - enable/disable pesan asisten
*Developer bisa eksekusi semua perintah dalam group manapun command

"""
      ]
