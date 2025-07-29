package main

import (
	"log"
	"encoding/json"
	"net/http"
	"database/sql"

	_ "github.com/mattn/go-sqlite3" // Import the SQLite driver

	"github.com/gorilla/mux"
)

type Link struct {
	ID   string `json:"id"`
	Name string `json:"name"`
	URL  string `json:"url"`
}

func updateLink(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    params := mux.Vars(r)
    var updatedLink Link
    err := json.NewDecoder(r.Body).Decode(&updatedLink)
    if err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }

    // Open database connection
    db, err := sql.Open("sqlite3", "profile.db")
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
    defer db.Close()

    // Update link in database
    _, err = db.Exec("UPDATE links SET name = ?, url = ? WHERE id = ?",
        updatedLink.Name, updatedLink.URL, params["id"])
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    // Update global profile variable
    profile := getProfile() 
    if profile != nil {
        for i, link := range profile.Links {
        if link.ID == params["id"] {
            profile.Links[i].Name = updatedLink.Name
            profile.Links[i].URL = updatedLink.URL
            break
        }
    }
    json.NewEncoder(w).Encode(updatedLink)
    }
}

func getProfile() *Profile {
    // This is a placeholder. In a real application, you would fetch the profile from a database or a global store.
    return &Profile{
        Links: []Link{
            {ID: "1", Name: "Old Name 1", URL: "http://oldurl1.com"},
            {ID: "2", Name: "Old Name 2", URL: "http://oldurl2.com"},
        },
    }
}

type Profile struct {
    Links []Link
}

func main() {
	// Initialize the database
	db, err := sql.Open("sqlite3", "profile.db")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// Create links table if it doesn't exist
	sqlStmt := `
	CREATE TABLE IF NOT EXISTS links (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		url TEXT
	);`
	_, err = db.Exec(sqlStmt)
	if err != nil {
		log.Printf("%q: %s\n", err, sqlStmt)
		return
	}

	router := mux.NewRouter()
	router.HandleFunc("/links/{id}", updateLink).Methods("PUT")
	log.Fatal(http.ListenAndServe(":8000", router))
}
