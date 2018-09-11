import morse
import discord
def wcode(txt, code):
        code = morse.mtt()
        for z in txt:
            await self.client.say(code[z])
