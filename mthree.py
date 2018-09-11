import morse
import discord
async def wcode(self, txt, code):
        for z in txt:
            await self.client.say(code[z])

code = morse.mtt()
