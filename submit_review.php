<?php
// Параметры подключения к базе данных
$servername = "localhost";
$db_username = "root"; // Замените на ваше имя пользователя БД
$db_password = "1362"; // Замените на ваш пароль БД
$dbname = "underplayer"; // Название вашей БД

// Создаем соединение
$conn = new mysqli($servername, $db_username, $db_password, $dbname);

// Проверка соединения
if ($conn->connect_error) {
    die("Ошибка подключения: " . $conn->connect_error);
}

// Проверка метода POST
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $user_name = trim($_POST["username"]);
    $review_text = trim($_POST["review"]);

    if (!empty($user_name) && !empty($review_text)) {
        // Использование подготовленного запроса для защиты от SQL инъекций
        $stmt = $conn->prepare("INSERT INTO reviews (username, review, created_at) VALUES (?, ?, NOW())");
        if ($stmt === false) {
            die("Ошибка подготовки запроса: " . $conn->error);
        }
        $stmt->bind_param("ss", $user_name, $review_text);
        if ($stmt->execute()) {
            echo "Спасибо за ваш отзыв!";
        } else {
            echo "Ошибка при сохранении отзыва: " . $stmt->error;
        }
        $stmt->close();
    } else {
        echo "Пожалуйста, заполните все поля.";
    }
} else {
    echo "Неверный метод запроса.";
}

$conn->close();
?> 
