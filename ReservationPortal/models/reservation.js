const mongoose = require('mongoose')
const Schema = mongoose.Schema

const { CustomerSchema } = require('./customer')
const { UserSchema } = require('./user')

const ReservationSchema = new Schema({
    time: Date,
    user: UserSchema,
    customer: CustomerSchema
})

const Reservation = mongoose.model('Reservation', ReservationSchema)

module.exports = { Reservation, ReservationSchema }