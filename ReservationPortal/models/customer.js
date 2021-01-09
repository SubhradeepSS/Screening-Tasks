const mongoose = require('mongoose')
const { UserSchema } = require('./user')
const Schema = mongoose.Schema

const CustomerSchema = new Schema({
    name: String,
    contact: String,
    user: UserSchema
})

const Customer = mongoose.model('Customer', CustomerSchema)

module.exports = { Customer, CustomerSchema }