-- upgrade --
ALTER TABLE `addresses` DROP INDEX `uid_addresses_post_co_2de388`;
ALTER TABLE `addresses` ADD UNIQUE INDEX `uid_addresses_country_6d219f` (`country_code`, `post_code`, `address_1`);
-- downgrade --
ALTER TABLE `addresses` DROP INDEX `uid_addresses_country_6d219f`;
ALTER TABLE `addresses` ADD UNIQUE INDEX `uid_addresses_post_co_2de388` (`post_code`, `address_1`);
