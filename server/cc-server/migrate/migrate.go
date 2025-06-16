package main

import (
	"cc-server/initializers"
	"cc-server/models"
)

func init() {
	initializers.LoadEnvVariables()
	initializers.ConnectToDB()

}

func main() {
	initializers.DB.AutoMigrate(&models.User{})
	
}