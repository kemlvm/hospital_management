-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 18 Haz 2023, 21:16:51
-- Sunucu sürümü: 10.4.22-MariaDB
-- PHP Sürümü: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `hospital_administrator`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `administrator_table`
--

CREATE TABLE `administrator_table` (
  `id` int(11) NOT NULL,
  `username` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `password` text COLLATE utf8mb4_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

--
-- Tablo döküm verisi `administrator_table`
--

INSERT INTO `administrator_table` (`id`, `username`, `password`) VALUES
(1, 'kemal', '12345');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `patients`
--

CREATE TABLE `patients` (
  `id` int(11) NOT NULL,
  `name` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `surname` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `disease_illness` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `blood_group` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `age` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `kilo` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `size` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `mothers_name` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `fathers_name` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `allergic_diseases` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `covid_vaccine_status` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `tc_no` text COLLATE utf8mb4_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

--
-- Tablo döküm verisi `patients`
--

INSERT INTO `patients` (`id`, `name`, `surname`, `disease_illness`, `blood_group`, `age`, `kilo`, `size`, `mothers_name`, `fathers_name`, `allergic_diseases`, `covid_vaccine_status`, `tc_no`) VALUES
(8, 'kemal', 'ünlü', 'grip', 'ab+', '20', '70', '180', 'anne adı', 'baba adı', 'polen', '1 Doz', '1111111111');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `administrator_table`
--
ALTER TABLE `administrator_table`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `administrator_table`
--
ALTER TABLE `administrator_table`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Tablo için AUTO_INCREMENT değeri `patients`
--
ALTER TABLE `patients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
