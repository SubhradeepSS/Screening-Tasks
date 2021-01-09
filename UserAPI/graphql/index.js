const express = require('express')
const mongoose = require('mongoose')
const { graphqlHTTP } = require('express-graphql')

const { username, password, cluster, db } = require('../mongo_express_node/creds')
const schema = require('./schema/schema')

const DB = `mongodb+srv://${username}:${password}@${cluster}.kigbf.mongodb.net/${db}?retryWrites=true&w=majority`
const port = 3000

const app = express()

mongoose.connect(DB, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => {
        console.log('Database connected')
        app.listen(port)
    })
    .catch(() => {
        console.log("error")
    })

app.use('/graphql', graphqlHTTP({
    schema,
    graphiql: true
}))