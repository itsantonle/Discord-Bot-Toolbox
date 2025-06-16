package main

import (
	"fmt"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

func main(){
// set up main first 
	dsn := "[LOAD USING ENV]"
	db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	fmt.Print(db)
if err != nil {
    fmt.Println("Failed to connect:", err)
    return
}
fmt.Println("Connected to Supabase!")

}