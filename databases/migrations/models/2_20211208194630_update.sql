-- upgrade --
ALTER TABLE `addresses` ADD UNIQUE INDEX `uid_addresses_post_co_2de388` (`post_code`, `address_1`);
-- downgrade --
ALTER TABLE `addresses` DROP INDEX `uid_addresses_post_co_2de388`;
