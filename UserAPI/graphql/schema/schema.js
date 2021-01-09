const User = require('../models/user')
const graphql = require('graphql')

const { GraphQLSchema, GraphQLObjectType, GraphQLString, GraphQLList, GraphQLID } = graphql

const UserType = new GraphQLObjectType({
    name: "User",
    fields: {
        id: { type: GraphQLID },
        name: { type: GraphQLString },
        email: { type: GraphQLString },
        phone: { type: GraphQLString }
    }
})

const Query = new GraphQLObjectType({
    name: "Query",
    fields: {
        user: {
            type: UserType,
            args: { id: { type: GraphQLID } },
            resolve(parent, args) {
                return User.findById(args.id)
            }
        },
        users: {
            type: new GraphQLList(UserType),
            resolve(parent, args) {
                return User.find({})
            }
        }
    }
})

const Mutation = new GraphQLObjectType({
    name: 'Mutation',
    fields: {
        addUser: {
            type: UserType,
            args: {
                name: { type: GraphQLString },
                phone: { type: GraphQLString },
                email: { type: GraphQLString }
            },
            resolve(parent, args) {
                const newUser = new User(args)
                return newUser.save()
            }
        },
        editUser: {
            type: UserType,
            args: {
                id: { type: GraphQLID },
                name: { type: GraphQLString },
                phone: { type: GraphQLString },
                email: { type: GraphQLString }
            },
            resolve(parent, args) {
                return User.findByIdAndUpdate(
                    args.id,
                    { "$set": { name: args.name, email: args.email, phone: args.phone } }
                ).exec()
            }
        },
        deleteUser: {
            type: UserType,
            args: { id: { type: GraphQLID } },
            resolve(parent, args) {
                return User.findByIdAndDelete(args.id)
            }
        }
    }
})


module.exports = new GraphQLSchema({
    query: Query,
    mutation: Mutation
})