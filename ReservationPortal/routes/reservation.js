const express = require('express')
const router = express.Router()

const { ensureAuthenticated } = require("../conf/auth.js")

const { 
    handleReservationSubmit, 
    handleReservation,
    reservationDelete,
    reservationDetail,
    reservationEdit
} = require('../controllers/reservation')


router.get('/', ensureAuthenticated, handleReservation)
router.post('/', ensureAuthenticated, handleReservationSubmit)

router.post('/detail', ensureAuthenticated, reservationDetail)
router.post('/edit', ensureAuthenticated, reservationEdit)
router.post('/delete', ensureAuthenticated, reservationDelete)


module.exports = router