package models

import (
	_ "github.com/jinzhu/gorm/dialects/sqlite"
)

type GeoStruct struct {
	Lat string `json:"lat"`
	Lng string `json:"lng"`
}
