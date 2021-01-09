const express = require('express')
const router = express.Router()
const bodyParser = require('body-parser')
const userController = require('../controllers/userController')

const jsonParser = bodyParser.json()

router.get('/', userController.loadUsers)
router.get('/users', userController.returnUsers)
router.delete('/users', userController.deleteUsers)
router.post('/users', jsonParser, userController.addUser)
router.get('/users/:id', userController.getUser)
router.delete('/users/:id', userController.deleteUser)


module.exports = router