const express = require('express')
const router = express.Router()

const { ensureAuthenticated } = require("../conf/auth.js")

const { 
    handleCustomerSubmit, 
    handleCustomer,
    customerDetail,
    customerDelete,
    customerEdit
} = require('../controllers/customer')


router.get('/', ensureAuthenticated, handleCustomer)
router.post('/', ensureAuthenticated, handleCustomerSubmit)

router.post('/detail', ensureAuthenticated, customerDetail)
router.post('/edit', ensureAuthenticated, customerEdit)
router.post('/delete', ensureAuthenticated, customerDelete)

module.exports = router