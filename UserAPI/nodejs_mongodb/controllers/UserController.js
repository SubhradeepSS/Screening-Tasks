const User = require('../models/user')
const axios = require('axios')

const url = "https://jsonplaceholder.typicode.com/users"

const loadUsers = (req, res) => {
    axios.get(url)
    .then(result => {
        result.data.forEach(user => {
            const User = new User(user)
            User.save()
        })
        res.send("Loading Successful!!")
    })
    .catch(err => {
        console.log(err)
        res.send("error")
    })
}

const returnUsers = (req, res) => {
    User.find({}, (err, usersList) => {
        if(err){
            console.log(err)
            res.status(400).send("error")
        }
        res.status(200).json(usersList)
    })
    .catch(err => {
        console.log(err)
        res.status(400).send("error")
    })
}

const deleteUsers = (req, res) => {
    User.deleteMany({}, err => {
        if(err){
            console.log(err)
            res.status(400).send("error")
        }
        res.status(200).send("Deleted all users")
    })
    .catch(err => {
        console.log(err)
        res.status(400).send("error")
    })
}

const addUser = (req, res) => {
    const user = new User(req.body)
    user.save()
        .then( () => {
            res.status(200).send("User added successfully")
        })
        .catch(err => {
            console.log(err)
            res.status(400).send("error")
        })
}

const getUser = (req, res) => {
    User.findOne({id: req.params.id})
        .then(user => {
            res.status(200).json(user)
        })
        .catch(err => {
            console.log(err)
            res.status(400).send("error")
        })
}

const deleteUser = (req, res) => {
    User.deleteOne({id: req.params.id})
        .then(() => {
            res.status(200).send("Deleted user successfully")
        })
        .catch(err => {
            console.log(err)
            res.status(400).send("Error in deleting")
        })
}

module.exports = {
    loadUsers,
    returnUsers,
    deleteUsers,
    addUser,
    getUser,
    deleteUser
}