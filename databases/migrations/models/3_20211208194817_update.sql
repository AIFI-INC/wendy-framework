-- upgrade --
ALTER TABLE `addresses` MODIFY COLUMN `province` VARCHAR(255);
ALTER TABLE `addresses` MODIFY COLUMN `post_code` VARCHAR(50) NOT NULL;
ALTER TABLE `addresses` MODIFY COLUMN `city` VARCHAR(255);
-- downgrade --
ALTER TABLE `addresses` MODIFY COLUMN `province` VARCHAR(255) NOT NULL;
ALTER TABLE `addresses` MODIFY COLUMN `post_code` VARCHAR(50);
ALTER TABLE `addresses` MODIFY COLUMN `city` VARCHAR(255) NOT NULL;
