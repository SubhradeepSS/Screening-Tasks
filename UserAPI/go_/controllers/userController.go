package controllers

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"

	"example.com/user/db"
	"example.com/user/models"
	"github.com/gofiber/fiber/v2"
)

func LoadUsers(c *fiber.Ctx) error {
	resp, err := http.Get("https://jsonplaceholder.typicode.com/users")
	if err != nil {
		fmt.Println(err.Error())
		os.Exit(1)
	}

	respData, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err)
	}

	var userList []models.User
	json.Unmarshal(respData, &userList)

	for _, user := range userList {
		dbConn := db.DBConn
		dbConn.Create(&user)
	}

	return c.JSON(userList)
}

func GetUsers(c *fiber.Ctx) error {
	dbConn := db.DBConn
	var users []models.User
	dbConn.Find(&users)
	return c.JSON(users)
}

/* `FIND` queries by ID of gorm and not by the id specified in struct */

func GetUser(c *fiber.Ctx) error {
	id := c.Params("id")
	dbConn := db.DBConn
	var user models.User
	dbConn.Find(&user, id)
	return c.JSON(user)
}

func DeleteUser(c *fiber.Ctx) error {
	id := c.Params("id")
	dbConn := db.DBConn
	var user models.User
	dbConn.Find(&user, id)
	dbConn.Delete(&user)
	return c.SendString("Deleted user")
}

func DeleteUsers(c *fiber.Ctx) error {
	dbConn := db.DBConn
	var users []models.User
	dbConn.Delete(&users)
	return c.SendString("Deleted all users from db")
}

func AddUser(c *fiber.Ctx) error {
	dbConn := db.DBConn
	user := new(models.User)

	if err := c.BodyParser(user); err != nil {
		return c.SendString(err.Error())
	}
	dbConn.Create(&user)
	return c.JSON(user)
}
