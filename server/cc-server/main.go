package main

import (
	"cc-server/controllers"
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
 r.GET("/", controllers.UserGet)
 r.GET("/:id", controllers.SingleUserGet)
 r.POST("/post", controllers.UserCreate )
 r.PUT("/post/:id", controllers.UpdateUser)
 r.DELETE("/post/:id", controllers.DeleteUser)

 r.Run()

}