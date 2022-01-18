package models

import (
	_ "github.com/jinzhu/gorm/dialects/sqlite"
)

type CompanyStruct struct {
	Name        string `json:"name"`
	CatchPhrase string `json:"catchPhrase"`
	Bs          string `json:"bs"`
}
