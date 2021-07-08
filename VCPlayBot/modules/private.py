import logging
from VCPlayBot.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from VCPlayBot.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME
logging.basicConfig(level=logging.INFO)
@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support 🧟", url="https://t.me/Kabaridevbot_bot"
                    ),
                    InlineKeyboardButton(
                        "Group 🧟", url="https://t.me/ossuport"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Owner 👱️", url="https://t.me/psycho_syridwan"
                    ),
                    InlineKeyboardButton(
                        "Moderator 👩", url="https://t.me/OJssyy"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Tambahkan bot ke Group 🎧️", url="http://t.me/auvbuzzbot?startgroup=true"
                    )
                    
                ],
                [
                    InlineKeyboardButton(
                        "Tambahkan Asiten 🎧️", url="http://t.me/asistenmusik2?startgroup=True"
                    )
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**🔴 {PROJECT_NAME} sedang online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Support Chat", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton("➕ AddTambahkan bot ke Group 🎧️", url=f"http://t.me/auvbuzzbot?startgroup=true")],
            [InlineKeyboardButton("➕ AddTambahkan asisten ke Group 🎧️", url=f"http://t.me/asistenmusik2?startgroup=true")],
            [InlineKeyboardButton(text = '📲 Updates', url=f"https://t.me/ossuport"),
             InlineKeyboardButton(text = 'REPORT 🧟', url=f"https://t.me/Kabaridevbot_bot")]
            [InlineKeyboardButton(text = '🛠 Creator 🛠', url=f"https://t.me/psycho_syridwan")],
            [InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '▶️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**🙋‍♀️ Hello Guyss! Saya bisa memutar musik & download video maupun musik di telegram groups & channels.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🟡 Click untuk bantuan 🟡", url=f"https://t.me/{BOT_USERNAME}?start"
                    )
                ]
            ]
        ),
    )

