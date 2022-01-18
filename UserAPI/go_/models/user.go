package models

import (
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/sqlite"
)

type User struct {
	gorm.Model
	UserId   int           `json:"id"`
	Name     string        `json:"name"`
	Username string        `json:"username"`
	Email    string        `json:"email"`
	Address  AddressStruct `json:"address"`
	Company  CompanyStruct `json:"company"`
	Phone    string        `json:"phone"`
	Website  string        `json:"website"`
}
