create database if not exists zx;
create user if not exists zxuser identified by 'zxuser';
GRANT ALL PRIVILEGES ON *.* TO 'zxuser';
GRANT ALL PRIVILEGES ON *.* TO 'zxuser'@'localhost';
commit;
end;
