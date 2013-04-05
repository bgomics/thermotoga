-- phpMyAdmin SQL Dump
-- version 3.2.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 05, 2013 at 08:41 PM
-- Server version: 5.1.44
-- PHP Version: 5.3.1

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `Genomes`
--

-- --------------------------------------------------------

--
-- Table structure for table `elfii`
--

CREATE TABLE IF NOT EXISTS `elfii` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7id` int(11) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `elfii`
--


-- --------------------------------------------------------

--
-- Table structure for table `hypogea`
--

CREATE TABLE IF NOT EXISTS `hypogea` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7id` int(11) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `hypogea`
--


-- --------------------------------------------------------

--
-- Table structure for table `lettingae`
--

CREATE TABLE IF NOT EXISTS `lettingae` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7id` int(11) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `lettingae`
--


-- --------------------------------------------------------

--
-- Table structure for table `maritima`
--

CREATE TABLE IF NOT EXISTS `maritima` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7id` int(11) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `maritima`
--


-- --------------------------------------------------------

--
-- Table structure for table `naphthophila`
--

CREATE TABLE IF NOT EXISTS `naphthophila` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7id` int(11) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `naphthophila`
--


-- --------------------------------------------------------

--
-- Table structure for table `neapolitana`
--

CREATE TABLE IF NOT EXISTS `neapolitana` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7id` int(11) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=105 ;

--
-- Dumping data for table `neapolitana`
--


-- --------------------------------------------------------

--
-- Table structure for table `petrophila`
--

CREATE TABLE IF NOT EXISTS `petrophila` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7id` int(11) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `petrophila`
--


-- --------------------------------------------------------

--
-- Table structure for table `RQ7`
--

CREATE TABLE IF NOT EXISTS `RQ7` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `identity` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `RQ7`
--

INSERT INTO `RQ7` (`id`, `identity`) VALUES
(1, 'gRQ7GL000001'),
(2, 'gRQ7GL000160'),
(4, 'gRQ7GL000566'),
(3, 'gRQ7GL000319'),
(5, 'gRQ7GL000983'),
(6, 'gRQ7GL001172 '),
(7, 'gRQ7GL001341  '),
(8, 'gRQ7GL001630'),
(9, 'gRQ7GL001868'),
(10, 'gRQ7GL001768');

-- --------------------------------------------------------

--
-- Table structure for table `subterranea`
--

CREATE TABLE IF NOT EXISTS `subterranea` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7id` int(11) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `subterranea`
--


-- --------------------------------------------------------

--
-- Table structure for table `thermarum`
--

CREATE TABLE IF NOT EXISTS `thermarum` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7id` int(11) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `thermarum`
--

