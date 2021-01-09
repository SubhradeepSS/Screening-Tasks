const express = require('express')
const mongoose = require('mongoose')
const api = express()

const routes = require('./routes/api')
const creds = require('./creds')

const db = `mongodb+srv://${creds.username}:${creds.password}@${creds.cluster}.kigbf.mongodb.net/${creds.db}?retryWrites=true&w=majority`
const port = 3000

mongoose.connect(db, { useNewUrlParser: true, useUnifiedTopology: true })
    .then( () => {
        console.log('Database connected')
        api.listen(port)
    })
    .catch(err => {
        console.log("error")
    })

api.use('/', routes)