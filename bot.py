import discord
import yaml

with open('secret.yaml', 'r') as f:
    secret = yaml.load(f)

token = secret['token']
default_server_id = secret['server']

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.server is not None:
        return

    for s in client.servers:
        if s.id == str(default_server_id):
            server = s

    if message.content.startswith('%join') or message.content.startswith('%leave'):
        is_join = message.content.startswith('%join')

        channel_name = message.content.split(' ')[1]

        for channel in server.channels:
            # Both cases are needed in order to handle PMs which won't have the
            # id replacemeent
            if channel.id == channel_name[2:-1] or channel.name == channel_name[1:]:
                allow = discord.Permissions.none()
                deny = discord.Permissions.none()
                allow.read_messages = is_join
                allow.send_messages = is_join

                # If its a PM we need to connect the author to the server
                member = message.author
                if not isinstance(member, discord.Member):
                    for m in server.members:
                        if member.id == m.id:
                            member = m

                await client.edit_channel_permissions(
                    channel,
                    member,
                    allow=allow,
                    deny=deny,
                )

                await client.send_message(message.channel, 'Seems like a success.')
                return

        await client.send_message(message.channel, 'No such channel exists')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------------')


client.run(token)
