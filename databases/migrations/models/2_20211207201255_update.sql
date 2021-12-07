-- upgrade --
ALTER TABLE `chairs` ADD `position` VARCHAR(255) NOT NULL;
ALTER TABLE `chairs` ADD `room_id` BIGINT NOT NULL;
ALTER TABLE `chairs` ADD CONSTRAINT `fk_chairs_rooms_469fef6b` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`id`) ON DELETE CASCADE;
-- downgrade --
ALTER TABLE `chairs` DROP FOREIGN KEY `fk_chairs_rooms_469fef6b`;
ALTER TABLE `chairs` DROP COLUMN `position`;
ALTER TABLE `chairs` DROP COLUMN `room_id`;
