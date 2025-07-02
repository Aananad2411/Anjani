async def cmd_start(self, ctx: command.Context) -> Optional[str]:
        """Bot start command"""
        chat = ctx.chat

        if chat.type == ChatType.PRIVATE:
            if ctx.input and ctx.input == "help":
                keyboard = await self.help_builder(chat.id)
                await ctx.respond(
                    await self.text(chat.id, "help-pm", self.bot_name),
                    reply_markup=InlineKeyboardMarkup(keyboard),
                )
                return None

            # Custom start photo and welcome message
            await ctx.respond_photo(
                photo="https://graph.org/file/681bb329b240aed64ae78-bde0fa7c1abd4e594d.jpg",
                caption=(
                    "**Hey there!**\n\n"
                    "My name is **Shadow**.\n"
                    "I can manage your group with lots of useful features.\n"
                    "Feel free to add me to your group!"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "👑 Owner", url="https://t.me/silent_Shadowzz"
                            ),
                            InlineKeyboardButton(
                                "➕ Add to your clan",
                                url=f"https://t.me/{self.bot.user.username}?startgroup=true"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                "📚 Help",
                                url=f"https://t.me/{self.bot.user.username}?start=help"
                            ),
                            InlineKeyboardButton(
                                "🛠 Support",
                                url="https://t.me/Inside_ShadowzMind"
                            ),
                        ],
                    ]
                ),
                parse_mode=ParseMode.MARKDOWN,
            )
            return None

        return await self.text(chat.id, "start-chat")
