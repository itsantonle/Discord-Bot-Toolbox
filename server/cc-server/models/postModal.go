package models

import "gorm.io/gorm"

// this is for the user model
type User struct{
	gorm.Model
	Guild_id int
	User_id int 
	Level int 
	Xp int 
	Level_up_xp int 
}