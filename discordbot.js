const Discord = require("discord.js")
const fs = require("fs")
const dotenv = require("dotenv")
dotenv.config()

const client = new Discord.Client()

fs.readdir("./events/", (err, files) => {
	files.forEach(file => {
		const eventHandler = require(`./events/${file}`)
		const eventName = file.split(".")[0]
		client.on(eventName, (...args) => eventHandler(client, ...args))
	})
})

client.login(process.env.TOKEN)