* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', sans-serif;
    background-color: #f4f4f9;
    display: flex;
    flex-direction: column;
}

.navbar {
    background-color: #2f4f4f;
    color: white;
    padding: 20px;
    text-align: center;
    font-size: 24px;
}

.sidebar {
    width: 250px;
    height: 100vh;
    background-color: #333;
    position: fixed;
    top: 0;
    left: 0;
    padding-top: 20px;
}

.sidebar ul {
    list-style-type: none;
    padding: 0;
}

.sidebar ul li {
    padding: 15px;
    text-align: center;
}

.sidebar ul li a {
    color: white;
    text-decoration: none;
    font-size: 18px;
}

.sidebar ul li a:hover {
    background-color: #575757;
}

.main-content {
    margin-left: 270px;
    padding: 30px;
    max-width: 1200px;
    margin-top: 20px;
}

h2 {
    font-size: 30px;
    margin-bottom: 20px;
}

.form-container {
    background-color: white;
    padding: 30px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    margin-bottom: 30px;
}

label {
    font-size: 18px;
    margin-bottom: 10px;
    display: block;
    margin-top: 15px;
}

input {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
    margin-bottom: 15px;
    font-size: 16px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

.submit-button {
    background-color: #2f4f4f;
    color: white;
    border: none;
    padding: 15px 30px;
    font-size: 18px;
    border-radius: 5px;
    cursor: pointer;
}

.submit-button:hover {
    background-color: #3e6666;
}

footer {
    background-color: #2f4f4f;
    color: white;
    text-align: center;
    padding: 15px;
    margin-top: 40px;
}
