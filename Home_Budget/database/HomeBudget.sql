-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Дек 19 2024 г., 02:52
-- Версия сервера: 8.0.30
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `HomeBudget`
--

-- --------------------------------------------------------

--
-- Структура таблицы `ExpenseCategories`
--

CREATE TABLE `ExpenseCategories` (
  `CategoryID` int NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `ExpenseCategories`
--

INSERT INTO `ExpenseCategories` (`CategoryID`, `Name`) VALUES
(1, 'Продукты'),
(2, 'Транспорт'),
(3, 'Коммунальные услуги');

-- --------------------------------------------------------

--
-- Структура таблицы `Expenses`
--

CREATE TABLE `Expenses` (
  `ExpenseID` int NOT NULL,
  `SectionID` int NOT NULL,
  `Date` date NOT NULL,
  `Quantity` decimal(10,2) NOT NULL,
  `Price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `Expenses`
--

INSERT INTO `Expenses` (`ExpenseID`, `SectionID`, `Date`, `Quantity`, `Price`) VALUES
(1, 1, '2024-12-01', '2.50', '50.00'),
(2, 2, '2024-12-02', '20.00', '55.00'),
(3, 3, '2024-12-03', '100.00', '5.00'),
(4, 4, '2024-12-01', '0.50', '76.50'),
(5, 5, '2024-11-01', '1.00', '340.00'),
(6, 6, '2023-11-01', '2.00', '60.00');

-- --------------------------------------------------------

--
-- Структура таблицы `Sections`
--

CREATE TABLE `Sections` (
  `SectionID` int NOT NULL,
  `Name` varchar(255) NOT NULL,
  `CategoryID` int NOT NULL,
  `Unit` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `Sections`
--

INSERT INTO `Sections` (`SectionID`, `Name`, `CategoryID`, `Unit`) VALUES
(1, 'Черный хлебушек', 1, 'кг'),
(2, 'Бензинчик', 2, 'литр'),
(3, 'Электроэнергия', 3, 'кВт*ч'),
(4, 'Макарошки', 1, 'кг'),
(5, 'Пельмешки', 1, 'кг'),
(6, 'Соль', 1, 'кг');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `ExpenseCategories`
--
ALTER TABLE `ExpenseCategories`
  ADD PRIMARY KEY (`CategoryID`);

--
-- Индексы таблицы `Expenses`
--
ALTER TABLE `Expenses`
  ADD PRIMARY KEY (`ExpenseID`),
  ADD KEY `SectionID` (`SectionID`);

--
-- Индексы таблицы `Sections`
--
ALTER TABLE `Sections`
  ADD PRIMARY KEY (`SectionID`),
  ADD KEY `CategoryID` (`CategoryID`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `ExpenseCategories`
--
ALTER TABLE `ExpenseCategories`
  MODIFY `CategoryID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `Expenses`
--
ALTER TABLE `Expenses`
  MODIFY `ExpenseID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблицы `Sections`
--
ALTER TABLE `Sections`
  MODIFY `SectionID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `Expenses`
--
ALTER TABLE `Expenses`
  ADD CONSTRAINT `expenses_ibfk_1` FOREIGN KEY (`SectionID`) REFERENCES `Sections` (`SectionID`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `Sections`
--
ALTER TABLE `Sections`
  ADD CONSTRAINT `sections_ibfk_1` FOREIGN KEY (`CategoryID`) REFERENCES `ExpenseCategories` (`CategoryID`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
