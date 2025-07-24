# ✨ Anime Themed Main Plugin ✨

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from anjani import plugin, command, filters, util
from pyrogram.enums.chat_type import ChatType
from pyrogram.enums.parse_mode import ParseMode

class Main(plugin.Plugin):
    name = "Main"

    async def cmd_start(self, ctx: command.Context) -> str | None:
        chat = ctx.chat
        if chat.type == ChatType.PRIVATE:
            if ctx.input == "help":
                keyboard = await self.help_builder(chat.id)
                await ctx.respond(
                    f"🌸 **Welcome, Senpai!**\n\n"
                    f"✨ I'm your Anime-styled assistant — ready to manage, protect, and entertain!\n"
                    f"💫 Use the buttons below to explore my powers.",
                    reply_markup=InlineKeyboardMarkup(keyboard),
                )
                return

            # Add-to-group / start-help buttons
            permissions = [
                "change_info", "post_messages", "edit_messages", "delete_messages",
                "restrict_members", "invite_users", "pin_messages",
                "promote_members", "manage_video_chats", "manage_chat"
            ]
            buttons = [
                [
                    InlineKeyboardButton("🌠 Add Me to Group", url=f"t.me/{self.bot.user.username}?startgroup=true&admin={'+'.join(permissions)}"),
                    InlineKeyboardButton("📖 Help Menu", url=f"t.me/{self.bot.user.username}?start=help"),
                ]
            ]

            await ctx.respond(
                f"👋 Kon'nichiwa, **{self.bot.user.first_name}** desu~!\n"
                f"I'm here to help with **moderation, info, and fun**.\n\n"
                f"🎌 Use /help to see all my commands.\n"
                f"💮 Powered by *Anjani Management Bot*.",
                reply_markup=InlineKeyboardMarkup(buttons),
                disable_web_page_preview=True,
                parse_mode=ParseMode.MARKDOWN,
            )
            return None

        return "💠 Use me in private for commands, Senpai~!"

    async def cmd_help(self, ctx: command.Context) -> None:
        chat = ctx.chat
        if chat.type != ChatType.PRIVATE:
            await ctx.respond(
                "🗒️ Use /help in **PM** to see full command list! 🎀",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("📬 Help in PM", url=f"t.me/{self.bot.user.username}?start=help")]
                ])
            )
            return

        keyboard = await self.help_builder(chat.id)
        await ctx.respond(
            "🌟 Choose your destiny!\nPick a plugin below to see its commands 🔮",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    async def cmd_donate(self, ctx: command.Context) -> None:
        await ctx.respond(
            "🌸 Want to support my creators?\nYour kindness keeps this bot running smoothly 💖",
            disable_web_page_preview=True,
        )

    async def cmd_privacy(self, ctx: command.Context) -> None:
        await ctx.respond(
            "🔐 Privacy is our top priority!\nRead the full policy below:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔍 Privacy Policy", url="https://userbotindo.com/privacy")]
            ])
        )

    async def cmd_markdownhelp(self, ctx: command.Context) -> None:
        await ctx.respond(
            "📘 *Markdown* lets you format your messages like a pro!\n"
            "`**bold**`, `__italic__`, `~~strike~~`, and more~",
            parse_mode=ParseMode.MARKDOWN,
        )

    @command.filters(aliases=["fillinghelp"])
    async def cmd_formathelp(self, ctx: command.Context) -> None:
        await ctx.respond(
            "📋 Here's the proper format for filling forms:\n\n"
            "`Field1: Value`\n`Field2: Value`\n\nUse this in commands like `/submit`",
            parse_mode=ParseMode.MARKDOWN,
            )
