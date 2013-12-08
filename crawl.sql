-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb2
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 08-12-2013 a las 18:14:03
-- Versión del servidor: 5.5.31
-- Versión de PHP: 5.4.4-14+deb7u5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `crawl`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anchor`
--

CREATE TABLE IF NOT EXISTS `anchor` (
  `wid` int(11) NOT NULL,
  `anchor` varchar(1024) COLLATE utf8_unicode_ci NOT NULL,
  `pwid` int(11) NOT NULL,
  KEY `wid` (`wid`),
  KEY `pwid` (`pwid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `links`
--

CREATE TABLE IF NOT EXISTS `links` (
  `wid` int(11) NOT NULL AUTO_INCREMENT,
  `hash` varchar(42) COLLATE utf8_unicode_ci NOT NULL,
  `protocol` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `domain` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `path` varchar(1024) COLLATE utf8_unicode_ci NOT NULL,
  `status` int(11) NOT NULL DEFAULT '0',
  `type` int(11) NOT NULL,
  PRIMARY KEY (`wid`),
  KEY `protocol` (`protocol`),
  KEY `hash` (`hash`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=40 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
