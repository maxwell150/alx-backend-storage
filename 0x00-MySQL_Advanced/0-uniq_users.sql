-- script that creates a table users
create table if not exists `users` (
    `id` int not null primary key auto_increment,
    `email` varchar(255) not null unique,
    `name` varchar(255)
);
