const { Customer } = require('../models/customer')
const { Reservation } = require('../models/reservation')

const handleCustomer = (req, res) => {
    Customer.find({user: req.user}, (err, customers) => {
        res.render('portal/customer/customers', { user: req.user, customers })
    })
}

const handleCustomerSubmit = (req, res) => {
    let newCustomer = new Customer()
    newCustomer.user = req.user
    newCustomer.name = req.body.name
    newCustomer.contact = req.body.contact

    newCustomer.save().then(() => {
        res.redirect('/portal/customer')
    })
}

const customerDetail = (req, res) => {
    Customer.findById(req.body.customerId).then(customer => {
        res.render('portal/customer/customer', { customer })
    })
}

const customerEdit = (req, res) => {
    Customer.findById(req.body.id).then(customer => {
        customer.name = req.body.name
        customer.contact = req.body.contact
        customer.save().then(() => {
            res.redirect('/portal/customer')
        })
    })
}

const customerDelete = (req, res) => {
    Customer.findById(req.body.id).then(customer => {
        Reservation.deleteMany({ customer }).then(() => {
            customer.remove().then(() => {
                res.redirect('/portal/customer')
            })
        })
    })
}

module.exports = {
    handleCustomerSubmit,
    handleCustomer,
    customerDetail,
    customerDelete,
    customerEdit
}