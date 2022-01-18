package models

import (
	_ "github.com/jinzhu/gorm/dialects/sqlite"
)

type AddressStruct struct {
	Street  string    `json:"street"`
	Suite   string    `json:"suite"`
	City    string    `json:"city"`
	Zipcode string    `json:"zipcode"`
	Geo     GeoStruct `json:"geo"`
}
