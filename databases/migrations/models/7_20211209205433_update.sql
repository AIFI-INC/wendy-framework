-- upgrade --
ALTER TABLE `tables` DROP FOREIGN KEY `fk_tables_rooms_3265998f`;
ALTER TABLE `addresses` DROP INDEX `uid_addresses_country_6d219f`;
ALTER TABLE `tables` DROP COLUMN `name`;
ALTER TABLE `tables` DROP COLUMN `room_id`;
ALTER TABLE `addresses` ADD UNIQUE INDEX `uid_addresses_country_59cc36` (`country_code`, `post_code`, `address_1`, `address_2`);
-- downgrade --
ALTER TABLE `addresses` DROP INDEX `uid_addresses_country_59cc36`;
ALTER TABLE `tables` ADD `name` VARCHAR(255) NOT NULL  COMMENT 'name of the table asset';
ALTER TABLE `tables` ADD `room_id` BIGINT NOT NULL;
ALTER TABLE `addresses` ADD UNIQUE INDEX `uid_addresses_country_6d219f` (`country_code`, `post_code`, `address_1`);
ALTER TABLE `tables` ADD CONSTRAINT `fk_tables_rooms_3265998f` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`id`) ON DELETE CASCADE;
