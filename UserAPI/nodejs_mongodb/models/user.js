const mongoose = require('mongoose')
const Schema = mongoose.Schema

const CompanySchema = new Schema({
    name: String,
    catchPhrase: String,
    bs: String
})

const GeoSchema = new Schema({
    lat: String,
    lng: String
})

const AddressSchema = new Schema({
    street: String,
    suite: String,
    city: String,
    zipcode: String,
    geo: GeoSchema
})

const UserSchema = new Schema ({
    id: Number,
    name: String,
    username: String,
    email: String,
    address: AddressSchema,
    phone: String,
    website: String,
    company: CompanySchema
})


const User = mongoose.model('user', UserSchema)

module.exports = User