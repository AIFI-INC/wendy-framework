-- upgrade --
ALTER TABLE `addresses` MODIFY COLUMN `country_code` VARCHAR(5) NOT NULL  DEFAULT 'jp';
ALTER TABLE `addresses` ALTER COLUMN `country_code` SET DEFAULT 'jp';
-- downgrade --
ALTER TABLE `addresses` MODIFY COLUMN `country_code` INT NOT NULL  DEFAULT 81;
ALTER TABLE `addresses` ALTER COLUMN `country_code` SET DEFAULT 81;
