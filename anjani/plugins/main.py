from typing import Optional
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from anjani import command

async def cmd_start(self, ctx: command.Context) -> Optional[str]:
    """Bot start command with anime shadow + Anuvibe theme"""
    chat = ctx.chat

    if chat.type == ChatType.PRIVATE:
        if ctx.input and ctx.input == "help":
            keyboard = await self.help_builder(chat.id)
            await ctx.respond(
                await self.text(chat.id, "help-pm", self.bot_name),
                reply_markup=InlineKeyboardMarkup(keyboard),
            )
            return None

        await ctx.respond_photo(
            photo="https://files.catbox.moe/qr0if2.jpg",
            caption=(
                "✨ **Kon'nichiwa, Master!**\n\n"
                "⚔️ I am **Shadow**, your loyal Anuvibe sentinel.\n"
                "🎴 Trained in silence, summoned for balance — I moderate with mastery.\n\n"
                "🌸 Add me to your group and let’s rewrite the clan destiny together."
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("👑 Anuvibe", url="https://t.me/Anuvibe"),
                        InlineKeyboardButton("➕ Summon to Clan", url=f"https://t.me/{self.bot.user.username}?startgroup=true"),
                    ],
                    [
                        InlineKeyboardButton("📚 Help", url=f"https://t.me/{self.bot.user.username}?start=help"),
                        InlineKeyboardButton("🛠 Support", url="https://t.me/Anuvibe"),
                    ],
                ]
            ),
            parse_mode=ParseMode.MARKDOWN,
        )
        return None

    return await self.text(chat.id, "start-chat")
