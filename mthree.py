import morse
import discord
async def wcode(self, txt, code):
        code = morse.mtt()
        for z in txt:
            await self.client.say(code[z])
