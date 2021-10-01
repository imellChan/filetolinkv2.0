import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def handle_force_sub(bot: Client, cmd: Message):
    try:
        user = await bot.get_chat_member(chat_id=(int(os.getenv('ID_CHANNEL')) if os.getenv('ID_CHANNEL').startswith("-100") else os.getenv('ID_CHANNEL')), user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Banned!",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        try:
            invite_link = await bot.create_chat_invite_link(chat_id=(int(os.getenv('ID_CHANNEL')) if os.getenv('ID_CHANNEL').startswith("-100") else os.getenv('ID_CHANNEL')))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            invite_link = await bot.create_chat_invite_link(chat_id=(int(os.getenv('ID_CHANNEL')) if os.getenv('ID_CHANNEL').startswith("-100") else os.getenv('ID_CHANNEL')))
        except Exception as err:
            print(f"Eror koneksi ke {os.getenv('ID_CHANNEL')}\n\nError: {err}")
            return 200
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Mohon Join Terlebih Dahulu!\nSetelah itu refresh.**,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("(❁´◡`❁) Join Dulu Mas", url=os.getenv('ID_CHANNEL'))
                    ],
                    [
                        InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshForceSub")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something went Wrong. Contact my [Support Group](https://t.me/DevsZone).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
    return 200
