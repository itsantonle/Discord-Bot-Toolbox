package initializers

import (
	"fmt"
	"log"
	"os"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

var DB *gorm.DB
func ConnectToDB() {
	var err error
	dsn := os.Getenv("SUPABASE_ANON_KEY")
	DB, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		log.Fatal("❌ Failed to connect to database")
		return
	}
	fmt.Printf("✅ Connected to Supabase DB: %v!", DB.Name())

}