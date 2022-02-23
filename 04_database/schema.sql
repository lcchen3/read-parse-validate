-- create database

DROP DATABASE IF EXISTS `Farm`;
CREATE DATABASE IF NOT EXISTS `Farm`;
USE `Farm`;

-- create table

CREATE TABLE `Customers`(
    `FirstName`  varchar(20) NULL, -- variable character type up to 20 characters, want to limit this
    `LastName`   varchar(20) NULL,
    `Email`      varchar(20) NULL
);
-- semicolon means commit
-- sample

INSERT INTO `Customers` VALUES
    ('kara','danvers','kara@mit.edu'),
    ('alice','zehner','alice@mit.edu')