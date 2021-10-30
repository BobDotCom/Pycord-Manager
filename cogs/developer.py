from discord.ext.commands import command
from jishaku.codeblocks import codeblock_converter
from jishaku.modules import ExtensionConverter

from utils import Cog


class Developer(Cog, command_attrs={"hidden": True}):
    def __init__(self, bot) -> None:
        super().__init__(bot)
        self.jishaku = bot.get_cog("Jishaku")

    @command(name="eval")
    async def _eval(self, ctx, *, code: codeblock_converter):
        await self.jishaku.jsk_python(ctx, code)

    @command(aliases=["reload"])
    async def load(self, ctx, *files: ExtensionConverter):
        await self.jishaku.jsk_load(ctx, *files)

    @command()
    async def unload(self, ctx, *files: ExtensionConverter):
        await self.jishaku.jsk_unload(ctx, *files)

    @command()
    async def shutdown(self, ctx):
        await ctx.send("Shutting down.")
        await self.bot.close()

    @command()
    async def pull(self, ctx):
        cog = self.bot.get_cog("Jishaku")
        await cog.jsk_git(ctx, "pull")

    async def cog_check(self, ctx):
        return ctx.author.id in self.bot.owner_ids


def setup(bot):
    bot.add_cog(Developer(bot))
