package controllers

import (
	"encoding/json"
	"io/ioutil"
	"net/http"

	"example.com/user/db"
	"example.com/user/models"
	"github.com/gofiber/fiber/v2"
	"github.com/jinzhu/gorm"
)

func LoadUsers(c *fiber.Ctx) error {
	resp, err := http.Get("https://jsonplaceholder.typicode.com/users")
	if err != nil {
		return c.Status(500).SendString(err.Error())
	}

	respData, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		c.Status(500).SendString(err.Error())
	}

	var userList []models.User
	json.Unmarshal(respData, &userList)

	dbConn := db.DBConn
	for _, user := range userList {
		if err := dbConn.Create(&user).Error; err != nil {
			return c.Status(500).SendString(err.Error())
		}
	}

	return c.Status(201).SendString("Loaded all users to db")
}

func GetUsers(c *fiber.Ctx) error {
	dbConn := db.DBConn
	var users []models.User
	if err := dbConn.Find(&users).Error; err != nil {
		return c.Status(500).SendString(err.Error())
	}
	return c.JSON(users)
}

/* `FIND` queries by ID of gorm and not by the id specified in struct */

func GetUser(c *fiber.Ctx) error {
	id := c.Params("id")
	dbConn := db.DBConn
	var user models.User
	err := dbConn.Find(&user, id).Error
	if err == gorm.ErrRecordNotFound {
		return c.Status(404).SendString("User not found")
	}
	if err != nil {
		return c.Status(500).SendString(err.Error())
	}
	return c.JSON(user)
}

func DeleteUser(c *fiber.Ctx) error {
	id := c.Params("id")
	dbConn := db.DBConn
	var user models.User

	res := dbConn.Find(&user, id)
	if res.Error == gorm.ErrRecordNotFound {
		return c.Status(404).SendString("User not found")
	}
	if res.Error != nil {
		return c.Status(500).SendString(res.Error.Error())
	}

	if err := dbConn.Delete(&user).Error; err != nil {
		return c.Status(500).SendString(err.Error())
	}
	return c.SendStatus(204)
}

func DeleteUsers(c *fiber.Ctx) error {
	dbConn := db.DBConn
	var users []models.User
	if err := dbConn.Delete(&users).Error; err != nil {
		return c.Status(500).SendString(err.Error())
	}
	return c.SendStatus(204)
}

func AddUser(c *fiber.Ctx) error {
	dbConn := db.DBConn
	user := new(models.User)

	if err := c.BodyParser(user); err != nil {
		return c.Status(400).SendString(err.Error())
	}
	if err := dbConn.Create(&user).Error; err != nil {
		return c.Status(500).SendString(err.Error())
	}
	return c.Status(201).SendString("User added to db")
}
