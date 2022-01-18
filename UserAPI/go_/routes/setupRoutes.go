package routes

import (
	"example.com/user/controllers"
	"github.com/gofiber/fiber/v2"
)

func SetupRoutes(app *fiber.App) {
	app.Get("/", controllers.LoadUsers)
	app.Get("/users", controllers.GetUsers)
	app.Post("/users", controllers.AddUser)
	app.Get("/users/:id", controllers.GetUser)
	app.Delete("/users", controllers.DeleteUsers)
	app.Delete("/users/:id", controllers.DeleteUser)
}
