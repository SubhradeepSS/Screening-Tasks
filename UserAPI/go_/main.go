package main

import (
	"example.com/user/db"
	"example.com/user/routes"
	"github.com/gofiber/fiber/v2"
)

func main() {
	app := fiber.New()

	db.InitDatabase()

	routes.SetupRoutes(app)
	app.Listen(":3000")

	db.CloseDatabase()
}
