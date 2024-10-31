import React, { useState } from 'react';
import axios from 'axios';

function BorrowBook() {
    const [userId, setUserId] = useState("");
    const [bookId, setBookId] = useState("");

    const handleBorrow = () => {
        axios.post('http://localhost:5000/borrow', { user_id: userId, book_id: bookId })
            .then(response => alert(response.data.message))
            .catch(error => console.error("Erro ao emprestar livro:", error));
    };

    return (
        <div>
            <h2>Empréstimo de Livro</h2>
            <input type="text" placeholder="ID do Usuário" value={userId} onChange={(e) => setUserId(e.target.value)} />
            <input type="text" placeholder="ID do Livro" value={bookId} onChange={(e) => setBookId(e.target.value)} />
            <button onClick={handleBorrow}>Emprestar</button>
        </div>
    );
}

export default BorrowBook;
