-- phpMyAdmin SQL Dump
-- version 3.2.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 18, 2013 at 03:40 PM
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
  `row` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7identity` varchar(20) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`row`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `hypogea`
--

CREATE TABLE IF NOT EXISTS `hypogea` (
  `row` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7identity` varchar(20) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`row`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `lettingae`
--

CREATE TABLE IF NOT EXISTS `lettingae` (
  `row` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7identity` varchar(20) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`row`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

-- --------------------------------------------------------

--
-- Table structure for table `maritima`
--

CREATE TABLE IF NOT EXISTS `maritima` (
  `row` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7identity` varchar(20) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`row`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=24 ;

-- --------------------------------------------------------

--
-- Table structure for table `naphthophila`
--

CREATE TABLE IF NOT EXISTS `naphthophila` (
  `row` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7identity` varchar(20) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`row`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=18 ;

-- --------------------------------------------------------

--
-- Table structure for table `neapolitana`
--

CREATE TABLE IF NOT EXISTS `neapolitana` (
  `row` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7identity` varchar(20) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`row`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=20 ;

-- --------------------------------------------------------

--
-- Table structure for table `petrophila`
--

CREATE TABLE IF NOT EXISTS `petrophila` (
  `row` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7identity` varchar(20) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`row`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=18 ;

-- --------------------------------------------------------

--
-- Table structure for table `RQ7`
--

CREATE TABLE IF NOT EXISTS `RQ7` (
  `row` int(11) NOT NULL,
  `identity` varchar(20) NOT NULL,
  PRIMARY KEY (`identity`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `subterranea`
--

CREATE TABLE IF NOT EXISTS `subterranea` (
  `row` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7identity` varchar(20) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`row`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `thermarum`
--

CREATE TABLE IF NOT EXISTS `thermarum` (
  `row` int(11) NOT NULL AUTO_INCREMENT,
  `RQ7identity` varchar(20) NOT NULL,
  `locus` text NOT NULL,
  `gi` int(11) NOT NULL,
  PRIMARY KEY (`row`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=17 ;
