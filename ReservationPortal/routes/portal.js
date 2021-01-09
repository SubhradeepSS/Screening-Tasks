const express = require('express')
const router = express.Router()

const { ensureAuthenticated } = require("../conf/auth.js")


router.get('/', ensureAuthenticated, (req, res) => {
    res.render('portal/home', { user: req.user });
})

router.use('/reservation', require('./reservation'))
router.use('/customer', require('./customer'))

module.exports = router