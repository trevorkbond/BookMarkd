import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5001";

function App() {
  const [health, setHealth] = useState(null);
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch health status
    axios
      .get(`${API_URL}/api/health`)
      .then((response) => {
        setHealth(response.data);
      })
      .catch((error) => {
        console.error("Error fetching health:", error);
      });

    // Fetch books
    axios
      .get(`${API_URL}/api/books`)
      .then((response) => {
        setBooks(response.data.books);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching books:", error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>BookMarkd</h1>
        <p>Your all-in-one book tracker</p>
        {health && (
          <p className="health-status">
            API Status: {health.status} - {health.message}
          </p>
        )}
      </header>
      <main className="App-main">
        <section className="books-section">
          <h2>Books</h2>
          {loading ? (
            <p>Loading books...</p>
          ) : books.length > 0 ? (
            <ul className="books-list">
              {books.map((book) => (
                <li key={book.id}>
                  {book.title} by {book.author}
                </li>
              ))}
            </ul>
          ) : (
            <p>No books found. Start by adding your first book!</p>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;
