CREATE TABLE esp(
	id int(11) not null PRIMARY KEY AUTO_INCREMENT,
    temp int(11) not null,
    humidity float(11) not null
);
INSERT INTO `esp`(`id`, `temp`, `humidity`) VALUES (1,10,20);