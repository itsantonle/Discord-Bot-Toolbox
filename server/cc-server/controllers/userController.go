package controllers

import (
	"cc-server/initializers"
	"cc-server/models"

	"github.com/gin-gonic/gin"
)

func UserGet(c *gin.Context){
	var users []models.User 
	initializers.DB.Find(&users)
	c.JSON(201, gin.H{
		"user": users,
		"status": 200,
		"success": true,
		"message": "Users are sucessfully fetched from the DB!",
		"error": nil,
	})

}

func SingleUserGet(c *gin.Context){
	// Get from params
	id := c.Param("id")

	// make user 
	var user models.User 

	// find user using primary key
	initializers.DB.First(&user, id)
	c.JSON(201, gin.H{
		"user": user,
		"status": 200,
		"success": true,
		"message": "Users are sucessfully fetched from the DB!",
		"error": nil,
	})
}
func UserCreate(c *gin.Context) {
// get date off request body
var request struct {
	Guild int
	User int
	Level int
	Xp int 
	LevelUpXP int 
}
c.Bind(&request)

// append to db
user := models.User{Guild_id: request.Guild, User_id: request.User, Level: request.Level, Xp: request.Xp, Level_up_xp: request.LevelUpXP}
result := initializers.DB.Create(&user)

if result.Error != nil{
 
 c.JSON(500, gin.H{
	"user": nil,
	"status": 500,
	"success": false,
	"message": "Failed to Create User!",
	"error": result.Error.Error(),
 })
 
}

// send back a response

c.JSON(201, gin.H{
	"user": user,
	"status": 201,
	"success": true,
	"message": "User has been created!",
	"error": nil,
})
	
}

func UpdateUser(c *gin.Context){
	// get the id param
	id:= c.Param("id")
	// get data off request body

	var request struct {
		Guild int
		User int
		Level int
		Xp int 
		LevelUpXP int 
	}
	c.Bind(&request)

	// make user 
	var user models.User 

	// find user using primary key
	initializers.DB.First(&user, id)

	// update that 

	initializers.DB.Model(&user).Updates(models.User{
		Guild_id: request.Guild,
		User_id: request.User,
		Level: request.Level,
		Xp: request.Xp,
		Level_up_xp: request.LevelUpXP,
		
	})
	c.JSON(201, gin.H{
		"user": user,
		"status": 201,
		"success": true,
		"message": "User is succesfully updated!",
		"error": nil,
	})
	

	// resnd back a response 
}

func DeleteUser(c *gin.Context){
		// get the id param
		id:= c.Param("id")



		// find user using primary key and delete 
		initializers.DB.Delete(&models.User{}, id)

		

		// send back response 
		c.JSON(200, gin.H{
			"user": nil,
			"status": 200,
			"success": true,
			"message": "User is succesfully deleted!",
			"error": nil,
		})

}