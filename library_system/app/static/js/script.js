let books = [];

// Book colors for visual variety
const bookColors = [
    '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7',
    '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9'
];

const booksList = document.getElementById('booksList');
const emptyMessage = document.getElementById('emptyMessage');
const emptyList = document.getElementById('emptyList');

// Initialize the library system
async function initializeLibrary() {
    showLoading();

    const response = await fetch('/get', {
        method: 'GET'
    })

    if (!response.ok) {
        const errorData = await response.json();
        showError();
        showNotification(errorData.error, 'error')
        return
    }

    const {data} = await response.json();

    data.forEach(book => {
        addBookToShelf(book);
        addBookToList(book);
    })

    books = data;

    updateBookList();
    hideLoading();
    showNotification('Library system loaded successfully!', 'success');
}

// Show loading screen
function showLoading() {
    document.getElementById('loadingScreen').classList.remove('hidden');
}

// Hide loading screen
function hideLoading() {
    document.getElementById('loadingScreen').classList.add('hidden');
}

// Show error screen
function showError() {
    document.getElementById('loadingScreen').classList.add('hidden');
    document.getElementById('errorScreen').classList.remove('hidden');
}

// Hide error screen
function hideError() {
    document.getElementById('errorScreen').classList.add('hidden');
}

// Retry loading
function retryLoading() {
    hideError();
    initializeLibrary();
}

// Show notification
function showNotification(message, type = 'info') {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.className = `notification ${type}`;
    notification.classList.add('show');
    
    setTimeout(() => {
        notification.classList.remove('show');
    }, 3000);
}

// Add book function
async function addBook() {
    const titleInput = document.getElementById('bookTitle');
    const authorInput = document.getElementById('bookAuthor');
    
    const title = titleInput.value.trim();
    const author = authorInput.value.trim();
    
    if (!title || !author) {
        showNotification('Please fill in both title and author fields', 'error');
        return;
    }

    // Create book object

    const form = new FormData()
    form.append('title', title)
    form.append('author', author)

    try {
        const response = await fetch('/add', {
            method: 'POST',
            body: form
        })

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Unknow error')
        }

        const data = await response.json();

        const book = {
            bid: data.bid,
            title: title,
            author: author,
            color: bookColors[Math.floor(Math.random() * bookColors.length)]
        };


        // Add book to shelf with animation
        addBookToShelf(book);   

        // Update books list
        addBookToList(book);

        // Local arrayy
        books.push(book);

        // Clear form
        titleInput.value = '';
        authorInput.value = '';

        updateBookList();
        showNotification(`"${title}" added to your library!`, 'success');
    }
    catch (error) {
        showNotification(`${error.message}`, 'error');
    }
}

// Add book to shelf visually
function addBookToShelf(book) {

    const color = bookColors[Math.floor(Math.random()*bookColors.length)];

    const booksContainer = document.getElementById('booksContainer');
    
    const bookElement = document.createElement('div');
    bookElement.className = 'book book-adding';
    bookElement.style.backgroundColor = color;
    bookElement.dataset.bookId = book.bid;
    
    const spineElement = document.createElement('div');
    spineElement.className = 'book-spine';
    spineElement.textContent = book.title.substring(0, 15);
    
    bookElement.appendChild(spineElement);
    bookElement.onclick = () => removeBook(book.bid, book.title);
    
    booksContainer.appendChild(bookElement);
}

// Remove book function
async function removeBook(bookId, bookTitle) {

    try {
        const response = await fetch(`/remove/${bookId}` , {
            method: 'DELETE'
        })

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error);
        }

        const bookElement = document.querySelector(`[data-book-id="${bookId}"]`);
        const listedBook = document.querySelector(`[data-list-id="${bookId}"]`);

        if (bookElement) {
            bookElement.classList.add('book-removing');
        }
        
        setTimeout(() => {
            bookElement.remove();
            listedBook.remove();
            books.splice(bookId - 1, 1);

            if (books.length === 0) {
                document.getElementById('emptyMessage').style.display = 'block';
            }
            
            updateBookList();  
            showNotification(`"${bookTitle}" removed from library`, 'info');
        }, 600);             
              
    }
    catch (error) {
        showNotification(error.message, 'error');
    }

}

// Update books list in side panel
function addBookToList(book) {
    const bookItem = document.createElement('div');
    bookItem.className = 'book-item';
    bookItem.setAttribute('data-list-id', book.bid);
    bookItem.innerHTML = `
        <div class="book-title">${book.title}</div>
        <div class="book-author">by ${book.author}</div>
        <button class="remove-btn" onclick="removeBook(${book.bid}, '${book.title}')">Remove</button>
    `;

    booksList.appendChild(bookItem);
}


function updateBookList() {
    if (books.length == 0) {
        emptyList.classList.remove('hidden');
        emptyMessage.classList.remove('hidden');
    } else {
        emptyList.classList.add('hidden');
        emptyMessage.classList.add('hidden');
    }
}

// Handle Enter key in form inputs
    document.getElementById('bookTitle').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            document.getElementById('bookAuthor').focus();
        }
    });

document.getElementById('bookAuthor').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        addBook();
    }
});

// Initialize the library system when page loads
window.addEventListener('DOMContentLoaded', initializeLibrary);