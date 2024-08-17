-- phpMyAdmin SQL Dump
-- version 5.2.1deb1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 17, 2024 at 09:02 PM
-- Server version: 10.11.6-MariaDB-0+deb12u1
-- PHP Version: 8.2.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `SistVeterinaria`
--

-- --------------------------------------------------------

--
-- Table structure for table `Citas`
--

CREATE TABLE `Citas` (
  `id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `mascota_id` int(11) NOT NULL,
  `procedimiento_id` int(11) DEFAULT NULL,
  `opcion` int(11) DEFAULT NULL,
  `cantidad_accesorios` int(11) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Citas`
--

INSERT INTO `Citas` (`id`, `fecha`, `hora`, `mascota_id`, `procedimiento_id`, `opcion`, `cantidad_accesorios`) VALUES
(1, '2024-10-10', '12:00:00', 22, NULL, NULL, 1),
(2, '2024-10-11', '12:00:00', 22, NULL, NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Mascotas`
--

CREATE TABLE `Mascotas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `peso` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Mascotas`
--

INSERT INTO `Mascotas` (`id`, `nombre`, `tipo`, `peso`) VALUES
(1, 'Rex', 'Perro', 12.50),
(2, 'bob', 'perro', 7.00),
(3, 'pedro', 'pug', 8.00),
(4, 'robert', 'cat', 8.00),
(5, 'bolacio', 'iguana', 2.00),
(6, 'terry', 'exterry', 500.00),
(7, 'pedro', 'pug', 8.00),
(8, 'adrian', 'rana', 0.20),
(9, 'dago', 'perro', 80.00),
(10, 'pedro', 'pug', 7.00),
(11, 'dagin messi', 'primera chamba', 106.00),
(12, 'bob', 'chihuaha', 8.00),
(13, 'pit', 'bull', 89.00),
(14, 'adria', 'geko', 1.00),
(15, 'pug', 'gato', 2.00),
(16, 'Rambola', 'Pug', 10.00),
(17, 'chuy', 'cerdo', 45.00),
(18, 'chuy', 'cerdo', 45.00),
(19, 'zahid', 'cangrejo', 1.00),
(20, 'isra', 'cangrejo ', 1.00),
(21, 'pepe', 'pug', 11.00),
(22, 'rani', 'rana', 1.00),
(23, 'bob', 'pug', 10.00),
(24, 'pedro', 'pug', 10.00),
(25, 'robert', 'gato', 6.00),
(26, 'squirtle', 'tortuga', 2.00),
(27, 'daniel', 'huron', 4.00),
(28, 'romona', 'pug', 12.00);

-- --------------------------------------------------------

--
-- Table structure for table `PreciosAccesorios`
--

CREATE TABLE `PreciosAccesorios` (
  `id` int(11) NOT NULL,
  `precio` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `PreciosAccesorios`
--

INSERT INTO `PreciosAccesorios` (`id`, `precio`) VALUES
(1, 95.00),
(2, 150.00),
(3, 55.00),
(4, 230.00),
(5, 150.00);

-- --------------------------------------------------------

--
-- Table structure for table `Procedimientos`
--

CREATE TABLE `Procedimientos` (
  `id` int(11) NOT NULL,
  `tipo` int(11) DEFAULT NULL,
  `opcion` int(11) DEFAULT NULL,
  `cantidad_accesorios` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Procedimientos`
--

INSERT INTO `Procedimientos` (`id`, `tipo`, `opcion`, `cantidad_accesorios`) VALUES
(1, 1, 2, 3),
(2, 2, 3, 45),
(3, 3, NULL, 1),
(4, 3, NULL, 1),
(5, 4, 1, 5),
(6, 2, NULL, 1),
(7, 3, NULL, 1),
(8, 4, NULL, 2),
(9, 1, 3, NULL),
(10, 2, 4, NULL),
(11, 2, 6, NULL),
(12, 1, 2, 1),
(13, 2, NULL, 1),
(14, 3, NULL, 1),
(15, 2, NULL, 1),
(16, 4, 1, 2),
(17, 3, NULL, 1),
(18, 4, 4, 34),
(19, 4, 5, 1),
(20, 3, NULL, 1),
(21, 3, NULL, 1),
(22, 4, 5, 5),
(23, 4, 1, 1),
(24, 4, 5, 10);

-- --------------------------------------------------------

--
-- Table structure for table `Registros`
--

CREATE TABLE `Registros` (
  `id` int(11) NOT NULL,
  `mascota_id` int(11) DEFAULT NULL,
  `procedimiento_id` int(11) DEFAULT NULL,
  `costo` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Registros`
--

INSERT INTO `Registros` (`id`, `mascota_id`, `procedimiento_id`, `costo`) VALUES
(1, 1, 1, 150.00),
(2, 2, 2, 35.00),
(3, 3, 3, 50.00),
(4, 4, 4, 50.00),
(5, 5, 5, 475.00),
(6, 6, 6, 75.00),
(7, 7, 7, 50.00),
(8, 8, 8, 300.00),
(9, 9, 9, 650.00),
(10, 10, 10, 75.00),
(11, 11, 11, 75.00),
(12, 12, 12, 300.00),
(13, 13, 13, 75.00),
(14, 14, 14, 50.00),
(15, 15, 15, 75.00),
(16, 16, 16, 190.00),
(17, 17, 17, 50.00),
(18, 18, 18, 7820.00),
(19, 19, 19, 150.00),
(20, 19, 20, 50.00),
(21, 20, 21, 50.00),
(22, 20, 22, 750.00),
(23, 21, 23, 95.00),
(24, 22, 24, 1500.00);

-- --------------------------------------------------------

--
-- Table structure for table `Usuarios`
--

CREATE TABLE `Usuarios` (
  `id` int(11) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `contrasena` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Citas`
--
ALTER TABLE `Citas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mascota_id` (`mascota_id`),
  ADD KEY `procedimiento_id` (`procedimiento_id`);

--
-- Indexes for table `Mascotas`
--
ALTER TABLE `Mascotas`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `PreciosAccesorios`
--
ALTER TABLE `PreciosAccesorios`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Procedimientos`
--
ALTER TABLE `Procedimientos`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Registros`
--
ALTER TABLE `Registros`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mascota_id` (`mascota_id`),
  ADD KEY `procedimiento_id` (`procedimiento_id`);

--
-- Indexes for table `Usuarios`
--
ALTER TABLE `Usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario` (`usuario`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Citas`
--
ALTER TABLE `Citas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `Mascotas`
--
ALTER TABLE `Mascotas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `Procedimientos`
--
ALTER TABLE `Procedimientos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `Registros`
--
ALTER TABLE `Registros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `Usuarios`
--
ALTER TABLE `Usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Citas`
--
ALTER TABLE `Citas`
  ADD CONSTRAINT `Citas_ibfk_1` FOREIGN KEY (`mascota_id`) REFERENCES `Mascotas` (`id`),
  ADD CONSTRAINT `Citas_ibfk_2` FOREIGN KEY (`procedimiento_id`) REFERENCES `Procedimientos` (`id`);

--
-- Constraints for table `Registros`
--
ALTER TABLE `Registros`
  ADD CONSTRAINT `Registros_ibfk_1` FOREIGN KEY (`mascota_id`) REFERENCES `Mascotas` (`id`),
  ADD CONSTRAINT `Registros_ibfk_2` FOREIGN KEY (`procedimiento_id`) REFERENCES `Procedimientos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
