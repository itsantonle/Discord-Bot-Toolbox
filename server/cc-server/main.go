package main

import (
	"cc-server/initializers"

	"github.com/gin-gonic/gin"
)

func init(){
	initializers.LoadEnvVariables()
	initializers.ConnectToDB()
}
func main(){
 r:= gin.Default()


//  adding a GET ROUTE, works on 8080 by default
 r.GET("/ping", func(c *gin.Context){
	c.JSON(200, gin.H{
		"message": "pong",
	})
 })

 r.Run()

}