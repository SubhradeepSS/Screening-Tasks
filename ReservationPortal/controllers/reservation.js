const { Reservation } = require('../models/reservation')
const { Customer } = require('../models/customer')

const handleReservation = (req, res) => {
   Reservation.find({ user:req.user }, (err,reservations) => {
        Customer.find({ user:req.user }, (err_, customers) => {
            res.render('portal/reservation/reservations', { user: req.user, reservations, customers })
        })
   })
}

const handleReservationSubmit = (req, res) => {
    let newRes = new Reservation()
    newRes.time = req.body.time
    newRes.user = req.user
    Customer.findById(req.body.customer).then(cust => {
        newRes.customer = cust
        newRes.save().then(() => {
            res.redirect('/portal/reservation')
        })
    })
}

const reservationDetail = (req, res) => {
    Reservation.findById(req.body.reservationId).then(reservation => {
        Customer.find({ user:req.user }).then(customers => {
            res.render('portal/reservation/reservation', { reservation,customers })
        })
    })
}

const reservationEdit = (req, res) => {
    Reservation.findById(req.body.id).then(reservation => {
        Customer.findById(req.body.customer).then(customer => {
            reservation.customer = customer
            reservation.time = req.body.time
            reservation.save().then(() => {
                res.redirect('/portal/reservation')
            })
        })
    })
}

const reservationDelete = (req, res) => {
    Reservation.findByIdAndDelete(req.body.id).then(() => {
        res.redirect('/portal/reservation')
    })
}

module.exports = {
    handleReservationSubmit,
    handleReservation,
    reservationDelete,
    reservationDetail,
    reservationEdit
}